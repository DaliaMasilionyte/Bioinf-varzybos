#!/usr/bin/env python3

import sys

x = y = z = 0
numOfAtoms = 0

try:
    if len(sys.argv) == 3:
        inputFile = sys.argv[1]
        outputFile = sys.argv[2]
    else:
        raise TypeError
except:
    sys.exit('Reikia įvesti dviejų failų pavadinimus')


def divide(coordinate):
    return coordinate / numOfAtoms

try:
    with open(inputFile, 'r') as inputFile:
        for line in inputFile:
            atom = line.split()
            x += float(atom[1])
            y += float(atom[2])
            z += float(atom[3])
            numOfAtoms += 1

        x = divide(x)
        y = divide(y)
        z = divide(z)

except FileNotFoundError:
    sys.exit("Įvesties failas neegzistuoja")


with open(outputFile, 'w') as output:
    output.write('CENTRAS {} {} {}'.format(x, y, z))


