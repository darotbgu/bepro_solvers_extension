import numpy as np
from composers.MinimizeComposer import MinimizeComposer
from ThreadsRunner import ThreadsRunner


def div_by_2(x):
    return sum(i/2 for i in x)


def div_by_3(x):
    return sum(i/3 for i in x)


def obj_func(x):
    bo,ho,t1,t2=x
    f=-321226.4817 + (10400000*bo*ho**3 - 10400000*(bo - 2*t2)*(ho - 2*t1)**3)/(125 + (10400000*bo*ho**3 - 10400000*(bo - 2*t2)*(ho - 2*t1)**3)/(1563920*t1*(bo - 2*t2)))
    return f


def first_thread(x):
    cons = {'type': 'eq', 'fun': lambda z: (z[0] * z[1] - (z[0] - 2 * z[3]) * (z[1] - 2 * z[2]) - 7.55)}

    bound = [[0.3, 10], [0.3, 10], [0.3, 10], [0.3, 10]]

    yield {"request": {"x": x, "fun": div_by_3},
           "block": {"bound": bound, "constraints": [cons]}}


def second_thread(x):
    cons = {'type': 'ineq', 'fun': lambda z: 0.1}
    bound = [[0.1, 100], [0.2, 100], [0.1, 100], [0.1, 100]]

    yield {"request": {"x": x, "fun": div_by_2},
           "block": {"bound": bound, "constraints": [cons]}}


def third_thread(x):
    bound = [[3, 10], [3, 10], [3, 10], [3, 10]]

    yield {"request": {"x": x, "fun": lambda x: sum(i+2 for i in x)}, "block": {"bound": bound, "constraints": []}}


def fourth_thread(x):
    bound = [[4, 36], [4, 36], [4, 36], [4, 36]]
    yield {"request": {"x": x, "fun": lambda x: sum(i**2 for i in x)}, "block": {"bound": bound, "constraints": []}}


def main():
    x = np.array([2, 2, 0.2, 0.2])

    bthreads = [first_thread(x), second_thread(x), third_thread(x), fourth_thread(x)]
    composer = MinimizeComposer(np.linalg.norm)
    runner = ThreadsRunner(bthreads, composer)
    runner.run()


if __name__ == '__main__':
    main()





