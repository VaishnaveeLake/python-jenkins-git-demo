# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:40:49 2021

@author: VaishnaveeLake
Set is unorderd uindexed collections of items

intersection()
union()
"""

set1={3,4,6}
set2={8,9,7}
set1.add(1)     #it prepend at first 1,3,4,6

print(set1)
# it clears set values set1.clear()    

set1.remove(3)
set1.discard(7) #remove n discard are same
set2.pop()
print(set1) 
print(set2)
