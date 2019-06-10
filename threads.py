from collections import namedtuple
from solverUtils import Bool, Real, And

bThread = namedtuple("bThread", ["request", "waitfor", "block"])

WAITFOR = "wait-for"
BLOCK = "block"
REQUEST = "request"

hot = Bool("hot")
cold = Bool("cold")
func = Real("func")


def no_two_hot_in_a_row():
    while True:
        yield {'wait-for': hot}
        # yield bThread(waitfor=hot, request=None, block=None)
        yield {'block': hot, 'wait-for': cold}
        # yield bThread(block=hot, waitfor=cold, request=None)


def no_two_cold_in_a_row():
    while True:
        yield {'wait-for': cold}
        # yield bThread(waitfor=cold, request=None, block=None)
        yield {'block': cold, 'wait-for': hot}
        # yield bThread(block=cold, waitfor=hot, request=None)


def three_hot():
    for i in range(3):
        # yield bThread(request=hot, waitfor=hot, block=None)
        yield {'request': hot, 'wait-for': hot}


def three_cold():
    for j in range(3):
        # yield bThread(request=cold, waitfor=cold, block=None)
        yield {'request': cold, 'wait-for': cold}


def exclusion():
    while True:
        # yield bThread(block=And(hot, cold, func > 3), waitfor=None, request=None)
        yield {'block': And(hot, cold, func>3)}
