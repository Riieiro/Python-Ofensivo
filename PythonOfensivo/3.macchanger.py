#!/usr/bin/env python3

import argparse
import re
from termcolor import colored
import subprocess
import sys
import signal
import socket


def def_handler(sig,frame): # Creamos una función para gestionar la lógica al pulsar Ctrl+C
  print(colored(f"\n[!] Saliendo del programa...\n","red"))
  sys.exit(1)

signal.signal(signal.SIGINT, def_handler) # Capturamos el Ctrl+C


def get_arguments(): # Creamos una función para gestionar la lógica de los posibles parámetros

  parser= argparse.ArgumentParser(description="Herramienta para cambiar la dirección MAC de una interfaz de red")
  parser.add_argument("-i","--interface", dest="interface", help="Nombre de la interfaz de red", required=True) # Parámetro requerido en los dos casos
  parser.add_argument("-m","--mac",dest="mac_address", help="Nueva dirección MAC para la interfaz de red")
  parser.add_argument("-l","--list",dest="list_mac",action="store_true",help="Listar la dirección MAC actual") # Parámetro sin argumentos


  return parser.parse_args() # Retornamos las opciones


def is_valid_input(interface,mac_address): # Creamos una función para gestionar la lógica de la validación de los argumentos -i -m

  is_valid_interface= re.match(r'^[e][n|t][s|h]\d{1,2}$', interface) # Con expresiones regulares vemos si el argumento introducido coincide con el patrón
  is_valid_mac_address = re.match(r'^([A-Fa-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}$', mac_address) # Con expresiones regulares vemos si el argumento introducido coincide con el patrón

  return is_valid_interface and is_valid_mac_address # Esto retorna un True o un False dependiendo si los argumentos han coincidido


def check_interface(interface): # Creamos una función para gestionar la lógica de la validación de los argumentos -i

  list_interfaces=socket.if_nameindex() # Almacenamos la tupla con varias listas en el interior en una variable
  for i in list_interfaces: # Iteramos por cada lista de la tupla
    if interface in i: # Si el argumento introducido en -i coincide con una interfaz de nuestra red
      return interface # Retornamos un Booleano


def list_mac(interface): # Creamos una función para gestionar la lógica cuando indiquemos el parámetro -l

  print(colored("\n[+] Mostrando la direción MAC actual: \n", 'yellow'))
  subprocess.run(["macchanger", "-s", interface]) # De esta forma ejecutamos un comando a nivel sistema que nos muestra la dirección MAC actual

def change_mac_address(interface,mac_address): # Creamos una función para gestionar la lógica cuando indiquemos los parámetros -m -i, cambiando así la dirección MAC

  if is_valid_input(interface,mac_address) and check_interface(interface): # Si los argumento -i y -m han pasado la validación y el argumento -i es una interfaz existente de la red
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig",interface,"hw","ether", mac_address]) # De esta forma cambiamos la dirección MAC
    subprocess.run(["ifconfig", interface, "up"])

    print(colored(f"\n[+] La MAC ha sido cambiada exitosamente\n",'green'))
    print(colored(f"\n[+] Mostrando nueva dirección MAC:\n",'yellow'))
    subprocess.run(["macchanger","-s", interface])
  else:
    print(colored("\n[!] Los datos introducidos son incorrectos", 'red'))


def main():

  if subprocess.check_output(["whoami"]).decode().strip() == 'root': # Comprobamos si estamos ejecutando el script como usuario root
    args= get_arguments() # Almacenamos los argumentos de los parámetros introducidos
    if "-m" in sys.argv: # Si hemos indicado el parámetro -m significa que queremos ejecutar la función change_mac_address
      change_mac_address(args.interface,args.mac_address)
    elif "-l" in sys.argv: # Si hemos indicado el parámetro -l significa que queremos ejecutar la función list_mac
      list_mac(args.interface)
    elif len(sys.argv)== 3 : # Si la cantidad de parámetros indicados son 2, significa que hemos ejecutado mal el script
      print(colored("\n[!] Es necesario especificar el parámetro -m o -l",'red'))

  else:
    print(colored(f"\n[!] Para ejecutar este script es necesario ser root.","red"))
    sys.exit(1)



if __name__ == '__main__':

  main()
