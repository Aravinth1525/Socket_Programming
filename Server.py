import socket
import sys
import time

s=socket.socket()
host=input(str("Enter Host Name : "))
port=1234
try:
    s.connect((host,port))
    print("Connected to Server !")
except:
    print("Connection Failed !")
while 1:
    incoming_msg = s.recv(1024)
    incoming_msg = incoming_msg.decode()
    print("Server : ",incoming_msg)

    message=input(str("You : "))
    message=message.encode()
    s.send(message)

