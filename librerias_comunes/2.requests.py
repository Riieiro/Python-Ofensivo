#!/usr/bin/env python3

import requests


response = requests.get("https://google.es") # Mandamos una petición get y la almacenamos en response


print(f"\n[+] Status code: {response.status_code}\n") # Vemos el código de estado
print(f"\n[+] Mostrando código fuente de la respuesta: \n")


with open ("index.html", "w") as f: # Creamos un archivo index.html con permiso de escritura
  f.write(response.text) # Almacenamos el código fuente de la página en el archivo index.html


# GET
values= {'key1': 'value1','key2':'value2','key3':'value3'} # Creamos un diccionario con ejemplos de clave valor
response = requests.get("https://httpbin.org/get",params=values) # Mandamos una petición get cambiando los argumentos
print(f"\n[+] Url final: {response.url}\n") # Vemos como se quedaría nuestra petición
print(response.text) # Mostramos la respuesta de la petición


# POST
payload= {'key1': 'value1','key2':'value2','key3':'value3'} # Creamos un payload
headers= {'User-Agent' : 'mi-pene'} # Creamos un header para cambiar el User-Agent
response= requests.post("https://httpbin.org/post", data=payload, headers=headers) # Mandamos un petición post enviando datos de un formulario y cambiando el User-Agent
print(f"\n[+] Url final: {response.url}\n")
print(response.text) # Mostramos la respuesta de la petición


headers= {'User-Agent': 'tonto'} # Creamos un header para cambiar el User-Agent
respones=requests.get("https://httpbin.org/get", headers) # Mandamos una petición get cambiando el User-Agent
print(response.request.headers) # Mostramos el User-Agent


try: # De esta forma controlamos los errores que pueden haber en una petición
  response = requests.get('https://google.ese', timeout=1) # Mandamos una petición get con una url incorrecta, indicándole un tiempo máximo para realizar la petición
  response.raise_for_status() # Muestra si ha habido un error

except requests.Timeout:
  print(f"\n[!] La petición ha excedido el límite de tiempo de espera")

except requests.HTTPError as http_err:
  print(f"\n[!] Error HTTP: {http_err}")

except requests.RequestException as err:
  print(f"\n[!] Error: {err}")

else:
  print(f"\n[+] No ha habido ningún error en la solicitud")


response = requests.get('https://httpbin.org/get') # Mandamos una petición get
data=response.json() # Guardamos la respuesta en formato json
if 'headers' in data and 'User-Agent' in data ['headers']: # Si el campo headers y User-Agent se encuentra en el código fuente
  user_agent=data['headers']['User-Agent']
  print(f"\n[+] User-Agent: {user_agent}")
else:
  print(f"\n[!] No existe este campo en la respuesta")
