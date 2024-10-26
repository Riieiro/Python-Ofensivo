#!/usr/bin/env python3

import socket

def start_client():

  host='localhost'
  port=1234

  with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as c:
    c.connect((host,port))
    c.sendall(b"Hola, servidor!")
    data= c.recv(1024)

  print(f"\n[+] Mensaje recibido del servidor {data.decode()}")


start_client()
