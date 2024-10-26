#!/usr/bin/env python3

import urllib3

http= urllib3.PoolManager() # Controlador de conexiones


response = http.request('GET', 'https://httpbin.org/get')
print(response.data.decode())


data= "Esto es una prueba"
encoded_data = data.encode()
response = http.request('POST','https://httpbin.org/post', body=encoded_data)
print(response.data.decode())


response = http.request('POST','https://httpbin.org/post', fields={'atributo': 'valor'})
print(response.data.decode())


response = http.request('GET', 'https://httpbin.org/redirect/1',redirect=False)
print(f"\n[+] La ruta a la que estamos siendo redirigidos con el código de estado {response.status} es: {response.get_redirect_location()}")
