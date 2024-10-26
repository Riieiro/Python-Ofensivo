#!/usr/bin/env python3

import tkinter as tk

def accion_de_boton():
  print("Tonto")


root= tk.Tk() # Ventana raiz o principal
root.title("Método pack") # Título de la aplicación


label1=tk.Label(root,text="Mi primer label", bg="red") # Crear un label con fondo rojo
label2=tk.Label(root,text="Mi segundo label", bg="green")
label3=tk.Label(root,text="Mi tercer label", bg="blue")
label1.pack(fill=tk.X) # Pintamos el label usando un fill de x para que ocupe toda la parte horizontal
label2.pack(fill=tk.X)
label3.pack(side=tk.LEFT,fill=tk.Y) # Pintamos el label usando un fill de y para que ocupe toda la parte vertical y side para que aparezca en la izquierda


button=tk.Button(root,text="Pulsa aquí", command=accion_de_boton) # Crear un botón
button.pack() # Mostrar el boton en pantalla




root.mainloop() # Ejecutar y manejar todos los eventos de dentro de la aplicación

