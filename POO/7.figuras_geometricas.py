#!/usr/bin/env python3

class FigurasGeometricas():


  def __init__(self,base):

    self.base=base

  def CalcularArea(self):

    raise NotImplementedError("Las subclases definidads deben implementar este método") 

class Cuadrado(FigurasGeometricas):

  def CalcularArea(self):

    return self.base*self.base

class Rectangulo(FigurasGeometricas):

  def __init__(self,base,altura):

    self.base=base
    self.altura=altura

  def CalcularArea(self):

    return self.base*self.altura

class Circulo(FigurasGeometricas):

  pi=3.14

  def __init__(self,radio):

    self.radio=radio

  def CalcularArea(self):

    return round(Circulo.pi * (self.radio**2),2)

def Area(figura):

  print(f"{figura.CalcularArea()}")



respuesta=input("\n[+] Selecciona la figura geometrica: ")

if respuesta == "cuadrado":

  lado=int(input("\n[+] Introduce los centímetros que mide el lado del cuadrado: "))
  Cuadrado=Cuadrado(lado)
  Area(Cuadrado)

elif respuesta == "rectangulo":

  base=int(input("\n[+] Introduce los centímetros que mide la base del rectángulo: "))
  altura=int(input("\n[+] Introduce los centímetros que mide la altura del rectángulo: "))
  Rectangulo=Rectangulo(base,altura)
  Area(Rectangulo)

elif respuesta == "circulo" :

  radio=float(input("\n[+] Introduce los centímetros que mide el radio del circulo: "))
  Circulo=Circulo(radio)
  Area(Circulo)







