import numpy as np
from composers.MinimizeComposer import MinimizeComposer
from ThreadsRunner import ThreadsRunner

robot_x = 0.1
robot_y = 0.9

bound = ((0, 1), (0, 1), (0, 1), (0, 1))
x_start = [0, 0.2, 0.2, 0.4]
y_start = [0.8, 1, 0.6, 0.8]


center_x = 0.2
center_y = 0.8

def block():
    pass

def div_by_2(x):
    return sum(i/2 for i in x)


def div_by_3(x):
    return sum(i/3 for i in x)


def obj_func(x):
    bo,ho,t1,t2=x
    f=-321226.4817 + (10400000*bo*ho**3 - 10400000*(bo - 2*t2)*(ho - 2*t1)**3)/(125 + (10400000*bo*ho**3 - 10400000*(bo - 2*t2)*(ho - 2*t1)**3)/(1563920*t1*(bo - 2*t2)))
    return f


def first_thread(x):
    cons = {'type': 'ineq', 'fun': lambda z: (z[0] * z[1] - (z[0] - 2 * z[3]) * (z[1] - 2 * z[2]) - 7.55)}

    # bnds = ((0, 1), (0.3, 10), (0.3, 10), (0.3, 10))
    # while True:
    yield {"request": {"x": x, "fun": div_by_3},
                   "block": {"bound": bound, "constraints": [cons]}}


def second_thread(x):
    cons = {'type': 'ineq', 'fun': lambda z: 0.1}
    # bnds = ((0.1, 100), (0.2, 100), (0.1, 100), (0.1, 100))  # all four variables are positive and greater than zero

    yield {"request": {"x": x, "fun": div_by_2},
           "block": {"bound": bound, "constraints": [cons]}}

    # m = yield {"request": {"x": x, "fun": power_by_3},
    #            "block": [NonlinearConstraint(f_x, lb=-np.inf, ub=5, jac='2-point', hess=BFGS())]}
               # "block": [{"type": "eq",
               #           "fun": NonlinearConstraint(f_x, lb=-np.inf, ub=5, jac='2-point')}]}


def main():
    first = np.array([2, 2, 0.2, 0.2])
    second = np.array([4, 4, 0.4, 0.4])

    bthreads = [first_thread(first), second_thread(second)]
    composer = MinimizeComposer(np.linalg.norm)
    runner = ThreadsRunner(bthreads, composer)
    runner.run()


if __name__ == '__main__':
    main()





