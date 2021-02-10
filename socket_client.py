# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 17:36:14 2021

@author: VaishnaveeLake
"""

import socket

HOST= '127.0.0.1'    

PORT = 4001
client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((HOST,PORT))
data= client.recv(1024)

print(data.decode('utf-8'))
