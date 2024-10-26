#!/usr/bin/env python3

import datetime

"""
Tipos de Datos Principales: ‘datetime‘ incluye varios tipos de datos, como ‘date‘ (para fechas), ‘time‘ (para horas), ‘datetime‘ (para fechas y horas combinadas),
y ‘timedelta‘ (para representar diferencias de tiempo). 
"""
ahora = datetime.datetime.now() # Hora actual
print(ahora)

año = ahora.year
mes = ahora.month
dia = ahora.day              # Con la función anterior podemos almacenar el dato que queramos
horas = ahora.hour
minutos = ahora.minute
segundos = ahora.second

print(f"\n[+] Año: {año}, mes: {mes}, día: {dia}, horas: {horas}, minutos: {minutos}, segundos: {segundos}\n")

fecha= datetime.date(2022,10,24) # Representa la fecha indicada
print(fecha)

time= datetime.time(14,15,15) # Representa la hora indicada
print(time)

fecha_hora=datetime.datetime(2022,10,24,14,15,15) # Representa la fecha y la hora indicada
print(fecha_hora)



