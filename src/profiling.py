#!/usr/bin/env python3
import math_lib
import fileinput
import re

def xavg(l):
    """Function xavg for calculating the average value of x
    input is a list of numbers, output is an average value of them
    """
    return math_lib.div(sum(l),len(l))

def inputf():
    """Function inputf for getting input from stdin
    takes input from stdin and returns a list of numbers found in stdin
    """
    nline=[]
    nlist=[]
    for line in fileinput.input():
        nline=(re.findall('[0-9]+',line))
        nlist=nlist+nline
    return [float(n) for n in nlist]
        
def deviation(lst):
    """Function deviation for calculating standard deviation
    input is a list of numbers
    """
    n=len(lst)    

    tmp4=math_lib.mul(n,math_lib.pow(xavg(lst),2))
    tmp3=sum(math_lib.pow(i,2) for i in lst)
    tmp2=math_lib.sub(tmp3,tmp4)
    tmp1=math_lib.div(tmp2,n-1)
    return math_lib.sqrt(tmp1,2) 

list=inputf()
print(deviation(list))