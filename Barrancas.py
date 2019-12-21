# encoding: UTF-8
# Autor: Diego Palmerín Bonada, A01747290
# Descripción: Barrancas


import random


def obtenerNyK(string: str):
    NyK = string.split()
    n = NyK[0]
    k = NyK[1]
    return int(n), int(k)


def calcularMejorRuta(emociones, k):
    max = 0
    suma = 0
    paradaPasada = 0
    for incio in range(0, len(emociones)):
        for x in range(incio, len(emociones)):
            for noLaUso in range(0, k):
                parada = random.randint(paradaPasada+1, len(emociones)-1)
                if paradaPasada == 0:
                    paradaPasada = incio
                else:
                    suma = suma + (emociones[parada] - emociones[paradaPasada])
                if max < suma:
                    max = suma
            suma = 0
    return max


def main():
    string = input("N y K: ")
    n, k = obtenerNyK(string)
    emociones = []
    for x in range(0, n):
        emociones.append(int(input("emoción: ")))
    print("La máxima emoción es %d" % calcularMejorRuta(emociones, k))


main()
