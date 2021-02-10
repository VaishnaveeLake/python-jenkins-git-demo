# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 17:26:21 2021

@author: VaishnaveeLake
"""

import socket

HOST= '127.0.0.1'    

PORT = 4001
 
#AF_INET means connecting to internet and SOCK_STREAM means takin input  output
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((HOST,PORT))
server.listen(2)

while True:
    #here server n client handshakig and is called destructuring
    clientsocket, address=server.accept()
    print(f"connected to client on {address}")
    clientsocket.send("This is a test msg fro server".encode("UTF-8"))

server.shutdown()
server.close()
    