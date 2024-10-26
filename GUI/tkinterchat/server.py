#!/usr/bin/env python3

import socket
import threading
import ssl


def client_thread(client_socket,clients,usernames): # Creamos la función donde creamos la lógica de los hilos

  username= client_socket.recv(1024).decode() # Guardamos en una variable el mensaje del cliente
  usernames[client_socket] = username # Almacenamos en el diccionario de usuarios el mensaje recibido

  print(f"\n[+] El usuario {username} se ha conectado")

  for client in clients: # Iteramos por cada cliente
    if client is not client_socket: # Si ese cliente no soy yo
      client.sendall(f"\n[+] El usuario {username} ha entrado al chat\n\n".encode()) # Mandamos el mensaje al socket del cliente

  while True: # Creamos un bucle para recibir consantemente los posibles mensajes de los clientes
    try:
      message = client_socket.recv(1024).decode() # Almacenamos en una variable el mensaje del cliente

      if not message: # Si la variable mensaje no tiene contenido
        break

      if message == "!usuarios": # Si el mensaje recibido es !usuarios
        client_socket.sendall(f"\n[+] Listado de usuarios disponibles: {', '.join(usernames.values())}\n\n".encode()) # Mostramos los valores del diccionario usernames
        continue # Salta la continuación del bucle

      for client in clients: # Iteramos por cada socket de la lista clientes
        if client is not client_socket: # Si el socket de la lista no es el socket actual del cliente. De esta forma no nos mandamos el mensaje a nosotros mismos
          client.sendall(f"{message}\n".encode()) # Mandamos al socket del cliente el mensaje
    except:
      break

  client_socket.close() # Cerramos el socket del cliente
  clients.remove(client_socket) # Eliminamos nuestro socket del cliente de la lista clients
  del usernames[client_socket] # Borramos tanto la key como el value de nuestro socket del cliente en el diccionario username, borrando asi el socket y el usuario


def server_program(): # Creamos la función donde creamos la lógica de las conexiones

  host= 'localhost'
  port= 12345


  server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Creamos el socket del servidor
  server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) # Modificamos el socket para poder reutilizarlo
  server_socket.bind((host,port)) # Nos ponemos en escucha
  server_socket = ssl.wrap_socket(server_socket,keyfile="server-key.key", certfile="server-cert.pem", server_side=True) # Le indicamos que queremos una comunicación cifrada
  server_socket.listen() # Aceptamos conexiones

  print(f"\n[+] El servidor está en escucha de conexiones entrantes...")


  clients = [] # Creamos una lista vacía para almacenar el número de clientes
  usernames = {} # Creamos un diccionario vacío para almacenar el nombre de los usuarios


  while True:

    client_socket,address= server_socket.accept() # Creamos el socket del cliente
    clients.append(client_socket) # Añadimos el socket del cliente a la lista clients

    print(f"\n[+] Se ha conectado un nuevo cliente: {address}")

    thread = threading.Thread(target=client_thread, args=(client_socket,clients,usernames)) # Creamos un hilo para gestionar las múltiples conexiones
    thread.daemon= True # Si ponemos esto todos los hilos se cerrarían, sino lo ponemos corremos el riesgo de que el programa se quede colgado
    thread.start() # Iniciamos el hilo

  server_socket.close() # Cerramos el socket del servidor

if __name__== '__main__':
  server_program()
