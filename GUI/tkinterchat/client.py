#!/usr/bin/env python3

import threading
import socket
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import ssl


def send_message(client_socket,username,text_widget,entry_widget): # Creamos la función donde creamos la lógica al pulsar enter en el widget donde escribimos

  message= entry_widget.get() # Guardamos el mensaje en una variable
  client_socket.sendall(f"{username} > {message}".encode()) # Mandamos el mensaje al servidor, indicando el usuario y el mensaje

  entry_widget.delete(0,END) # Borramos el mensaje del widget donde escribimos
  text_widget.configure(state='normal') # Cambiamos el estado del widget del chat a normal para poder insertar el mensaje
  text_widget.insert(END,f"{username} > {message}\n") # Insertamos el mensaje al widget del chat
  text_widget.configure(state='disabled') # Cambiamos el estado del widget del chat a disabled para que no se puedan insertar mensajes

def recieve_message(client_socket,text_widget):
  while True:
    try:
      message = client_socket.recv(1024).decode() # Voy a estar intentando recibir constantemente mensajes del servidor

      if not message:
        break

      text_widget.configure(state='normal') # Cambiamos el estado del widget del chat a normal para poder insertar el mensaje
      text_widget.insert(END, message) # Insertamos el mensaje al widget del chat
      text_widget.configure(state='disabled') # Cambiamos el estado del widget del chat a disabled para que no se puedan insertar mensajes

    except:
      break

def list_users_requests(client_socket): # Función que se activa al pulsar el botón listar usuarios
  client_socket.sendall("!usuarios".encode()) # Mandamos al servidor el mensaje !usuarios actuando como un chivato


def exit_requests(client_socket,username,window): # Creamos la función donde creamos la lógica para el abandono del usuario
  client_socket.sendall(f"\n[!] El usuario {username} ha abandonado el chat\n\n".encode()) # Mandamos al servidor el mensaje
  client_socket.close() # Cerramos el socket del cliente

  window.quit() # Cerramos la ventana principal
  window.destroy() # Destuimos la ventana principal para asegurarnos que se cierra correctamente el programa

def client_program(): # Creamos la función donde creamos la lógica del programa

  host='localhost'
  port=12345

  client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creamos el socket del cliente
  client_socket=ssl.wrap_socket(client_socket) # Le indicamos que queremos tener una comunicación cifrada
  client_socket.connect((host,port)) # Nos conectamos al servidor

  username = input(f"\n[+] Introduce tu usuario: ") # Preguntamos al cliente por su usuario
  client_socket.sendall(username.encode()) # Mandamos el usuario al servidor

 # GUI
  window = Tk() # Creamos la ventana principal
  window.title("Chat") # Le ponemos un título


  text_widget=ScrolledText(window, state='disabled') # Creamos el widget donde apareceran todos los mensajes de los usuarios. State para bloquear la entrada de texto
  text_widget.pack(padx=5,pady=5) # Añadimos el widget a la ventana principal


  frame_widget= Frame(window) # Creamos un frame para organizar los botones y el texto de abajo, creando una especie de plantilla
  frame_widget.pack(padx=5,pady=2,fill=BOTH, expand=1)


  entry_widget= Entry(frame_widget) # Creamos el widget donde escribiremos
  entry_widget.bind("<Return>", lambda _: send_message(client_socket,username,text_widget,entry_widget)) # Cuando presione el enter ejecuta la función send_message
  entry_widget.pack(side=LEFT, fill=X, expand=1)


  button_widget= Button(frame_widget, text="Enviar", command=lambda: send_message(client_socket,username,text_widget,entry_widget)) # Cuando presione el botón ejecuta la función send_message
  button_widget.pack(side=RIGHT, padx=5)


  users_widget=Button(window,text="Listar usuarios", command=lambda: list_users_requests(client_socket)) # Cuando presione el botón ejecuta la función list_users_requests
  users_widget.pack(padx=5,pady=5)


  exit_widget=Button(window,text="Salir", command=lambda: exit_requests(client_socket,username,window)) # Cuendo presione el botón ejecuta la función exit_requestss
  exit_widget.pack()

  thread = threading.Thread(target=recieve_message, args=(client_socket, text_widget)) # Creamos un hilo para gestionar los mensajes que recibamos del servidor
  thread.daemon= True # De esta forma no quedan hilos abiertos dejando el programa colgado
  thread.start() # Iniciamos el hilo


  window.mainloop()
  client_socket.close()



if __name__ == '__main__':
  client_program()
