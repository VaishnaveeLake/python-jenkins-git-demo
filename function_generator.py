# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:30:02 2021

@author: VaishnaveeLake
"""

def myFunctionGenerator(n):
    #yield "something"
    #result =[]
    for x in range(n):
        yield x*2
    #return result

#numbers = myFunctionGenerator(10)
#print(numbers)    

for num in myFunctionGenerator(5):
    print(num)
    
number=myFunctionGenerator(10)
for num1 in number:
    print(num)
    
    
    
    
    
    