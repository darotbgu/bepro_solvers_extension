from utils.numpyUtils import *
from .BaseComposer import BaseComposer


class MinimizeComposer(BaseComposer):

    def __init__(self, func):
        super().__init__()
        self._func = func

    @staticmethod
    def wrap(accum, f):
        return lambda x: f(accum(x))

    @staticmethod
    def get_smaller_bound(bounds):
        min_bound = []
        for bound in bounds:
            if not min_bound:
                min_bound = bound
                continue

            for i in range(len(bound)):
                lower = bound[i][0]
                upper = bound[i][1]
                if lower > min_bound[i][0]:
                    min_bound[i][0] = lower
                if upper < min_bound[i][1]:
                    min_bound[i][1] = upper
        return min_bound

    def compose(self, snapshots):
        cons = []
        bounds = []
        new_x = []

        for ss in snapshots:
            request = ss.get("request")
            block = ss.get("block")

            if request:
                origin_x = request.get("x", None)
                if origin_x is None:
                    raise KeyError("Expected x vector")
                new_x.append(request.get("fun")(origin_x))

            if block:
                cons.extend(block.get("constraints"))
                bounds.append(block.get("bound"))

        return {"x": new_x, "fun": self._func}, \
               {"bound": MinimizeComposer.get_smaller_bound(bounds), "constraints": cons}

    def next_event(self, requested, blocked):
        return minimize_equation(requested.get("fun"), requested.get("x")

                                 , bounds=blocked.get("bound")
                                 , constraints=blocked.get("constraints"))

    def advance_bthreads(self, event, snapshots):
        success = True
        bound = ()
        constraints = []
        for ss in snapshots:
            request = ss.get("request")
            block = ss.get("block")
            if request:
                fun = request.get("fun", None)

            if block:
                constraints = block.get("constraints")
                bound = block.get("bound")
            min_res = minimize_equation(fun, x=event.x, bounds=bound, constraints=constraints)
            if min_res.success:
                success = success and min_res.success
                new_x = min_res.x
                print("New X:\n", new_x)
                ss.update({
                    "request": {"x": event.x, "fun": fun},
                    "block": {"bound": bound, "constraints": constraints}
                })
                ss.update(next(ss['bt'], {}))
        if not success:
            exit(0)


