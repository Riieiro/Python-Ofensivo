#!/usr/bin/env python3
"""
Diferencias Clave

    - Modelo de Ejecución: ‘threading‘ ejecuta hilos en un solo proceso compartiendo el mismo espacio de memoria, 
    mientras ‘multiprocessing‘ ejecuta múltiples procesos con memoria independiente.
    - Uso de CPU: ‘multiprocessing‘ es más adecuado para tareas que requieren mucho cálculo y pueden beneficiarse de múltiples núcleos de CPU, 
    mientras que ‘threading‘ es mejor para tareas limitadas por E/S.
    - Global Interpreter Lock (GIL): ‘threading‘ está limitado por el GIL en CPython, lo que restringe la ejecución en paralelo de hilos, 
    mientras que ‘multiprocessing‘ no tiene esta limitación.
    - Gestión de Recursos: ‘threading‘ es más eficiente en términos de memoria y creación de hilos, 
    pero ‘multiprocessing‘ es más eficaz para tareas aisladas y seguras en cuanto a datos.

"""


import threading
import time


def tarea(num_tarea):

  print(f"\n[+] Hilo {num_tarea}")
  time.sleep(2)
  print(f"\n[+] Hilo {num_tarea} finalizando")


thread1 = threading.Thread(target=tarea, args=(1,)) # Para que la tupla de args funcione es necesaria la coma después del número
thread2 = threading.Thread(target=tarea, args=(2,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(f"\n[+] los hilos han finalizadado exitosamente")


import requests
# Sin hilos
dominios = ["https://google.es","https://yahoo.com","https://wikipedia.org"]
start_time= time.time()
for url in dominios:
  response = requests.get(url)
  print(f"\n[+] URL [{url}]: {len(response.content)} bytes")

end_time= time.time()
print(f"\n[+] Tiempo total transcurrido: {end_time-start_time}")


# Con hilos
start_time=time.time()
def busqueda(url):
  response = requests.get(url)
  print(f"\n[+] URL [{url}]: {len(response.content)} bytes")

hilos= []
for url in dominios:
  thread= threading.Thread(target=busqueda,args=(url,))
  thread.start()

  hilos.append(thread)

for hilo in hilos: # Para poder hacer un join y que no cree la variable end_time antes de tiempo y así poder ver el tiempo real transcurrido
  hilo.join()

end_time=time.time()
print(f"\n[+] Tiempo total transcurrido: {end_time-start_time}")
