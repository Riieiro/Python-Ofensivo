#!/usr/bin/env python3

import tkinter as tk

def accion_de_boton():
  print("Tonto")


root= tk.Tk() # Ventana raiz o principal
root.title("Mi primera aplicación") # Título de la aplicación


label1=tk.Label(root,text="Mi primer label", bg="red") # Crear un label con fondo rojo
label2=tk.Label(root,text="Mi segundo label", bg="green")
label3=tk.Label(root,text="Mi tercer label", bg="blue")


label1.grid(row=0, column=0) # Con grid podemos indicar la fila y la columna donde queramos que aparezca el label
label2.grid(row=0,column=1)
label3.grid(row=1,column=0,columnspan=2) # Con columnspan indicamos que ocupe dos columnas


root.mainloop() # Ejecutar y manejar todos los eventos de dentro de la aplicación

