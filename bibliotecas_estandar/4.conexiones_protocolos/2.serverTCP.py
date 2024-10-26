#!/usr/bin/env python3

import socket

def start_server(): # Creamos la función start_server

  host= 'localhost' # Indicamos el host del servidor
  port=1234 # Indicamos el puerto del servidor

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # De esta manera no hace falta hacer un bucle infinito, ya que usando with cierra automáticamente el socket del servidor
    s.bind((host,port)) # Nos ponemos en escucha | Es necesario pasarle a esta función una tupla, por eso hay dos paréntesis
    print(f"\n[+] Servidor en escucha en {host}:{port}")
    s.listen(1) # Limitamos la conexión a 1
    conn,addr= s.accept() # Aceptamos la conexión | Para que esta conexión funcione necesitamos 2 socket. 1 socket del cliente 
                                                   #y otro que recibe la ip y el puerto que abre (Este puerto es aleatorio y cambia cada vez que hagamos la conexión)

    with conn: # De esta manera cerramos automáticamente el socket del cliente
      print(f"\n[+] Se ha conectado un nuevo cliente: {addr}")
      while True: # Creamos un bucle infinito para no perder la conexión cuando mandemos un mensaje
        data= conn.recv(1024) # Almacenamos en data los mensajes del cliente
        if not data: # Si data no tiene contenido, es decir pulsamos control c o similar
          break # Para el bucle y por tanto la conexión
        conn.sendall(data) # Mandamos al cliente la data

start_server()
