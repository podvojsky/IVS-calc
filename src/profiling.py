#!/usr/bin/env python3

##
# @file stddev.py
#
# @brief This module implements algorithm for
# calculation of standard deviation from given
# data on standard input.
#
#
# @section author_doxygen_example Author(s)
# - Created by David Formánek on 04/24/2023.
#
# Copyright (c) 2023 xpodvo00-ivs-team. All rights reserved.


import math_lib
import fileinput
import re
import sys

def xavg(lst):
    """! @brief Function xavg for calculating the average value of x.
    @param List of numbers
    @return Average value of input numbers
    """
    return math_lib.div(sum(lst),len(lst))

def inputf():
    """! @brief Function inputf for getting input from stdin.
    @return List of numbers found in stdin
    """
    nline=[] #A list of numbers inputted on a line
    nlist=[] #A list of the inputted numbers
    for line in fileinput.input():
        nline=(re.findall('[0-9]+',line))
        nlist=nlist+nline
    return [float(n) for n in nlist]
        
def deviation(lst):
    """! @brief Function deviation for calculating standard deviation.
    @param List of numbers
    """
    n=len(lst) #The number of numbers in the list
    if n==0:
        print("No numbers were found in the input")
        sys.exit()
    tmp5=math_lib.pow(xavg(lst),2) 
    tmp4=math_lib.mul(n,tmp5)                   
    tmp3=sum(i*i for i in lst)    
    tmp2=math_lib.sub(tmp3,tmp4)                
    tmp1=math_lib.div(tmp2,n-1)                 
    return math_lib.sqrt(2,tmp1)                

def main():
    """! @brief Main part of stddev.
    """
    list=inputf()
    print(deviation(list))

if __name__ == "__main__":
    main()


# End of file stddev.py
