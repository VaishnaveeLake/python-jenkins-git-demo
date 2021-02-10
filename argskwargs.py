# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:55:09 2021

@author: VaishnaveeLake
"""

def myfun(*args):
    print(args)
    print(type(args))
    for a in args:
        print(a)
    
myfun(1,2,3,'java',5.7,'nodejs')
    
def newfunc(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key,value in kwargs.items():
        print('key:',key,'  value:',value)

newfunc(name="manu",add="solapur",company="IBM")
  
def order(name, *dishes,**kwargs):
    print(f"Hello {name}")  
    print("your orders are")                  # f indicates formattable string
    for dish in dishes:                 #{dish} asa bracket madhe indicate karun print karaych asel tr f use karaych
        print(f"{dish}")        #or we can write print(dish) only
    if kwargs.get("address"):
        address=kwargs.get("address")
        print(f"we are delivering to {address}")
        
order("manu","rice","dal","chicken","coffee",address="solapr")