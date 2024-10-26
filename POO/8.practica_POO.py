#!/usr/bin/env python3

class ESO:
  alumnos=[]
  alumnos_suspendidos=[]

  def __init__(self,nombre,clase,edad,nota):

    self.nombre = nombre
    self.clase = clase
    self.edad = edad
    self.nota = nota


  @staticmethod
  def aprobados(nota):

    return nota>=5

  @classmethod
  def crear_alumno(cls,nombre,clase,edad,nota):

    if cls.aprobados(nota):
      cls.alumnos.append(nombre)
      return f"\n[+] El alumno {nombre} {edad} {clase} ha aprobado -> {nota} {cls.alumnos}"
    else:
      cls.alumnos_suspendidos.append(nombre)
      return f"\n[+] El alumno {nombre} {edad} {clase} ha suspendido -> {nota} {cls.alumnos_suspendidos}"

class Bachillerato(ESO):
  alumnos=[]
  alumnos_suspendidos=[]

  @classmethod
  def crear_alumno(cls,nombre,clase,edad,nota):

    if cls.aprobados(nota):
      cls.alumnos.append(nombre)
      return f"\n[+] El alumno {nombre} {edad} {clase} ha aprobado -> {nota} {cls.alumnos}"
    else:
      cls.alumnos_suspendidos.append(nombre)
      return f"\n[+] El alumno {nombre} {edad} {clase} ha suspendido -> {nota} {cls.alumnos_suspendidos}"

print(ESO.crear_alumno("Javier","2A",14,8.5))
print(ESO.crear_alumno("Pepe","4A",16,3.5))
print(ESO.crear_alumno("Juan","1A",12,9.5))
print(ESO.crear_alumno("Paula","3A",13,4.5))

print(Bachillerato.crear_alumno("Jose", "1B", 17, 7))
print(Bachillerato.crear_alumno("Luis", "1C", 17, 3))
print(Bachillerato.crear_alumno("Lucas", "2A", 18, 9))
print(Bachillerato.crear_alumno("Pablo", "2B", 19, 0.5))
