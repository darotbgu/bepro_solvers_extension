from z3 import *

true = BoolSort().cast(True)
false = BoolSort().cast(False)

hot = Bool("hot")
cold = Bool("cold")
func = Real("func")


def no_two_hot_in_a_row():
    while True:
        yield {'wait-for': hot}
        yield {'block': hot, 'wait-for': cold}


def no_two_cold_in_a_row():
    while True:
        yield {'wait-for': cold}
        yield {'block': cold, 'wait-for': hot}


def three_hot():
    for i in range(3):
        yield {'request': hot, 'wait-for': hot}


def three_cold():
    for j in range(3):
        yield {'request': cold, 'wait-for': cold}


def exclusion():
    while True:
        yield {'block': And(hot, cold, func>3)}


#############################################################

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
