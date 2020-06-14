#Chat Program Appliccation using Python by Ademeso Daniel

#This is the server side

import socket
import sys
import time

##imports end here##

##initialization of program start here##

soc = socket.socket()
host = socket.gethostname()
print ("Server will be running on the host: ", host)
port = 8585             #My port 8080 is in use by Jenkins | Any unused port can be used here
soc.bind((host,port))
print("")
print("Server done binding the host and port successfully")
print("")
print("Server is waiting for incoming connection")
soc.listen(1)
conn,addr = soc.accept()
print (addr, "Connected to the server and now online")
print("")
while 1:
    message = input(str("Server: "))
    message = message.encode()
    conn.send(message)
    print ("Message sent")
    print("")
    print("Connected to chat server")
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print("Client: ", incoming_message)
    print("")


    



