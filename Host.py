import socket
import sys
import time

s=socket.socket()
host=socket.gethostname()
print("Host name : ",host)
port=1234
s.bind((host,port))
print("Waiting !")
s.listen(1)
connection,address=s.accept()
print(address," has connected !")
while 1:
    message=input(str("You : "))
    message=message.encode()
    connection.send(message)
    incoming_msg=connection.recv(1024)
    incoming_msg=incoming_msg.decode()
    print("Host : ",incoming_msg)
