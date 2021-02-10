# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 11:39:43 2021

@author: VaishnaveeLake
"""

import csv
total=0
brand=0

def func():
    class Error(Exception):
        pass
    class Notavailable(Error):
        pass
    class StockUnavailable(Error):
        pass
    global total
    global brand
    m=1
    b=0
    
    var=0
    try:
        product=str(input("Enter the product u want:"))
        print("Recommanded brands and prices are:")
        for a in range(1,len(l)-2):
            if product==str(l[a][1]):
                print(l[a][2]+" "+l[a][3])
                var=1
                    
        
        if var==1:
            print("Select which brand to want:")
            for i in range(0,len(l)-2 ):
                if (product==str(l[i][1]) and brand ==str(l[a][2])) :
                    m+=1
           
        else:
            raise Notavailable
            m=0
          
    
        if m!=0:
              brand=input()
              quantity=int(input("Enter quantity:"))
              for i in range(0,len(l)-2):
                  if (brand ==str(l[i][2]) or str(product)==str(l[a][0])):
                      t=i
                      if quantity <= int(l[i][4]):
                          print("Item:"+l[i][1]+"\t"+"  Brand:"+brand+"  Quantity:"+str(quantity)+"  Price:"+str(l[i][3]))  
                          b=int(l[t][3])*int(quantity);
                          print("Product mrp:",b)
                          total = total + b
                          print("total mrp:",total)
                          
                      else:
                              raise StockUnavailable
                           
    except Notavailable:
        print("Product u entered not available ")
    except StockUnavailable:
        print("Product is out of stock")
          
    s=str(input("want to continue shopping(yes/no):"))
    if(s=='yes'):
        func() 
    else:
        print("Your total bill is:",total)
    
 
           
sets=set()
l=[]
with open('data_stock.csv','r') as a:
    data=csv.reader(a)
    for item in data:
        l.append(item)

with open('data_stock.csv','r') as a:
    data=csv.DictReader(a)
    
    for i in data:
        sets.add((i)['name']);
           
    for i in sets:
        print(i)  
func()
  
