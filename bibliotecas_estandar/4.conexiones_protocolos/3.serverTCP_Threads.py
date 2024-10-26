#!/usr/bin/env python3

import socket
import threading
import pdb # Debugging


class ClientThread(threading.Thread): # Creamos una clase nueva, heredando la clase Thread del módulo importado threading

  def __init__(self,client_sock,client_addr):

    super().__init__() # De esta forma indicamos el contenido del anterior constructor al nuestro
    self.client_sock = client_sock
    self.client_addr = client_addr

    print(f"\n[+] Nuevo cliente conectado: {client_addr}")


  def run(self): # Sobreescribimos la función run de la clase Thread


    with self.client_sock: # De esta forma cerramos automáticamente el socket del cliente
      message = '' # Creamos una variable vacía para usarla en el bucle
      while True:

        data = self.client_sock.recv(1024) # Almacenamos el mensaje del cliente en la variable data, cada iteración se almacenará el mensaje en data
        message = data.decode() # Almacenamos la variable data en texto claro en la variable message
        #pdb.set_trace() # Breakpoint | Así podemos ver donde esta el error del código

        if message.strip() == 'bye': # Al descodificar el mensaje del cliente aparece con saltos de línea, para que la 
          break                      #condición detecte que el cliente escribe la palabra bye usamos strip()

        print(f"\n[+] Mensaje enviado por el cliente: {message.strip()}")
        self.client_sock.send(data) # Le mandamos el mismo mensaje recibido por el cliente

      print(f"\n[!] Cliente {self.client_addr} desconectado")

HOST= 'localhost'
PORT= 1234

"""
La función ‘setsockopt‘ en la programación de redes juega un papel crucial al permitir a los desarrolladores ajustar y controlar varios aspectos de los sockets.
Los sockets son fundamentales en la comunicación de red, proporcionando un punto final para el envío y recepción de datos en una red.
"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # De esta forma se cerrará automáticamente el socket del servidor

  s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR ,1) # TIME_WAIT | De esta forma podemos reutilizar la conexión cuando esta en estado TIME_WAIT

  s.bind((HOST,PORT)) # Nos ponemos en escucha

  print(f"\n[+] En espera de conexiones entrantes...")

  while True:

    s.listen() # De esta forma python elige las conexiones que pueden haber en cola
    client_sock,client_addr = s.accept() # Creamos el socket del cliente
    new_thread = ClientThread(client_sock,client_addr) # Creamos un objeto donde le pasamos el socket del cliente y su dirección
    new_thread.start() # Aquí estamos llamando a la función run
