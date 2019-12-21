# encoding: UTF-8
# Autor: Diego Palmerín Bonada, A01747290
# Descripción:

from sys import stdin, stdout

valores = [int(x) for x in stdin.readline().split()]
minimo, maximo = valores[0], valores[1]
a, b, c = minimo, minimo, minimo

contador = 0
dif = maximo - minimo

stdout.write(str(contador))
