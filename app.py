# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:59:44 2021

@author: VaishnaveeLake
"""

name=input("Enter your name")
age=int(input("Enter your age"))
val={"BJP":0,"CONGRESS":0,"NCP":0,"SP":0 }
    

if age<18:
     print("You are not eligible")
    
else:
    
    party=str(input("which party u wan to join"))     
    if party in val:
        print("Cogratulations your membership accepted")
        val[party]=val[party]+1
        print(val)
    else:
        input("Not a party")
    
    
        
    
    

