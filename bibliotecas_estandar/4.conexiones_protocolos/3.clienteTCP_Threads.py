#!/usr/bin/env python3

import socket

def start_client(): # Creamos la función start_client

  host = 'localhost'
  port= 1234

  with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as c: # De esta forma el socket del cliente se cerrará automáticamente
    c.connect((host,port)) # Nos conectamos al servidor

    while True:
      message= input("\n[+] Introduce tu mensaje: ")
      c.sendall(message.encode()) # Mandamos el mensaje al servidor

      if message == 'bye': # Si escribimos bye el bucle parará y por consecuente la conexión
        break

      data=c.recv(1024)
      print(f"\n[+] Mensaje de respuesta del servidor: {data.decode()}")


start_client()
