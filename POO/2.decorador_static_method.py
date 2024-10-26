#!/usr/bin/env python3



class Calculadora:

  @staticmethod
  def suma(num1,num2):

    return num1 + num2

  @staticmethod
  def resta(num1,num2):

    return num1 - num2

  @staticmethod
  def multiplicacion(num1,num2):

    return num1 * num2

  @staticmethod
  def division(num1,num2):

    return num1 / num2 if num2 !=0 else "\n[!] Error: No se puede dividir un número entre 0"


print(Calculadora.suma(2,8))
print(Calculadora.resta(8,4))
print(Calculadora.multiplicacion(2,5))
print(Calculadora.division(4,2))



class Automovil:

  def __init__(self,marca,modelo):

    self.marca = marca
    self.modelo = modelo

  @classmethod
  def deportivos(cls, marca):

    return cls(marca,"Deportivo")

  def __str__(self):

    return f"La marca {self.marca} es un modelo {self.modelo}"

  @classmethod
  def clasico(cls,marca):

    return  cls(marca,"Clásico")

  def __str__(self):

    return f"La marca {self.marca} es un modelo {self.modelo}"

deportivo = print(Automovil.deportivos("Ferrari"))   # Automovil("Ferrari, "Deportivo"")
clasico = print(Automovil.clasico("Seat"))           # Automovil("Seat", "Clásico")



class Estudiantes:

  estudiantes = []

  def __init__(self,nombre,edad):

    self.nombre = nombre
    self.edad = edad

    Estudiantes.estudiantes.append(self)

  @staticmethod
  def es_mayor_de_edad(edad):
    return edad>=18

  @classmethod
  def crear_estudiante(cls, nombre,edad):

    if cls.es_mayor_de_edad(edad):
      return cls(nombre,edad)
    else:
      print(f"\n[!] Error: El estudiante {nombre} es menor de edad")

  @staticmethod
  def mostrar_estudiante():

    for i,estudiante in enumerate(Estudiantes.estudiantes):
      print(f"[+] Estudiante número [{i+1}]: {estudiante.nombre}")


Estudiantes.crear_estudiante("Javi",19)
Estudiantes.crear_estudiante("Peter",59)
Estudiantes.crear_estudiante("Paula",29)
Estudiantes.crear_estudiante("Julian",17)
Estudiantes.crear_estudiante("Pepe",12)


Estudiantes.mostrar_estudiante()
