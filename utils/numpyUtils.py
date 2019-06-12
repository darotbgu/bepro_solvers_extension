import numpy as np
from scipy.optimize import *

SLSQP = "SLSQP"
TRUST_CONSTR = "trust-constr"

# TODO: add the rest of the methods, see if there is an enum


def minimize_equation(func, x, bounds, constraints):
    # expecting to get numpy array

    return minimize(func, x, bounds=bounds, constraints=constraints)


def f_x(x):
    return x
