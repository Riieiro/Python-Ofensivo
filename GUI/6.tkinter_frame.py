#!/usr/bin/env python3


import tkinter as tk

root=tk.Tk()
root.geometry('500x650')
root.title("Método frame")


frame = tk.Frame(root,bg="black",bd=5) # Creamos un contenedor y le ponemos 5px de marco
frame.place(relx=0.5,rely=0.2, anchor=tk.CENTER) # 


label1=tk.Label(frame,text="Mi primer label", bg="green") # Indicamos que queremos meter el label en el frame
label2=tk.Label(frame,text="Mi segundo label", bg="red")
label1.pack(fill=tk.X)
label2.pack(fill=tk.X)



root.mainloop()
