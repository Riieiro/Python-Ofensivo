#!/usr/bin/env python3


import tkinter as tk

root=tk.Tk()
root.geometry('500x500')
root.title("Método entry")


entry_widget= tk.Entry(root) # Con entry permitimos al usuario introducir una frase
entry_widget.pack(pady=5,padx=100, fill=tk.X) # Padding del eje y


def get_data(): # Creamos la función get_data
  data=entry_widget.get() # Almacenamos el contenido del widget en una variable
  print(f"\n[+] Datos introducidos por el usuario: {data}")

button=tk.Button(root, text='Recoger datos de entrada', command=get_data) # Botón para introducir el texto
button.pack(padx=15,fill=tk.X)


root.mainloop()
