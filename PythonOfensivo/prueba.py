import socket
import netifaces

def obtener_direccion_red():
    interfaz = netifaces.gateways()['default'][netifaces.AF_INET][1]  # Obtener la interfaz de red predeterminada
    direccion_ip = netifaces.ifaddresses(interfaz)[netifaces.AF_INET][0]['addr']  # Dirección IP

    return direccion_ip


#print(obtener_direccion_red())



ip= obtener_direccion_red()
