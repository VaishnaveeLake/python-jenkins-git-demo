# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:07:04 2021

@author: VaishnaveeLake
"""
from functools import reduce
def movie_starts_with(name):
    return name[0] == "A"

movies =["Andhadhun","Aashiqi","Andazapnapna","Annabla","arjunreddy"]

#movieswith =map(movie_starts_with,movies);
#print(list(movieswith))

resultmap =list(map(lambda s: s[0]=='A',movies))
print(resultmap)

print(list(filter(movie_starts_with,movies)))

data=reduce(lambda  x,y: x+y,map(lambda x:x+x,filter(lambda x: (x>=3),(1,2,3,4,5))))#reduce will combine all into one
print(data)