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
    sys.exit ('Reikia įvesti dviejų failų pavadinimus')



# Tranzicijos - mutacija, A<->G, C<->T 
def countTransitions(seq1, seq2):
    transitionCounter = 0
    for base in range(len(seq1)):
        if seq2[base] == transitions[seq1[base]]:
            transitionCounter += 1
    return transitionCounter

# Transvercija - mutacija, A<->C, G<->T A<->T, C<->G
def countTransversion(seq1, seq2):
    transversionCounter = 0
    for base in range(len(seq1)):
        if seq2[base] in transversions[seq1[base]]:
            transversionCounter += 1
    return transversionCounter



try:
    with open(inputFile, 'r', encoding = 'utf-8') as input:
        for match in finditer(r'^>.*$([^>]+)', input.read(), re.M | re.I):
            # Ištriname eilučių skirtukus
            sequence = match.group(1).replace('\n', '')
            sequences.append(sequence)

        transit = countTransitions(sequences[0], sequences[1])
        transv = countTransversion(sequences[0], sequences[1])
        ratio = float(transit/transv)


        with open(outputFile, 'w') as output:
            output.write(str(ratio))

except FileNotFoundError:
    sys.exit("Įvesties failas neegzistuoja")