#!/usr/bin/env python3
import math_lib
import fileinput
import re
import math

def xavg(l):
    """Function xavg for calculating the average value of x
    input is a list of numbers, output is an average value of them
    """
    return math_lib.div(sum(l),len(l))

def inputf():
    """Function inputf for getting input from stdin
    takes input from stdin and returns a list of numbers found in stdin
    """
    tmp=[]
    for line in fileinput.input():
        tmp=tmp+(re.findall('[0-9]+',line))
    return [float(n) for n in tmp]
        
def deviation(lst):
    """Function deviation for calculating standard deviation
    input is a list of numbers
    """
    n=len(lst)    
    result=math.sqrt(math_lib.div(math_lib.sub(sum(i*i for i in lst),math_lib.mul(n,math.pow(xavg(lst),2))),n-1))   
    return result

list=inputf()
print(deviation(list))