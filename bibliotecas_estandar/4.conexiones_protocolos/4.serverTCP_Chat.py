#!/usr/bin/env python3

import socket


def start_chat_server(): # Creamos la función start_chat_server

  host='localhost'
  port=1234

  server_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Creamos el socket del servidor
  server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) # Cambiamos un componente del socket para reutilizar el socket cuando este en TIME_WAIT
  server_socket.bind((host,port)) # Nos ponemos en escucha
  server_socket.listen(1) # Limitamos la conexión a 1


  print(f"\n[+] Servidor listo para aceptar una conexión...")
  connection,client_addr= server_socket.accept() # Creamos el socket del cliente
  print(f"\n[+] Se ha conectado el cliente {client_addr}")

  while True:
    client_message=connection.recv(1024).decode().strip() # Guardamos el mensaje del cliente descodificandolo y aplicando strip para evitar saltos de línea
    print(f"\n[+] Mensaje del cliente: {client_message}")

    if client_message=='bye': # Cuando el cliente escriba bye el bucle se detendrá y por consecuente la conexión
      break

    server_message = input(f"\n[+] Mensaje para enviar al cliente: ") # Guardamos en una variable el mensaje que queramos enviar al cliente
    connection.send(server_message.encode()) # Mandamos el mensaje del servidor al cliente
  connection.close() # Cerramos la conexión del socket del cliente

start_chat_server()
