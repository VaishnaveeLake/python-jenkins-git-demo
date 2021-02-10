# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 17:43:37 2021

@author: VaishnaveeLake
"""

class One:
    def sendMsg(self):
        print('send msg1 executed')
class Two(One):
    def sendMsg(self):
        super().sendMsg()       #calls parent class fun
        print('send msg2 executed')
        
two= Two()
two.sendMsg()