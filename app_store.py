# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:11:48 2021

@author: VaishnaveeLake
"""
import csv
set={}
with open('data_stock.csv','r') as data:
    pointer=csv.reader(data)
    for i in pointer:
       set.append(i)
# print("Welcome to grocery store..... We have following items")
# for i in range(1,len(list)-1):
#     print(str(list[i][0])+" "+str(list[i][1])+" "+str(list[i][2]))