# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:39:29 2021

@author: VaishnaveeLake
"""

def add(x):
    def add2(y):
        return x+y
    return add2
a=add(5)
print(a)