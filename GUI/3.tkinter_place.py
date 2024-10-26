#!/usr/bin/env python3

import tkinter as tk

root=tk.Tk()
root.geometry('500x500') # Abrimos la ventana con este tamaño
root.title("Método place")


label1= tk.Label(root,text="Mi primer label", bg="red")
label2=tk.Label(root,text="Mi segundo label", bg="red")
label3=tk.Label(root,text="Mi tercer label", bg="red")


label1.place(x=20,y=20) # Indicamos los píxeles donde queramos que aparezca la label
label2.place(relx=0.8,rely=0.2) # En función al tamaño que pongas en la ventana se va ha ampliar la label
label3.place(relx=0.5,rely=0.5, anchor=tk.CENTER) # De esta forma centramos la label en la mitad


root.mainloop()
