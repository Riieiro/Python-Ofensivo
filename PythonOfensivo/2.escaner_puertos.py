#!/usr/bin/env python3

import socket
import argparse
import signal
import sys
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored


open_sockets=[] # Creamos una lista para almacenar todos los sockets existentes

def def_handler(sig, frame): # Creamos una función donde gestionaremos la lógica al pulsar Ctrl+C

  print(colored(f"\n[!] Saliendo del programa...",'red'))

  for socket in open_sockets: # Iteramos por cada socket abierto
    socket.close() # Cerramos todos los sockets

  sys.exit(1) # Salimos del programa con un código de estado 1

signal.signal(signal.SIGINT, def_handler) # Ctrl+C | Capturamos el Ctrl+C y llamamos a la función def_handler


def get_arguments():
  parser = argparse.ArgumentParser(description= 'Fast TCP Port Scanner')
  parser.add_argument("-t","--target",dest="target", required=True,help="Victim target to scan (Ex: -t 192.168.1.1)") # Cuando le pase -t o --target al programa lo almacena en target
  parser.add_argument("-p","--port", dest="port", required=True,help="Port range to scan (Ex: -p 1-100 | -p 21,22,80,445 | -p 80)")
  options= parser.parse_args() # Le pasamos a options las opciones que tiene el programa


  return options.target,options.port  # Le retornamos las opciones elegidas


def create_socket(): # Creamos la función donde gestionaremos la lógica de la creación del socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(1) # Ponemos un límite de tiempo para comprobar si esta abierto o cerrado

  open_sockets.append(s)

  return s

def port_scanner(port,host): # Creamos la función donde gestionaremos la lógica de las conexiones

  s = create_socket() # Creamos un socket por cada iteración llamando a la función create_socket
  try: # Probamos a conectarnos al puerto del host indicado
    s.connect((host,port))
    s.sendall(b"HEAD / HTTP/1.0\r\n\r\n") # Mandamos esta cabecera por si está abierto el puerto 80
    response = s.recv(1024) # Guardamos la respuesta en una variable
    response= response.decode(errors='ignore').split('\n')[0] 

    if response:
      print(colored(f"\n[+] El puerto {port} está abierto - {response}", 'green'))
    else:
      print(colored(f"\n[+] El puerto {port} está abierto", 'green'))
    s.close() # Cerramos el socket para que no queden sockets abiertos
  except (socket.timeout, ConnectionRefusedError):
    s.close() # Cerramos el socket para que no queden sockets abiertos


def scan_ports(ports,target): # Creamos la función donde gestionaremos la lógica del escaneo de los puertos

  with ThreadPoolExecutor(max_workers=50) as executor: # Indicamos que queremos como máximo 50 hilos
    executor.map(lambda port: port_scanner(port, target), ports) # El método map solo permite un argumento, en este caso como queremos pasar dos necesitamos una función lambda
   # map funciona como un bucle

def parse_ports(ports_str): # Creamos la función donde gestionaremos la lógica de la creación de una lista de puertos, dependiendo del formato en el que el usuario indique los puertos


  if '-' in ports_str: # Si el "-" está dentro de los valores del parámetro -p o --port
    start,end=map(int,ports_str.split('-')) # Con split separamos los valores tomando como delimitador el "-" creando una lista de dos elementos, con map pasamos a int cada elemento de la lista
    return range(start,end+1) # Retornamos la lista desde el valor de inicio hasta el valor del final+1
  elif ',' in ports_str: # Si la "," está dentro de los valores del parámetro -p o --port
    return map(int, ports_str.split(',')) # Retornamos la lista con split separamos los valores tomando como delimitador la ",", con map pasamos a int cada elemento de la lista
  else: # Si indicamos un único puerto
    return list((int(ports_str),)) # Retornamos una lista con un único puerto haciendo un typecast de int


def main():

  target,ports_str= get_arguments() # Recibimos los valores de los parámetros elegidos
  ports=parse_ports(ports_str) # Guardamos en una variable las listas retornadas de la función parse_ports
  scan_ports(ports,target) # Llamamos a la función scan_ports pasando las variables ports y target

if __name__ == '__main__':
  main()
