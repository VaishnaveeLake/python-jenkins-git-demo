# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:09:36 2021

@author: VaishnaveeLake
"""
import re       #re is regulae exp

name="Python is a lang for ds"

pattern = r"P....n"
print(re.findall(pattern,name))

name2="AAmir 124453, aditi 00567,vaishi 789"
pattern2= r"\d+"    #for searching number
pattern3= r"\d{4,8}"    #min 4,max8 nums should be there
print(re.findall(pattern2,name2))
print(re.findall(pattern3,name2))       #return type of findall is list

pattern4= "Python is a lang for ds !and I like Python"
#print(re.fullmatch(pattern4,name))

pattern5= r"Python"
# print(re.search(pattern5,pattern4).span()) 
# print(re.search(pattern5,pattern4).group()) 
# print(re.search(pattern5,pattern4).start())

patt= r"h"
print(re.split(patt,pattern4))

patt1= r"!"
print(re.sub(patt1, replace, pattern4)
