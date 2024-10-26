#!/usr/bin/env python3

import socket

def start_udp_server():

  host='localhost'
  port=1234

  with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s: # De esta forma estamos diciendo que el tipo de conexión es IPV4 y UDP
     s.bind((host,port)) # Nos ponemos en escucha
     print(f"\n[+] Servidor UDP iniciado en {host}:{port}")

     while True:
      data,addr = s.recvfrom(1024) # De esta forma guardamos el mensaje y la dirección del cliente
      print(f"\n[+] Mensaje enviado por el cliente: {data.decode()}")
      print(f"[+] Información del cliente que nos ha enviado el mensaje: {addr}")

start_udp_server()
