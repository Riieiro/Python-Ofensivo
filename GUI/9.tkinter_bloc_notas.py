#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog,messagebox
import os

class SimpleTextEditor:

  def __init__(self,root):
    self.root=root
    self.text_area=tk.Text(self.root) # Creamos el widget texto
    self.text_area.pack(fill=tk.BOTH, expand=1) # Aplicamos el widget texto, añadiendole el máximo tamaño en los dos ejes. En el eje y hay un límite por eso ponemos expand
    self.current_open_file='' # Para saber que archivo está abierto

  def new_file(self):
    self.text_area.delete("1.0", tk.END) # Borramos el contenido del texto
    self.current_open_file='' # Indicamos que no hay ningún archivo abierto

  def open_file(self):
    filename= filedialog.askopenfilename() # Almacenamos la ruta del archivo seleccionado en una variable

    if filename: # Si ese archivo tiene contenido
      self.text_area.delete("1.0", tk.END) # Borramos el contenido del texto
      with open(filename, 'r') as file: # Abrimos el archivo seleccionado con permiso de lectura
        self.text_area.insert("1.0",file.read()) # Insertamos en el texto el contenido de ese archivo

      self.current_open_file=filename # Indicamos que el archivo que está abierto es filename

  def save_file(self):
    if not self.current_open_file: # Si la variable current_open_file no tiene contenido
      new_file=filedialog.asksaveasfilename() # Almacenamos la ruta del archivo que indiquemos en una variable
      if new_file: # Si new_file tiene contenido
        self.current_open_file=new_file # Indicamos que hay contenido en la variable current_open
      else:
        return
    with open(self.current_open_file, 'w') as file: # Abrimos el archivo current_open_file con permisos de escritura
      file.write(self.text_area.get("1.0",tk.END)) # Almacenamos el contenido del widget texto en el archvo current_open_file

  def delete_file(self):
    filename=filedialog.askopenfilename() # Almacenamos la ruta del archivo que indiquemos en una variable
    if messagebox.askokcancel("Archivo", f"¿Estás seguro de que desas borrar el archivo {filename}?"): # La función askokcancel despliega un menú con dos opciones y devuelve un booleano
      os.remove(filename) # Borramos el archivo filename
      self.text_area.delete("1.0",tk.END) # Limpiamos el texto actual

  def quit_confirm(self):
    if messagebox.askokcancel("Salir", "¿Estás seguro de que deseas salir"): # La función askokcancel despliega un menú con dos opciones y devuelve un booleano
      self.root.destroy() # De esta forma destruimos la interfaz raiz



# GUI
root=tk.Tk()
root.title("Notas")
root.geometry('500x550')


editor = SimpleTextEditor(root) # Creamos el objeto editor pasandole el valor root haciendo referencia a la interfaz raiz


menu_bar = tk.Menu(root)
menu_options = tk.Menu(menu_bar, tearoff=0)


menu_options.add_command(label="Nuevo", command=editor.new_file)
menu_options.add_command(label="Abrir", command=editor.open_file)
menu_options.add_command(label="Guardar", command=editor.save_file)
menu_options.add_command(label="Borrar", command=editor.delete_file)
menu_options.add_command(label="Salir", command=editor.quit_confirm)


root.config(menu=menu_bar)
menu_bar.add_cascade(label="Archivo", menu=menu_options)


root.mainloop()
