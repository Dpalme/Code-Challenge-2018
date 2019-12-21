# encoding: UTF-8
# Autor: Diego Palmerín Bonada, A01747290
# Descripción: Destructor

from sys import stdin, stdout


def main(edificios, alturasInt):
    areas = set([max(alturasInt)])
    minh = min(alturasInt)
    minhIndex = alturasInt.index(minh)-(len(alturasInt)/2)
    if minhIndex < 0:
        minhIndex = minhIndex * -2
    else:
        minhIndex = minhIndex * 2
    while edificios > 0:
        if edificios < minhIndex:
            areas.add(edificios * minh)
        else:
            areas.add(edificios * min(alturasInt))
        if edificios % 2 == 0:
            alturasInt.pop()
        else:
            alturasInt.pop(0)
        edificios = edificios - 1
    stdout.write(str(max(areas))+"\n")


if __name__ == "__main__":
    edificios = int(stdin.readline())
    alturasInt = [int(x) for x in stdin.readline().split()]
