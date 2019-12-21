# encoding: UTF-8
# Autor: Diego Palmerín Bonada, A01747290
# Descripción: divide y hubiera ganado el code

from sys import stdin, stdout
numeros = int(stdin.readline())
listaNums = [int(x) for x in stdin.readline().split()]
clon, clonn = listaNums, len(listaNums)
sumas = []

while clonn > 0:
    sumas.append(sum(clon))
    if numeros % 2 == 0:
        clon.pop(clonn-1)
    else:
        clon.pop(0)
        clonn += - 1

clon, clonn = listaNums, numeros
listaNums.pop(clonn-1)
print clon
while clonn > 0:
    sumas.append(sum(clon))
    clon.pop(clonn-1)
    clonn += - 1

clon, clonn = listaNums, numeros
listaNums.pop(0)
while clonn > 0:
    sumas.append(sum(clon))
    clon.pop(0)
    clonn += - 1

stdout.writelines(str(max(sumas)))
