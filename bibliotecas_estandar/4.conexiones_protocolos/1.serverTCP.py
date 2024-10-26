#!/usr/bin/env python3
"""
Conexiones cliente-servidor: Con ‘socket‘, puedes crear aplicaciones cliente-servidor, donde un programa actúa como servidor esperando conexiones entrantes 
y otro actúa como cliente para conectarse al servidor.
"""


import socket

server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Con esta variable creamos un socket que acepta conexiones entrantes
                                                                 # La primera parte indicamos que aceptamos IPV4| La segunda parte indicamos que aceptamos conexiones TCP

server_address= ('localhost',1234) # Indicamos la ip y el puerto del servidor
server_socket.bind(server_address) # Nos ponemos en escucha
server_socket.listen(1) # Limitar el límite de conexiones

while True:

  client_socket,client_address= server_socket.accept() # Aceptamos la conexión | Para que esta conexión funcione necesitamos 2 socket. 1 socket del cliente 
                                                       #y otro que recibe la ip y el puerto que abre (Este puerto es aleatorio y cambia cada vez que hagamos la conexión)

  data= client_socket.recv(1024) # Almacenamos la información que nos proporcione el cliente limitandolo a 1024 bytes (El contenido de esta data viene en bytes)
  print(f"\n[+] Mensaje recibido del cliente: {data.decode()}") # Para leer el mensaje tenemos que descodificarlo
  print(f"[+] Información del cliente que se ha comunicado con nosotros: {client_address}")

  client_socket.sendall(f"Un saludo crack\n".encode()) # De esta forma mandamos un mensaje al cliente en formato bytes
  client_socket.close() # Cerramos el socket de la conexión con el cliente

