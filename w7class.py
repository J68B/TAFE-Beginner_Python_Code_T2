import socket
import sys

#create a TCP/IP socket
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# create a UDP/IP socket
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#create a servername/port pair
server_address = ('www.google.com',80)

# Open a TCP/IP connection
sock1.connect(server_address)

# send or recieve data

# close the connection
sock1.close()