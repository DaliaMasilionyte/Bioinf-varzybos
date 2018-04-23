#!/usr/bin/env python3
import sys

markovChain = {}
sequences = []

try:
    if len(sys.argv) == 4:
        markovFile = sys.argv[1]
        dataFile = sys.argv[2]
        outputFile = sys.argv[3]
    else:
        raise TypeError
except:
    sys.exit ('Reikia įvesti trijų failų pavadinimus')


# Reikia susikurti Markovo tikimybių saugojimo struktūrą
with open(markovFile, 'r') as markovFile:
    # Markovo failą skaitome po eilutę
    for line in markovFile:
        # Eilutę paverčiame masyvu, skirtukas yra tarpas
        lineArray = line.split()
        # Bazė, kurios mutacijos tikimybes stebime yra pirmoji
        head = lineArray[0][0]
        # Išmetame "galvą" iš masyvo
        lineArray.pop(0)
        transitions = {}
        for transition in lineArray:
            base, probability = transition.split(':')
            transitions[base] = float(probability)
        markovChain[head] = transitions

with open(dataFile, 'r') as dataFile:
    for line in dataFile:
        # strip() funkcija nukerpa eilutės pabaigos skirtuką
        line = line.strip()
        sequences.append(line)

prob = 1
for index in range(len(sequences[0])):
        # Tikimybę dauginame iš tikimybės, kad pirmos sekos nukleotidas
        # mutuos į antros sekos nukleotidą
        prob *= markovChain[sequences[0][index]][sequences[1][index]]


with open(outputFile, 'w') as outputFile:
    outputFile.write(str(prob))

