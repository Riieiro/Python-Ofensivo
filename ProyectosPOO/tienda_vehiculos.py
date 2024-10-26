#!/usr/bin/env python3

class Vehiculo:

  def __init__(self,matricula,modelo):

    self.matricula=matricula
    self.modelo=modelo
    self.disponible=True

  def alquilar(self):
    if self.disponible:
      self.disponible=False

  def devolver(self):
    if not self.disponible:
      self.disponible=True

  def __repr__(self):
    return f"Vehiculo=({self.matricula}), Modelo=({self.modelo}), Disponible=({'Si' if self.disponible else 'No'})"


class Concesionario:

  def __init__(self):

    self.vehiculos=[]

  def agregar_vehiculo(self,vehiculo):

    self.vehiculos.append(vehiculo)

  def alquilar_vehiculo(self,matricula):

    for vehiculo in self.vehiculos:
      if vehiculo.matricula==matricula:
        vehiculo.alquilar()

  def devolver_vehiculo(self,matricula):

    for vehiculo in self.vehiculos:
      if vehiculo.matricula==matricula:
        vehiculo.devolver()

  def __repr__(self):

    return "\n".join(str(vehiculo)for vehiculo in self.vehiculos)


if __name__ == '__main__':

  concesionario=Concesionario()
  concesionario.agregar_vehiculo(Vehiculo("AKDNB23", "Ferrari"))
  concesionario.agregar_vehiculo(Vehiculo("BDF342", "Tesla"))

  print("\n[+] Flota inicial:\n")
  print(concesionario)


  concesionario.alquilar_vehiculo("AKDNB23")
  print(f"\n{concesionario}")

  concesionario.devolver_vehiculo("AKDNB23")
  print(f"\n{concesionario}")
