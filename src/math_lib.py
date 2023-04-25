#!/usr/bin/env python3

##
# @file math_lib.py
#
# @brief This module includes basic mathematical functions.
#
# @section description_doxygen_example Description
# Each function in this module represents equivalent mathematical function.
# This module can be used for general purposes, but was designed
# to be used in calculator application.
#
# @section libraries_main Libraries/Modules
# - math (https://docs.python.org/3/library/math.html)
#   - Access to mathematical functions.
#
#
# @section author_doxygen_example Author(s)
# - Created by Jaroslav Ištvan on 04/24/2023.
#
# Copyright (c) 2023 xpodvo00-ivs-team. All rights reserved.


import math

def add(x: int | float, y: int | float) -> int | float:
    """! @brief Function add for adding two numbers.
    @param x First operand of type int or float
    @param y Second operand of type int or float
    @return Result of type int or float
    """
    return round(x + y, 10)


def sub(x: int | float, y: int | float) -> int | float:
    """! @brief Function sub for subtracting two numbers.
    @param x First operand of type int or float
    @param y Second operand of type int or float
    @return Result of type int or float
    """
    return round(x - y, 10)


def mul(x: int | float, y: int | float) -> int | float:
    """! @brief Function mul for multiplying two numbers.
    @param x First operand of type int or float
    @param y Second operand of type int or float
    @return Result of type int or float
    """
    return round(x * y, 10)


def div(x: int | float, y: int | float) -> int | float:
    """! @brief Function div for dividing two numbers.
    @param x First operand of type int or float
    @param y Second operand of type int or float
    @return Result of type int or float
    """
    return round(x / y, 10)


def fac(x: int) -> int:
    """! @brief Function fac for calculating factorial of a number.
    @param x Input number
    @return Factorial value of the input number
    """
    if x < 0:
        return 0
    elif x == 0:
        return 1
    else:
        return x * fac(x-1)


def pow(x: int | float, n: int | float) -> int | float:
    """! @brief Function pow for calculating power of a number.
    @param x Base number of type int or float
    @param n Exponent
    @return Result (x^n) of type int or float
    """
    return round(math.pow(x, n), 10)


def sqrt(x: int | float, n: int | float) -> int | float:
    """! @brief Function sqrt for calculating n root of a number.
    @param x Number of type int or float
    @param n Root degree
    @return Result (x root n) of type int or float
    """
    return round(math.pow(n, 1/x), 10)


def log(x: int | float, n: int | float) -> int | float:
    """! @brief Function log for calculating logarithm of a number.
    @param x Number of type int or float
    @param n Logarithm degree
    @return Result (n log(x)) of type int or float
    """
    return round(math.log(x,n), 10)


def change_sign(x: int | float) -> int | float:
    """! @brief Function change_sing for inverting sign of an input number
    @param x Number of type int or float
    @return Number with changed sign
    """
    return round(-1 * x, 10)


# End of file math_lib.py
