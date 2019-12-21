# encoding: UTF-8
# Autor: Diego Palmerín Bonada, A01747290
# Descripción: Maquina Descompuesta

from sys import stdin, stdout

cadenas = stdin.readline().split()
c = ""
cadenaFinal = ""

titulo = False
x = len(cadenas)
for n in range(0, x):
    caden = cadenas[n].capitalize()
    if n == x-1:
        cadenaFinal += caden
    else:
        cadenaFinal = " ".join(caden, cadenaFinal)

    if caden.endswith(":"):
        cadenaFinal = cadenaFinal + '"'
        break
else:
    cadenaFinal = cadenaFinal + c.join('"')

stdout.write(cadenaFinal)
