#!/usr/bin/env python3

import argparse 
import subprocess
import sys
import signal
import re
from termcolor import colored
from concurrent.futures import ThreadPoolExecutor


def def_handler(sig,frame): # Creamos una función donde gestionaremos la lógica al pulsar Ctrl+C
  print(colored(f"\n[!] Saliendo...\n","red"))
  sys.exit(1)

signal.signal(signal.SIGINT, def_handler) # Capturamos el Ctrl+C


def get_arguments(): # Creamos una función donde gestionaremos la lógica al recibir parámetros

  parser=argparse.ArgumentParser(description="Herramienta para descubrir host activos en una red (ICMP)")
  parser.add_argument("-t","--target",required=True,dest="target", help="Host o rango de red a escanear") # Parámetro requerido
  parser.add_argument("-th","--thread",dest="max_threads",help="Máximo de hilos al realizar el escaneo", type=int) # Parámetro tipo int


  return parser.parse_args() # Retornamos los argumentos


def parse_target(target_str): # Creamos una función donde gestionaremos la lógica para devolver la ip ya parseada

  target_str_splitted=target_str.split('.') # ["192", "168", "1", "1-100"])
  first_three_octets='.'.join(target_str_splitted[:3]) # 192.168.1
  ip_total='.'.join(target_str_splitted[:4]) # 192.168.1.1 | 192.168.1.1-100
  ip_valid=re.match(r"^192\.168\.\d{1,3}\.\d{1,3}(-\d{1,3})?$", ip_total) # Patrón para comprobar si el argumento indicado target es válido



  if len(target_str_splitted) == 4 and ip_valid: # Si la lista es más larga que 4 argumentos y no corresponde con el patrón, significa que no es ip válida
    if "-" in target_str_splitted[3]: # Si el último octet tiene un "-" quiere decir que queremos escanear un rango de ip
      start,end=target_str_splitted[3].split('-') # Tomamos como delimitador el "-" y creamos dos variables
      return [f"{first_three_octets}.{i}" for i in range(int(start), int(end)+1)] # Retornamos los tres primeros octets añadiendole el último que es un bucle del primer número al último
    else:
      return [target_str] # Retornamos al ip una vez pasada la validación
  else:
    print(colored(f"\n[!] El formato de IP o rango de IP no es válido","red"))


def host_discovery(target): # Creamos una función donde gestionaremos la lógica del escaneo

  try:
    ping= subprocess.run(["ping","-c","1",target], timeout=1, stdout=subprocess.DEVNULL) # Ejecutamos un comando a nivel sistema "ping -c 1 192.168.1.1" mandando el stout a /dev/null
    if ping.returncode==0: # Si el código de estado es 0, es decir exitoso
      print(colored(f"\n[+] La IP {target} está activa","green")) # Indicamos que está abierto
  except subprocess.TimeoutExpired: # Para poder realizar Ctrl+C y que el programa no se quede colgado, necesitamos controlar esta excepción
    pass


def main():

  args=get_arguments() # Recogemos todos los argumentos de los parámetros

  targets=parse_target(args.target) # Guardamos en targets la ip retornada de la función parse_target



  with ThreadPoolExecutor(max_workers=args.max_threads) as executor: # De esta forma empleamos hilos que se cierran automáticamente indicando el máximo de hilos
    executor.map(host_discovery,targets) # La función map necesita un único argumento para pasarle a la función que indiquemos, actuando como un bucle



if __name__=='__main__':
  main()


