import numpy as np
from scipy.optimize import *
from math import cos, atan

SLSQP = "SLSQP"

def f_x(x):
    return x


def min_f(x):
    return x**2


def foo(x):
    return x**2


def f(x):
    return 0.1 * x[0] * x[1]


def ineq_constraint(x):
    return x[0]**2 + x[1]**2 - (5. + 2.2 * cos(10 * atan(x[0] / x[1])))**2


con = {'type': 'ineq', 'fun': ineq_constraint}
x0 = np.array([1, 1])
print(minimize(f, x0, method='SLSQP', constraints=con))

# TODO: block : x < 8 won't happen

# x0 = np.array([1, 2, 3, 4, 5, 6])
# nonlinearconstraint = {'type': 'eq', 'fun': NonlinearConstraint(f_x, lb=-np.inf, ub=10, jac='2-point')}
# print(minimize(min_f, x0, method=SLSQP, constraints=nonlinearconstraint))