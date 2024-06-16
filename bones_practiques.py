#!/usr/bin/env python

'''
Divisió entera.

Institut Icària
Programació - 1r Batxillerat - Curs 2023-24

Fa la divisió de dos nombres enters donant quocient i residu.
'''

__author__ = "Luis Rey Cabrerizo"
__email__ = "lrey@instituticaria.cat"
__date__ = "2023/07/17"

# Entrada de dades
print("Divisió de nombres enters")
dividend = int(input("Entra el dividend: "))
divisor = int(input("Entra el divisor: "))

# Càlculs
quocient = dividend // divisor
residu = dividend % divisor

# Impressió resultats
print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")
