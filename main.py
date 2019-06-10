from solverUtils import *
from threads import *


def collectInitialSnapshots(bthreads):
    snapshots = []

    for bt in bthreads:
        ss = next(bt)
        ss['bt'] = bt
        snapshots.append(ss)

    return snapshots


def nextEvent(snapshots):
    requested, blocked = (false, false)

    for ss in snapshots:
        requested = Or(requested, ss.get('request', false))
        blocked = Or(blocked, ss.get('block', false))

    sl = Solver()

    sl.add(And(requested, Not(blocked)))

    if sl.check() == sat:
        return sl.model()
    else:
        return None


def advanceBThreads(e, snapshots):
    for ss in snapshots:

        if is_true(e.eval(ss.get('wait-for', true))):
            ss.update({'wait-for': true, 'request': false, 'block': false})
            ss.update(next(ss['bt'], {}))


def run(bthreads):
    snapshots = collectInitialSnapshots(bthreads)

    while True:
        e = nextEvent(snapshots)

        if e is None:
            return

        print("Event--->", e)

        advanceBThreads(e, snapshots)


run([three_cold(), three_hot(), exclusion(),
     no_two_hot_in_a_row(), no_two_cold_in_a_row()])

# TODO: add class for composition
# TODO: add numpy utils
