#!/usr/bin/env python3


import tkinter as tk

root=tk.Tk()
root.geometry('500x500')
root.title("Método text")


text_widget= tk.Text(root) # Con text podemos escribir textos más largos con saltos de línea
text_widget.pack(pady=10,padx=100, fill=tk.X) # Padding del eje y


def get_data(): # Creamos la función get_data
  data=text_widget.get("1.0",tk.END) # Indicamos que almacene desde el primer caracter de la línea 1 hasta el final
  print(f"\n[+] Datos introducidos por el usuario: {data}")

button=tk.Button(root, text='Recoger datos de entrada', command=get_data)
button.pack(padx=15,fill=tk.X)


root.mainloop()
