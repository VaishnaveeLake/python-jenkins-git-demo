# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 17:08:58 2021

@author: VaishnaveeLake
"""

class Person:
    company="ibm"
    persons=1000
    def __init__(self,name,persons):
        self.name=name
        self.persons=persons
    def sayHello(self,msg=" Python"):
        print(f'hello {msg}')
    def get_total_persons(self):
        print(self.persons)
        
person = Person('manu',500)
person.sayHello("nodejs")
person.get_total_persons()
print(person.name)

print(person.company)
print(type(person))