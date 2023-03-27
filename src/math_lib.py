#!/usr/bin/env python3
"""@package math_lib
This module includes basic mathematical functions.

Each function in this module represents equivalent mathematical function.
This module can be used for general purposes, but was designed
to be used in calculator application.
"""

import math

def add(x: int | float, y: int | float) -> int | float:
    """Documentation for a function.
 
    More details.
    """
    return x + y
    pass

def sub(x: int | float, y: int | float) -> int | float:
    """Documentation for a function.
 
    More details.
    """
    return x - y
    pass

def mul(x: int | float, y: int | float) -> int | float:
    """Documentation for a function.
 
    More details.
    """
    return x * y
    pass

def div(x: int | float, y: int | float) -> int | float:
    """Documentation for a function.
 
    More details.
    """
    return x / y
    pass

def fac(x: int) -> int:
    """Documentation for a function.
 
    More details.
    """
    if x < 0:
        return -444
    elif x == 0:
        return 1
    else:
        return x * fac(x-1)
    pass

def pow(x: int | float, n: int | float) -> int | float:
    """Documentation for a function.
 
    More details.
    """
    return pow(x, n)
    pass

def sqrt(x: int | float, n: int | float) -> int | float:
    """n is an index for root function
    x is a radicand od function
    the function works as: n root of x
    More details.
    """
    return pow(n, 1/x)
    pass

def log(x: int | float, n: int | float) -> int | float:
    """x is number argument of logarithm
    n is number of logarithms base
    More details.
    """
    return math.log(x,n)
    pass

def change_sign(x: int | float) -> int | float:
    """Documentation for a function.
 
    More details.
    """
    return -1 * x
    pass
