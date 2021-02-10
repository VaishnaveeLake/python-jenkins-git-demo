# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 17:14:12 2021

@author: VaishnaveeLake
"""

import re


name="Vaish.Llake@ibm.com"

pattern =r"([a-z+A-Z\._]+@[a-z]+\.[a-z]{2,5})"

print(re.findall(pattern,name))