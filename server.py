#!/usr/bin/python3

import socket
import threading

def send_msg():
  while True:
    msg = input("$ ").encode()
    s.send(msg)

def receive_msg():
  while True:
    receive = s.recv(1024)
    print(receive.decode())

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Connecting...")
while True:
  try:
    s.connect(('127.0.0.1',1111))
    break
  except ConnectionRefusedError:
    continue
print("Connected.")

t2 = threading.Thread(target=send_msg)
t2.start()
receive_msg()
