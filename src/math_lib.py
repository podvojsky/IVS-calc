#!/usr/bin/env python3
"""@package math_lib
This module includes basic mathematical functions.

Each function in this module represents equivalent mathematical function.
This module can be used for general purposes, but was designed
to be used in calculator application.
"""

import math

def add(x: int | float, y: int | float) -> int | float:
    """Function add for adding two numbers
    uses input variables x and y of data type int or float
    output data type is int or float
    """
    return x + y
    pass

def sub(x: int | float, y: int | float) -> int | float:
    """Function sub for subtracting two numbers
    uses input variables x and y of data type int or float
    output data type is int or float
    """
    return x - y
    pass

def mul(x: int | float, y: int | float) -> int | float:
    """Function mul for multiplying two numbers
    uses input variables x and y of data type int or float
    output data type is int or float
    """
    return x * y
    pass

def div(x: int | float, y: int | float) -> int | float:
    """Function div for dividing two numbers
    uses input variables x and y of data type int or float
    output data type is int or float
    """
    return x / y
    pass

def fac(x: int) -> int:
    """Function fac for calculating factorial of a number
    uses input variable x of data type int
    output data type is int
    """
    if x < 0:
        return -444
    elif x == 0:
        return 1
    else:
        return x * fac(x-1)
    pass

def pow(x: int | float, n: int | float) -> int | float:
    """Function pow for calculating power of a number
    uses input variables x and n of data type int or float
    output data type is int or float
    output is result of x to the power of n: x^n
    """
    return pow(x, n)
    pass

def sqrt(x: int | float, n: int | float) -> int | float:
    """Function sqrt for calculating n root of a number
    uses input variables x and n of data type int or float
    output data type is int or float
    n is an index for root function and x is a radicand od function
    output is result of: n root of x
    """
    return pow(n, 1/x)
    pass

def log(x: int | float, n: int | float) -> int | float:
    """Function log for calculating logarithm of a number
    uses input variables x and n of data type int or float
    output data type is int or float
    x is number argument of logarithm
    n is number of logarithms base
    output is result of: n log(x)
    """
    return math.log(x,n)
    pass

def change_sign(x: int | float) -> int | float:
    """Function change_sing for inverting sign of an input number
    uses input variable x of data type int or float
    output data type is int or float
    """
    return -1 * x
    pass
