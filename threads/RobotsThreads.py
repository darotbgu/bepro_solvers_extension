import numpy as np
from utils.graphUtil import draw

x_start = np.array([0, 0.2, 0.2, 0.4])
y_start = np.array([0.8, 1, 0.6, 0.8])

target_x = 0.9
target_y = 0.1

x = np.array([(0, 0.8), (0.2, 1), (0.2, 0.6), (0.4, 0.8)])
x_tag = x
length = 4

bounds = ((0,0), (1,1))

def lower_bound(i, n):
    return 0.2 + 0.2*np.cos((2*np.pi * i) / n)


def upper_bound(i, n):
    return 0.8 + 0.2 * np.sin((2*np.pi * i) / n)


def block_not_equal_lower():
    yield {"block": {"bound": [(None, lower_bound(i, length)) for i in range(length)]}}


def block_not_equal_upper():
    yield {"block": {"bound": [(upper_bound(i, length), None) for i in range(length)]}}


def block_derive():
    yield {"block": {"constraints": {}}}


def specific_point():
    return abs(sum([x_tag[i] - [target_x, target_y] for i in range(length)])/length)


def specific_point_thread():
    yield {"request": specific_point, "block": bounds}


def main():
    robot_x = 0.9
    robot_y = 0.1

    bound = ((0, 1), (0, 1), (0, 1), (0, 1))

    center_x = 0.2
    center_y = 0.8

    draw(x)
    #
    # bthreads = [first_thread(first), second_thread(second)]
    # composer = MinimizeComposer(np.linalg.norm)
    # runner = ThreadsRunner(bthreads, composer)
    # runner.run()


if __name__ == '__main__':
    main()
