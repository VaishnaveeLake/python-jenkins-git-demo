# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 13:01:40 2021

@author: VaishnaveeLake
"""

def my_decorator(original_func):
    def wrapper():
        print("inside wrapper function before")
        
        original_func()
        print("execute after")
    
    return wrapper

@my_decorator
def sayHello():
    print("say hello")
    
sayHello()