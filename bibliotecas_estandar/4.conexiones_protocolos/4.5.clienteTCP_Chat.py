#!/usr/bin/env python3

import socket


def start_chat_client(): # Creamos la función start_chat_client

  host= 'localhost'
  port= 1234

  with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as c: # De esta forma el socket del cliente se cerrará automáticamente

    c.connect((host,port)) # Nos conectamos al servidor

    while True:

      client_message=input(f"\n[+] Mensaje para enviar al servidor: ") # Almacenamos en una variable el mensaje que queramos enviar al servidor
      c.send(client_message.encode()) # Mandamos el mensaje al servidor

      if client_message=='bye': # Si escribimos bye el bucle se detendrá y por consecuente se cerrará la conexión del socket del cliente
        break

      server_message= c.recv(1024).decode().strip() # Almacenamos el mensaje descodificado y con strip para evitar saltos de línea
      print(f"\n[+] Mensaje del servidor: {server_message}")


start_chat_client()
