#!/usr/bin/env python3
import subprocess
import os
import sys
import signal
import socket
import netifaces
import scapy.all as scapy
from termcolor import colored
from colorama import Fore,Style


def def_handler(sig,frame): # Creamos una función para gestionar la lógica al pulsar Ctrl+C
  print(colored(f"\n\n[!] Saliendo del programa...\n","red"))
  sys.exit(1)

signal.signal(signal.SIGINT, def_handler) # Capturamos el Ctrl+C

def root(): # Creamos una función donde gestionamos la lógica para comprobar si estamos ejecuntando el script con el usuario root
  if subprocess.check_output(["whoami"]).decode().strip() == 'root':
    return True


def help():
  return "Options: \n\n\t- arp.scan -> Start ARP Scanner (Example: arp.scan)"


def obtener_direccion_red():
    interfaz = netifaces.gateways()['default'][netifaces.AF_INET][1]  # Obtener la interfaz de red predeterminada
    direccion_ip = netifaces.ifaddresses(interfaz)[netifaces.AF_INET][0]['addr']  # Dirección IP
    mascara_subred = netifaces.ifaddresses(interfaz)[netifaces.AF_INET][0]['netmask']  # Máscara de subred

    # Calcular la dirección de red
    ip_red = ip_red_calculada(direccion_ip, mascara_subred)
    return ip_red and mascara_subred

def ip_red_calculada(direccion_ip, mascara_subred):
    direccion_ip_int = int.from_bytes(socket.inet_aton(direccion_ip), 'big')
    mascara_subred_int = int.from_bytes(socket.inet_aton(mascara_subred), 'big')
    ip_red_int = direccion_ip_int & mascara_subred_int
    ip_red = socket.inet_ntoa(ip_red_int.to_bytes(4, 'big'))
    return ip_red


def arp_scan():
  direccion_red = obtener_direccion_red()
  mascara_subred = obtener_direccion_red()
  print(mascara_subred)
  arp_scan=scapy.arping(direccion_red)


def menu():
  os.system("clear")
  while True:
    option= input(Fore.YELLOW+ "\n NoC"+Fore.RED+"Sniffer" + Fore.GREEN+ "v1.0"+ Fore.YELLOW + " > " + Fore.WHITE)
    if option == "help":
      print(Fore.YELLOW+ "\n NoC"+Fore.RED+"Sniffer" + Fore.GREEN+ "v1.0"+ Fore.YELLOW + " > " + Fore.WHITE + help())
    elif option == "arp.scan":
      arp_scan()




def main():
  if root():
    menu()




if __name__ == '__main__':
  main()
