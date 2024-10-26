#!/usr/bin/env python3 

import requests


response = requests.get('https://httpbin.org/basic-auth/foo/bar', auth=('foo','bar')) # Mandamos una petición get autenticándonos directamente
print(response.text)


cookies = {'cookies_are': 'coking'} # Creamos una variable con las nuevas cookies
response = requests.get('https://httpbin.org/cookies', cookies=cookies) # Cambiamos las cookies
print(response.text)


my_file= {'archivo' : open('example.txt', 'r')} # Guardamos el archivo example.txt en una variable
response = requests.post('https://httpbin.org/post', files=my_file) # Mandamos una petición post con el archivo example.txt
print(response.text)


set_cookies_url= 'https://httpbin.org/cookies/set/my_cookie/123123' # Creamos una variable con la url seteando una nueva cookie
s = requests.Session() # De esta forma guardamos la sesión con las cookies nuevas
response = s.get(set_cookies_url) # Mandamos una petición get con la url con cookies nuevas
response = s.get('https://httpbin.org/cookies') # Mandamos una petición get a la url de las cookies
print(response.text)


s = requests.Session() 
headers = {'Custom-Header':'my_custom_header'}
req = requests.Request('GET', 'https://httpbin.org/get', headers=headers)
prepped = req.prepare()
prepped.headers['Custom-Header'] = 'my_header_changed'
prepped.headers['Another-Header'] = 'this_is_another_header'
response = s.send(prepped)
print(response.text)


r = requests.get('http://github.com', allow_redirects=False)
print(r.url)


r = requests.get('http://github.com')
for i in r.history:
  print(f"\n\t[+] Hemos pasado por el dominio {i.url} con un código de estado {i.status_code}")
print(f"\n[+] URL final: {r.url} con el código de estado {r.status_code}")


with requests.Session() as session : # De esta forma mantenemos la sesión iniciada arrastrando todos los datos de la sesión
  session.auth = ('pepe', '123')
  response1 = session.get('https://httpbin.org/basic-auth/pepe/123')
  print(response1.text)


  response2= session.get('https://httpbin.org/basic-auth/pepe/123')
  print(response2.text)


requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
response = requests.get('https://195.78.66.103/', verify=False)
print(response.text)
