#!/usr/bin/env python3
import sys
import re
from re import finditer

sequences = []


try:
    if len(sys.argv) == 3:
        inputFile = sys.argv[1]
        outputFile = sys.argv[2]
    else:
        raise TypeError
except:
    sys.exit('Reikia įvesti dviejų failų pavadinimus')

# Visos sekos vienodo ilgio
def calculateFrequencies(sequences):
    sequenceLength = len(sequences[0])
    frequencyMatrix = {
        'A' : [0] * sequenceLength,
        'C' : [0] * sequenceLength,
        'G' : [0] * sequenceLength,
        'T' : [0] * sequenceLength
    }
    for sequence in sequences:
        for index, nucleotide in enumerate(sequence):
            frequencyMatrix[nucleotide][index] += 1
    return frequencyMatrix

def findConsensus(sequenceLength, frequencyMatrix):
    consensus = ""
    for i in range(sequenceLength):
        maxFrequency = -1
        mostFrequentNucleotide = None
        for nucleotide in "ATGC":
            if frequencyMatrix[nucleotide][i] > maxFrequency:
                maxFrequency = frequencyMatrix[nucleotide][i]
                mostFrequentNucleotide = nucleotide
        # Kadangi galima pateikti bet kurį dažniausiai sutinkamą nukleotidą,
        # kitų nebetikriname
        consensus += mostFrequentNucleotide
    return consensus


try:
    with open(inputFile, 'r', encoding = 'utf-8') as input:
        for match in finditer(r'^>.*$([^>]+)', input.read(), re.M | re.I):
            # Ištriname eilučių skirtukus
            sequence = match.group(1).replace('\n', '')
            sequences.append(sequence)
        frequencyMatrix = calculateFrequencies(sequences)
        consensus = findConsensus(len(sequences[0]), frequencyMatrix)
        print(consensus)


except FileNotFoundError:
    sys.exit("Įvesties failas neegzistuoja")

