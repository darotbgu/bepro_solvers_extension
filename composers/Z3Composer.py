from utils.solverUtils import *
from .BaseComposer import BaseComposer


class Z3Composer(BaseComposer):

    def __init__(self):
        super().__init__()

    def compose(self, snapshots):
        requested, blocked = (false, false)

        for ss in snapshots:
            requested = Or(requested, ss.get('request', false))
            blocked = Or(blocked, ss.get('block', false))

        return requested, blocked

    def next_event(self, requested, blocked):
        sl = Solver()

        sl.add(And(requested, Not(blocked)))

        if sl.check() == sat:
            return sl.model()
        else:
            return None

    def advance_bthreads(self, event, snapshots):
        for ss in snapshots:

            if is_true(event.eval(ss.get('wait-for', true))):
                ss.update({'wait-for': true, 'request': false, 'block': false})
                ss.update(next(ss['bt'], {}))
