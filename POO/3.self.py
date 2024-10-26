#!/usr/bin/env python3

class Persona:

  def __init__(self, nombre, edad): # Persona.__init__(marcelo, nombre ,edad)

    self.nombre = nombre # marcelo.nombre = "Marcelo"
    self.edad = edad # marcelo.edad = 28

  def presentacion(self):

    return f"\n[+] Hola {self.nombre}, tienes {self.edad} años"

marcelo=Persona("Marcelo", 28)


print(marcelo.presentacion())



class Calculadora:

  def __init__(self,num1): # Calculadora.__init__(calc,num1)

    self.num1=num1 # calc.num1 = 5

  def suma (self,num2): # Calculadora.suma(calc,num2)

    return self.num1 + num2 # calc.num1 + 8 -> 5+2 = 7

  def doble_suma(self,num1,num2): # Calculadora.doble_suma(calc,num1,num2)

    return self.suma(num1) + self.suma(num2) # calc.suma(2) + calc.suma(5) -> Calculadora.suma(calc,2) + Calculadora.suma(calc,5) = 7+10 = 17

calc = Calculadora(5)
print(calc.suma(8))
print(calc.doble_suma(2,5))


