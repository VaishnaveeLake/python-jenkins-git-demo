# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:15:10 2021

@author: VaishnaveeLake
"""

class Myiterator:
    def __init__(self,min,max):
        self.current=min
        self.max=max
    def __iter__(self):
        return self
    def __next__(self):
        if self.current>self.max:
            raise StopIteration
        else:
            self.current +=1
            return self.current-1
myItr=Myiterator(4,12)
iterator =iter(myItr)
while True:
    try:
        x=iterator.__next__()
        print(x,end=' ')
    except StopIteration:
        break