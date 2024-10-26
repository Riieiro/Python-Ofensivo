# example.txt ("Hola mundo")

f = open("example.txt", "w") # De esta forma indicamos que queremos escribir en ese archivo  (En bash sería >)
# f = open("example.txt", "a") # Con la función "a" indicamos que queremos escribir sin borrar el contenido del archivo  (En bash sería >>)

f.write("Hola mundo")

with open("example.txt", "w") as f: # Esta es la forma más óptima de tratar con archivos
  f.write("Hola mundo")


with open("/etc/hosts", "r") as f: # De esta forma guardamos el contenido de /etc/hosts en una variable, para después mostrarla por pantalla
  file_content=f.read()
print(file_content)


with open("/etc/hosts", "r") as f: # Es posible iterar por cada línea del archivo de esta forma
  for line in f:
    print (line.strip()) # Con la función strip() evitamos los espacios entre líneas

"""
with open("/usr/share/wordlists/rockyou.txt", "rb") as f: # Con la opción "b", indicamos que se trata de un archivo binario
  for line in f:
    print(line.strip().decode()) # Con la función decode() descodificamos el texto en bytes
"""

with open ("/usr/share/wordlists/rockyou.txt" , "rb") as f: 
  first_line=f.readline()  # De esta forma guardamos la primera línea del archivo
print(first_line.strip().decode())


mi_lista=["Primera línea\n", "Segunda línea\n", "Tercera línea\n", "Cuarta línea\n"]
with open ("example.txt" ,"w") as f: # De esta forma metemos el contenido de la lista en un archivo
  f.writelines(mi_lista)


with open("/home/rieiro/Rieiro/Pictures/niña.png", "rb") as f_in, open ("image.png", "wb") as f_out: # De esta forma podemos copiar archivos
  file_content=f_in.read()
  f_out.write(file_content)


try:
  with open("prueba.txt","r") as f: # De esta forma podemos comprobar si existe el archivo, controlando el error
    print(f.read())
except FileNotFoundError:
  print("\n[!] No se ha encontrado el archivo")
