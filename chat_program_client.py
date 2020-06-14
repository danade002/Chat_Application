#Chat Program Appliccation using Python by Ademeso Daniel

#This is the client side

import socket
import sys
import time

##imports end here##

##initialization of program start here##
soc = socket.socket()
host = input("Please enter the hostname of the server: ")
port = 8585
soc.connect((host,port))

while 1:
    print("Connected to chat server")
    incoming_message = soc.recv(1024)
    incoming_message = incoming_message.decode()
    print("Server: ", incoming_message)
    print("")
    message = input(str("Client: "))
    message = message.encode()
    soc.send(message)
    print ("Message sent")
    print("")
