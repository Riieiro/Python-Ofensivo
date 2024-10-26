#!/usr/bin/env python3

import scapy.all as scapy
import argparse
import subprocess
from termcolor import colored



def root():
  if subprocess.check_output(["whoami"]).decode().strip() == 'root':
    return True


def get_arguments():
  parser= argparse.ArgumentParser(description="ARP Scanner")
  parser.add_argument("-t", "--target",required=True, dest="target",help="Host / IP Range to Scan")


  args=parser.parse_args()
  return args.target


def scan(ip):

  print("\n")
  arp_scan=scapy.arping(ip) # Realizamos el escaneo ARP

"""
Manera compleja para crear y enviar los paquetes ARP manualmente

  arp_packet = scapy.ARP(pdst=ip) # Ip destino ARP request
  broadcast_packet= scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # MAC destino ARP request

  arp_packet = broadcast_packet/arp_packet # La "/" une capas o protocolos de red, fomando así el paquete ARP request

  answered,unanswered= scapy.srp(arp_packet, verbose=False, timeout=1) # Mandamos el paquete ARP, almacenando los que tienen respuesta o no en variables distintas

  print(colored("\n[+] Mostrando las respuestas ARP:\n","yellow"))
  response= answered.summary() # Indicamos que haga un resumen del paquete con respuesta
"""
def main():
  if root():
    target = get_arguments()
    scan(target)
  else:
    print(colored("\n[!] Este script necesita ser ejecutado por el usuario root.","red"))


if __name__ == '__main__':
  main()
