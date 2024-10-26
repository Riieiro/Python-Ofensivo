#!/usr/bin/env python3 

import socket

client_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #Con esta variable creamos un socket que acepta conexiones entrantes
                                                                 # La primera parte indicamos que aceptamos IPV4| La segunda parte indicamos que aceptamos conexiones TCP

server_address=('localhost', 1234) # Indicamos la ip y el puerto del servidor
client_socket.connect(server_address) # Nos conectamos al servidor


try:
  message=b"Este es un mensaje de prueba que estoy enviando al servidor"
  client_socket.sendall(message) # Mandamos el mensaje en formato bytes
  data=client_socket.recv(1024) # Almacenamos la información que nos proporcione el cliente limitandolo a 1024 bytes (El contenido de esta data viene en bytes)

  print(f"\n[+] El servidor nos ha respondido con este mensaje: {data.decode()}") # Para leer el mensaje tenemos que descodificarlo
finally:
  client_socket.close() # Cerramos el socket del cliente

