#!/usr/bin/env python3


import tkinter as tk

root=tk.Tk()
root.geometry('500x650')
root.title("Método canvas")


canvas=tk.Canvas(root,width=250,height=250, bg="white")
canvas.pack(pady=10)


oval= canvas.create_oval(50 ,50 ,150 ,150 ,fill="red") # Creamos el circulo indicando 4 valores que hacen referencia a la posicion del canvas
rect = canvas.create_rectangle(150 ,50 ,250 ,100 ,fill="green") # Creamos el rectángulo
line=canvas.create_line(50,120,200,300, fill="blue", width=5) # Creamos una línea añadiendo más anchura


root.mainloop()
