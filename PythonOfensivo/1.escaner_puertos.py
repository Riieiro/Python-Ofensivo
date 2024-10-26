#!/usr/bin/env python3

import socket


host= input(f"\n[+] Introduce la dirección IP: ")
port= int(input(f"\n[+] Introduce el puerto a escanear: "))

def port_scanner(port): # Creamos la función donde gestionaremos la lógica de las conexiones

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(0.2) # Ponemos un límite de tiempo para comprobar si esta abierto o cerrado

  if s.connect_ex((host,port)): # Nos conectamos al host y puerto indicado, la función connect_ex te devuelve un código exitoso "0" o código erróneo "111"
    print(f"\n[+] El puerto {port} está cerrado") # Aunque el código de estado sea exitoso, en python el valor 0 corresponde a un estado booleano False
  else:
    print(f"\n[+] El puerto {port} está abierto")

  s.close()

def main():
  port_scanner(port)


if __name__ == '__main__':
  main()
