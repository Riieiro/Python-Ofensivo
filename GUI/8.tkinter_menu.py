#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox,filedialog

"""
[!] messagebox [!]

   -  Funciones Comunes:
        showinfo(), showwarning(), showerror(): Muestran mensajes informativos, de advertencia y de error, respectivamente.

[!] filedialog [!]

    - Funciones Clave:
        askopenfilename(): Abre un cuadro de diálogo para seleccionar un archivo para abrir.
        asksaveasfilename(): Abre un cuadro de diálogo para seleccionar la ubicación y el nombre del archivo para guardar.
        askdirectory(): Permite al usuario seleccionar un directorio
"""

root=tk.Tk()
root.geometry('500x650')
root.title("Método menu")


barra_menu=tk.Menu(root) # Barra para menúes
root.config(menu=barra_menu) # Insertamos la barra de menúes en la interfaz raiz


menu1=tk.Menu(barra_menu, tearoff=0) # Creamos el primer menú indicandole la opción tearoff para dejar las opciones fijas
barra_menu.add_cascade(label="Menú", menu=menu1) # Aplicamos el menú
menu1.add_command(label="Opción 1") # Creamos una opción del menu1
menu1.add_command(label="Opción 2")


def accion_menu(): # Creamos la función accion_menu
  messagebox.showinfo("Menú", "Eres tonto") # De esta forma desplegamos un panel informativo


def open_explorer(): # Creamos la función open_explorer
  ruta_archivo=filedialog.askopenfilename() # De esta forma abrimos el gestor de archivos y almacenamos la ruta del archivo seleccionado en una variable
  print(f"\n[+] Ruta del archivo en cuestión: {ruta_archivo}")

menu2=tk.Menu(barra_menu, tearoff=0) # Creamos el segundo menú
barra_menu.add_cascade(label="Extras", menu=menu2) # Aplicamos el menú
menu2.add_command(label="Tonto",command=accion_menu) # Creamos una opción del menu2 que al pulsarlo tenga una función
menu2.add_command(label="File", command=open_explorer) # Creamos una opción del menu2 que al pulsarlo te abra un gestor de archivos


root.mainloop()
