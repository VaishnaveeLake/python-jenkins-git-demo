# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:20:48 2021

@author: VaishnaveeLake
"""



user={'name':'some name'}
try:
    name=user['name1']
except Exception as e:      #in java it wont work if generic block is shadowing the other one
    print(type(e))          #but python will accept this shows generic block if its first
    print("generic",e)
except KeyError as e:
    print(type(e))
    print("specific",e)
finally:
    print("user[name1]")
    
print('after key error')
