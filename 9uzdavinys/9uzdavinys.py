#!/usr/bin/env python3

import sys
import re
from re import finditer

transitions = {
    'A' : 'G',
    'G' : 'A',
    'C' : 'T',
    'T' : 'C'
}

transversions = {
    'A' : 'CT',
    'C' : 'AG',
    'G' : 'TC',
    'T' : 'GA'
}

sequences = []

try:
    if len (sys.argv) == 3:
        inputFile = sys.argv[1]
        outputFile = sys.argv[2]
    else:
        raise TypeError
except:
    sys.exit('Reikia įvesti dviejų failų pavadinimus')

def countMutations(seq1, seq2, mutationType):
    counter = 0
    for base in range(len(seq1)):
        if seq2[base] in mutationType[seq1[base]]:
            counter += 1
    return counter

try:
    with open(inputFile, 'r', encoding = 'utf-8') as input:
        for match in finditer(r'^>.*$([^>]+)', input.read(), re.M | re.I):
            # Ištriname eilučių skirtukus
            sequence = match.group(1).replace('\n', '')
            sequences.append(sequence)

        transit = countMutations(sequences[0], sequences[1], transitions)
        transv = countMutations(sequences[0], sequences[1], transversions)
        ratio = float(transit/transv)


        with open(outputFile, 'w') as output:
            output.write(str(ratio))

except FileNotFoundError:
    sys.exit("Įvesties failas neegzistuoja")
