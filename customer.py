# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 17:50:11 2021

@author: VaishnaveeLake
"""

class Customer:
    def __init__(self,name,age,email):
        self.name=name
        self.age=str(age)
        self.email=email
    def __str__(self):
        return self.name+" "+self.email+" "+self.age
    
    
customer =Customer('SRK',56,"SRK@gmail.com")
customer.__dir__()
print(customer)