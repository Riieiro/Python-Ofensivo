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



import multiprocessing
import time

def tarea(num_tarea):
  print(f"\n[+] Proceso {num_tarea} iniciando")
  time.sleep(2)
  print(f"\n[+] Proceso {num_tarea} finalizando")

proceso1 = multiprocessing.Process(target=tarea, args=(1,))
proceso2 = multiprocessing.Process(target=tarea, args=(2,))

proceso1.start()
proceso2.start()

proceso1.join()
proceso2.join()

print(f"\n[+] Los procesos han finalizado exitosamente")


import requests
def realizar_peticion(url):
  response = requests.get(url)
  print(f"\n[+] URL [{url}]: {len(response.content)} bytes")

dominios = ["https://google.es","https://yahoo.com","https://wikipedia.org"]
start_time=time.time()
procesos=[]
for url in dominios:
  proceso= multiprocessing.Process(target=realizar_peticion,args=(url,))
  proceso.start()
  procesos.append(proceso)

for proceso in procesos:
  proceso.join()

end_time=time.time()
print(f"\n[+] Tiempo total transcurrido: {end_time-start_time}")

