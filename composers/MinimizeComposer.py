from utils.numpyUtils import *
from .BaseComposer import BaseComposer


class MinimizeComposer(BaseComposer):

    def __init__(self, func):
        super().__init__()
        self._func = func

    @staticmethod
    def wrap(accum, f):
        return lambda x: f(accum(x))

    def compose(self, snapshots):
        cons = []
        bound = ()

        new_x = []
        origin_x = 0

        for ss in snapshots:
            origin_x = ss.get("request").get("x")
            new_x.append(ss.get("request").get("fun")(origin_x))
            cons.extend(ss.get("block").get("constraints"))
            bound = ss.get("block").get("bound")
        new_x.extend([0] * (len(origin_x) - len(new_x)))

        return {"x": new_x, "fun": self._func}, {"bound": bound, "constraints": cons}

    def next_event(self, requested, blocked):
        return minimize_equation(requested.get("fun"), requested.get("x")

                                 , bounds=blocked.get("bound")
                                 , constraints=blocked.get("constraints"))

    def advance_bthreads(self, event, snapshots):
        # print("Event:\n", event)
        success = True
        for ss in snapshots:
            fun = ss.get("request").get("fun")
            constraints = ss.get("block").get("constraints")
            bound = ss.get("block").get("bound")
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


