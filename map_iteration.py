# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:55:50 2021

@author: VaishnaveeLake
"""

data=[5,10,15,20,25]
print(list(map(lambda x:x*5 ,data)))

#or 
def mul(data):
    return data*5

a=map(mul,data)
print(list(a)) 