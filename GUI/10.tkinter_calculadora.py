#!/usr/bin/env python3


import tkinter as tk
from tkinter import messagebox


class Calculadora:
  def __init__(self,root):
    self.root=root
    self.display= tk.Entry(root,width=15, font=("Arial", 23), bd=10, insertwidth=1, bg="white", fg="black", justify="right") 
    # Creamos el texto con Entry.Width(Ancho), font(Cambiamos la fuente indicandole más tamaño para que el recuadro del texto sea más grande),
    # bd(Tamaño del borde), insertwidth(tamaño del cursor), bg(color del fondo), fg(color de las letras), justify(posición del texto)
    self.display.grid(row=0, column=0, columnspan=4, pady=25) # Con grid añadimos el texto Entry, seleccionando la posicion y valores como columnspan(ocupa 4 columnas)
    self.root.geometry("280x500") # Tamaño del programa
    self.root.title("Calculadora") # Título
    self.root.resizable(False, False) # Bloquear la ventana
    self.op_verification=False # Creamos una variable chivato para saber si hemos pulsado un signo de operación
    self.current="" # Variable para guardar el número antes de la operación
    self.op="" # Variable para guardar la operación que hemos indicado
    self.total=0 # Variable para guardar en float el primer número antes de la operación


    row=1 # Creamos la variable row indicandole que empieza por la fila 1  (Estas variables van a ser utilizadas en el bucle más adelante)
    col=0 # Creamos la variable col indicandole que empieza por la columna 0

    buttons = [ # Creamos una lista con los botones que va a tener la calculadora para despues poder iterar por cada elemento de la lista
      "7","8","9","/",
      "4","5","6","*",
      "1","2","3","-",
      "C","0",".","+",
      "="
    ]

    for button in buttons: # Creamos un bucle para crear la posicion de los botones del programa
      self.build_button(button, row,col) # Llamamos a la función build_button pasandole los valores button,row y col
      col+=1 # Incrementa 1 la variable col
      if col > 3: # Si col vale más de 3
        col=0 # Iguala la variable col a 0
        row+=1 # Incrementa 1 la variable row

    self.root.bind("<Key>", self.key_press) # De esta forma al pulsar el teclado llama a la función key_press

  def key_press(self,event):
    key= event.char # Con event.char guardamos lo que escribimos en el teclado

    if key == "\r": # \r significa el enter
      self.calculate()
      return
    elif key == "\x08": # \x08 significa delete
      self.clear_display()
      return
    elif key == "\x1b": # \x1b significa escape
      self.root.quit()
      return
    if key in "0123456789/*+--.": # Si lo que escribamos en el teclado esta dentro de esos caracteres
      self.click(key) # Pasamos el digito a la función click

  def clear_display(self):
    self.display.delete(0,tk.END) # Borramos el texto
    self.op_verification = False # Volvemos a poner la variable op_verification en False
    self.current="" # Volvemos a poner la variable current en vacío
    self.op="" # Volvemos a poner la variable op en vacío

  def calculate(self):
    if self.current and self.op: # Si existen números y operaciones recibidas
      if self.op =="/": # Si la operación es /
        try:
          self.total=self.total/float(self.current)
        except ZeroDivisionError: # En caso de que se divida entre 0
          self.clear_display()
          messagebox.showinfo("Error","No se ha podido realizar la operación")
      if self.op =="*": # Si la operación es *
        self.total=self.total*float(self.current)
      if self.op =="+": # Si la operación es +
        self.total=self.total+float(self.current)
      if self.op =="-": # Si la operación es -
        self.total=self.total-float(self.current)

    self.display.delete(0,tk.END) # Borramos el texto
    self.display.insert("end", round(self.total,3)) # Insertamos el total de la operación redondeando a 3

  def click(self,button):
    if self.op_verification: # Si la variable chivato op_verification esta en True
      self.op_verification=False

    self.display.insert("end",button) # Insertamos en el texto el número indicado, tendremos que colocarlo al final ya que el texto empieza por la derecha

    if button in "0123456789" or button==".": # Si el botón es un digito 
      self.current+=button # Incrementa el número indicado en la variable current. De esta forma tendremos el primer número para operar
    else: # Si es una operación
      if self.current: # Si hay contenido en la variable current, el objetivo es no poder poner una operación sin antes poner números
        if not self.op: # Si no hay contenido en la variable op
          self.total=float(self.current) # Almacenamos en la variable total el número antes de indicar una operación
      self.current="" # Volvemos a poner la variable current a 0

      self.op=button # Almacenamos en op la operación indicada
      self.op_verification=True # Ponemos la variable chivato op_verification en True

  def build_button(self,button,row,col): # Creamos la función build_button pasandole las variables button,row y col
    if button=="C":
      b = tk.Button(self.root,text=button, width=2, height=2,font=("Arial",20), bg="orange", fg="black", command=lambda: self.clear_display())
      # Creamos el botón text(Nombre del botón sacado de cada iteración de la lista buttons), width(anchura del botón), height(altura del botón), 
      #font(Cambiamos la fuente indicandole más tamaó para que el número se vea mas grande), bg(color del fondo), fg(color de los números)
    elif button=="=":
      b = tk.Button(self.root,text=button, width=2, height=2,font=("Arial",20), bg="orange", fg="black", command=lambda: self.calculate())
    else:                                                  # Al pasarle a la función click() un parámetro, esta se ejecuta sola, para evitarlo usamos funciones lambda
      b = tk.Button(self.root,text=button, width=2, height=2,font=("Arial",20), bg="orange", fg="black", command=lambda: self.click(button))  
    b.grid(row=row, column=col) # Con grid añadimos el botón, seleccionando la posición creada a base del bucle anterior


root = tk.Tk()
my_gui = Calculadora(root) # Creamos el objeto my_gui
root.mainloop()
