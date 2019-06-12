from ThreadsRunner import ThreadsRunner
from composers.Z3Composer import Z3Composer
from utils.solverUtils import *

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


def main():
    bthreads = [three_cold(), three_hot(), exclusion(), no_two_hot_in_a_row(), no_two_cold_in_a_row()]
    composer = Z3Composer()
    runner = ThreadsRunner(bthreads, composer)
    runner.run()


if __name__ == '__main__':
    main()
