# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:39:29 2021

@author: VaishnaveeLake
"""

# def add1(x):
#     def add2(y):
#         return x+y
#     return add2

# print(add1(10)(20))
 #OR


def add(y):
    return lambda x: y+x
a = add(7)(6)
print(a)
    