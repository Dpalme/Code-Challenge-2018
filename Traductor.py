# encoding: UTF-8
# Autor: Diego Palmerín Bonada, A01747290
# Descripción: Traducir de una forma de if else a otra

from sys import stdin

inp = stdin.readline().strip()
quest = inp.index("?")
colon = inp.index(":")
string1 = inp[:quest-1]
string2 = inp[quest+1:colon]
string3 = inp[colon+1:]
print("""if(%s)
     %s;
else
     %s;
""" % (string1, string2, string3))