# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 17:22:44 2021

@author: VaishnaveeLake
"""

class Shape:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def calculatearea(self):
        raise NotImplementedError('calculate area not omplemented') #if any of method is not implemented use this error
    
class Rectangle(Shape):         #inheritance we can inherit many fun by using comma but it takes first wrote class as first in sequence
    def calculatearea(self):
        return self.width*self.height
        
class Triangle(Shape):
    def calculatearea(self):
        return 0.5*self.height*self.width

rectangle =Rectangle(25.5,24)
print(rectangle.calculatearea())


triangle =Triangle(25.5,24)
print(triangle.calculatearea())
