# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 15:37:54 2021

@author: VaishnaveeLake
"""
import csv
from typing import List, Dict
l=[]
sets=set()
table: List[Dict[int,str]]=[]



with open('data_stock.csv','r') as a:
    data=csv.reader(a)
    for item in data:
        l.append(item)
for i in range(1,len(l)-1):
    print(l[i][1])
        

with open('data_stock.csv','r') as a:
    data=csv.DictReader(a)
    
    for i in data:
        sets.add((i)['name']);
    
       
for i in sets:
    print(i)
    


       



