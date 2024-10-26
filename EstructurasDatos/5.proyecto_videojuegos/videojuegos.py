#!/usr/bin/env python3
from colorama import init, Fore, Back, Style


# Géneros
generos= {
  "Super Mario Bros": "Aventura",
  "Zelda" : "Aventura",
  "CyberPunk 2077": "Rol",
  "Final Fantasy VII": "Rol"
}


# Ventas y Stock
ventas_y_stock = {
  "Super Mario Bros": (400, 200),
  "Zelda": (600, 20),
  "CyberPunk 2077": (60, 120),
  "Final Fantasy VII": (924, 0)
}

# Clientes
clientes = {
  "Super Mario Bros": {"Javi", "Mario", "Pepe", "Luis"},
  "Zelda": {"Javi", "Manolo", "Lucia","Pepe"},
  "CyberPunk 2077": {"Manolo", "Juan", "Pepe", "Antonio"},
  "Final Fantasy VII": {"Lucia", "Paula", "Luis", "Javi", "Patricia"}
}
# Precio
precio= {
  "Super Mario Bros": 50,
  "Zelda": 35.99,
  "CyberPunk 2077": 69.99,
  "Final Fantasy VII": 25.35
}

# Sumario

def juegos_disp():
  print(f"\n{Fore.YELLOW}[i] Mostrando los juegos disponibles: \n{Fore.RESET}")
  for juego,genero in generos.items():
    stock = ventas_y_stock[juego][1]
    if stock > 1:
      print(f"\t{Fore.YELLOW}[+]{Fore.RESET} {juego} -> {Fore.RED}{genero}{Fore.RESET} {Fore.BLUE}||{Fore.RESET} {Fore.YELLOW}[+]{Fore.RESET} Stock disponible -> {Fore.GREEN}{ventas_y_stock[juego][1]}{Fore.RESET}")
    else:
      print(f"\t{Fore.YELLOW}[+]{Fore.RESET} {juego} -> {Fore.RED}{genero}{Fore.RESET} {Fore.BLUE}||{Fore.RESET} {Fore.YELLOW}[+]{Fore.RESET} Stock disponible -> {Fore.RED}{ventas_y_stock[juego][1]}{Fore.RESET} ->{Fore.RED} Temporalmente sin stock{Fore.RESET}")
  total_ventas= lambda: sum(ventas for juego, (ventas, _) in ventas_y_stock.items())
  print(f"\n\t{Fore.YELLOW}[i]{Fore.RESET} Ventas totales: {Fore.GREEN}{total_ventas()}{Fore.RESET}")

def resumen_juego():
  mi_juego = str(input(f"\n{Fore.YELLOW}[?] Introduce el nombre del juego: {Fore.RESET}"))
  print(f"\n{Fore.YELLOW}[i] Resumen del juego {mi_juego}{Fore.RESET}")
  print(f"\n\t{Fore.YELLOW}[+]{Fore.RESET} Género del juego: {Fore.GREEN}{generos[mi_juego]}{Fore.RESET}")
  print(f"\t{Fore.YELLOW}[+]{Fore.RESET} Precio {Fore.GREEN}{precio[mi_juego]}€{Fore.RESET}")
  print(f"\t{Fore.YELLOW}[+]{Fore.RESET} Total de ventas para este juego: {Fore.GREEN}{ventas_y_stock[mi_juego][0]}{Fore.RESET}")
  print(f"\t{Fore.YELLOW}[+]{Fore.RESET} Total de stock para este juego: {Fore.GREEN}{ventas_y_stock[mi_juego][1]}{Fore.RESET}")
  print(f"\t{Fore.YELLOW}[+]{Fore.RESET} Clientes que han adquirido el juego: {Fore.GREEN}{', '.join(clientes[mi_juego])}{Fore.RESET}")

def opciones():
  print(f"\n{Fore.YELLOW}[i] Mostrando opciones disponibles:{Fore.RESET}")
  print(f"\n\t{Fore.YELLOW}[1]{Fore.RESET} Mostrar juegos disponibles")
  print(f"\t{Fore.YELLOW}[2]{Fore.RESET} Buscar por nombre del juego")
  respuesta = input(f"\n{Fore.YELLOW}[+]{Fore.RESET} Elige una opción ({Fore.YELLOW}1{Fore.RESET}{Fore.RED}/{Fore.RESET}{Fore.YELLOW}2{Fore.RESET}): {Fore.RESET}")
  if respuesta == "1":
    juegos_disp()
  elif respuesta == "2":
     resumen_juego()
opciones()


