# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 11:56:52 2021

@author: VaishnaveeLake

number (int(y[base]),float(y),complex(real[img]))

tuple(y)
list(y)
set(y)
dict(y)
hex(y)
oct(y)
"""

# num1=55
# num2=15.6
# add= num1+num2  #implicit type conversion(typecasting)
# print(add,type(add))

num1=85
num2="55"
print('Data type of num1:',type(num1))
print('Data type of num2:',type(num2))
num2=int(num2)
print('Data type of num2 after casting:',type(num2))
add=num1+num2
print(type(add))