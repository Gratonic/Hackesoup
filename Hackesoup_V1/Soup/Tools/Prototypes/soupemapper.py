"""
# :: Author Information and Program Details :: #

File Name: soupemapper.py
Author(s): Gratonic (https://github.com/Gratonic)
Written In: Python 3.10.12
Dependencie(s): None (yet)
Last Modified: April 7th, 2025

# :: Description :: #

This is the prototype for the Port Scanner / Network Mapper tool.
"""

# :: Imports :: #
import socket

target = "192.168.1.1"
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect_ex((target, port))
message = "Hello Mr Router".encode()
s.send(message)
s.recv(1046)
s.close()