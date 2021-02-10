# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 09:44:25 2021

@author: VaishnaveeLake
"""

filestream= open('data.txt','w')    #open writable file mode

str= input("Enter the data can be stored in the text")
filestream.write(str)

filestream.close()
