import numpy as np
from scipy.optimize import *
from math import cos, atan

def func(x):
    return x


def foo(x):
    return x**2


def f(x):
    return 0.1 * x[0] * x[1]


def ineq_constraint(x):
    return x[0]**2 + x[1]**2 - (5. + 2.2 * cos(10 * atan(x[0] / x[1])))**2


con = {'type': 'ineq', 'fun': ineq_constraint}
x0 = np.array([1, 1])
print(minimize(f, x0, method='SLSQP', constraints= con))

