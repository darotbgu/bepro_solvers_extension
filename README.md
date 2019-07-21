# Mechanisem for Solvers Using Behavioral Programming

A scenario-based execution mechanism based on bpjs, expanded with python
 
Extending python BP to allow wrapping every desired solver.
In our project we showed two POC (Proof of Concept):
1. Z3 Solver
  
2. Optimization solver using SciPy (NumPy)  

  "SciPy optimize provides functions for minimizing (or maximizing) objective functions, 
  possibly subject to constraints. It includes solvers for nonlinear problems
  (with support for both local and global optimization algorithms), linear programing, constrained and nonlinear least-squares, root finding and curve fitting."
 
 Scipy documentaion:
  https://docs.scipy.org/doc/scipy/reference/optimize.html#module-scipy.optimize
  

### Components:

## Composer
Each composer implements the selection of the next event, and the advancing of the bThreads according to the used solver in this composer.
In addition, the composer composed the "snapshots" in the suitable way for the solver. From the composed "snapshots" which the next event will be chosen.


## ThreadRunner
Advance the existing bThreads and call nextEvent, using the given Composer.
The ThreadRunner holds the current "snapshot" of the threads, 

# ####

This mechanism allow you to use BP with any chosen solver, by creating new Composers.

You can see some examples in threads folder.
