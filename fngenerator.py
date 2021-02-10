# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:03:49 2021

@author: VaishnaveeLake
"""

def myFunctionGenerator(n):
    
    for x in range(n):
        yield x*2
   
gen =myFunctionGenerator(3)
print(next(gen))            #it returns next value
print(next(gen))
print(next(gen))
#print(next(gen))

