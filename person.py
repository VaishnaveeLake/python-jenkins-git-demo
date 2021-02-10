# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 16:49:41 2021

@author: VaishnaveeLake
"""

class Person:                    #person() or person is allowed
    def __int__(self,name):
        self.name=name
    def sayHello(self,msg="Hello python"):
        print(msg)
       


person = Person('someone')
person.sayHello()
print(person.name)
print(type(person))
