#!/usr/bin/env python3

import re
import os
import signal
import sys
import subprocess
import argparse
import scapy.all as scapy
from termcolor import colored


def def_handler(sig,frame): # Creamos una función para gestionar la lógica al pulsar Ctrl+C
  print(colored(f"\n[!] Saliendo del programa...\n","red"))
  sys.exit(1)

signal.signal(signal.SIGINT, def_handler) # Capturamos el Ctrl+C


def get_arguments(): # Creamos una función para gestionar la lógica al recibir parámetros
  parser=argparse.ArgumentParser(description="DNS Sniffer")
  parser.add_argument("-i", "--interface", required=True,dest="interface", help="Interface to sniff")

  return parser.parse_args()


def root(): # Creamos una función donde gestionamos la lógica para comprobar si estamos ejecuntando el script con el usuario root
  if subprocess.check_output(["whoami"]).decode().strip() == 'root':
    return True


def process_dns_packet(packet): # Creamos una función donde gestionamos la lógica sobre cada paquete que nos llega udp and port 53
  if packet.haslayer(scapy.DNSQR): # A veces algunos paquetes no tienen la capa DNSQR, por eso nos aseguramos que esta capa tiene contenido
    domain = packet[scapy.DNSQR].qname.decode() # Dentro de la capa DNSQR filtramos por qname, recibiendo así el dominio final

    exclude_keywords=["google", "cloud", "bing", "static"] # Creamos una lista con las palabras que no queremos que aparezcan

    if domain not in domains_seen and not any(keyword in domain for keyword in exclude_keywords): # Si el dominio no está en el set de domains_seen
                                          # Iteras por cada valor de la lista exclude_keywords y con any indicas que si el elemento de la lista esta en domain devuelva un True
      domains_seen.add(domain) # Almacenamos el dominio en el set domains_seen
      split_domain=domain.split(".") # Separamos todos los dominios tomando el "." como delimitador
      if re.findall("www", domain): # Si el dominio contiene "www"
        print(colored(f"[+] Domain: {domain}","green"))
      elif len(split_domain) == 3: # Si la lista creada con split tiene 3 elementos
        print(colored(f"[+] Domain: {domain}","green"))
      else:
        print(f"[+] Domain: {domain}")


def set_global(): # Creamos una función donde creamos una variable global
  global domains_seen
  domains_seen = set()


def main():
  if root():
    os.system("clear")
    set_global()

    arguments=get_arguments()

    print(colored("\n[+] Interceptando paquetes de la máquina víctima:\n","yellow"))
    scapy.sniff(iface=arguments.interface, filter="udp and port 53", prn=process_dns_packet, store=0) # Iface(interfaz), filter(filtro de wireshark), prn(Pasar cada paquete a una función store(Para no almacenarlo en memoria))


if __name__ == '__main__':
  main()
