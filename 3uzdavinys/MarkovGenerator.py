#!/usr/bin/env python3

# Kodas, skirtas generuoti skirtingus Markovo modelius
# Markovo tikimybių modelis bus teikiamas kaip vienas iš duomenų failų

import random
import sys


try:
    if len(sys.argv) == 2:
        fileName = sys.argv[1]
    else:
        raise TypeError
except:
    sys.exit ('Reikia įvesti išvesties failo pavadinimą')


# Funkcija, kuri sukuria atsitiktines tikimybes kiekvienos bazės pasiketiimui
def createMarkovChain():
    markovChain = {}
    for nucleotide in "ATGC":
        slices = sorted(
            [0] + [random.random() for i in range(3)] + [1])
        transitionProbabilities = [slices[i+1] - slices[i] for i in range(4)]
        markovChain[nucleotide] = {base: p for base, p
                                   in zip ('ATGC', transitionProbabilities)}
    return markovChain

# Sanity check: patikrinimas ar tikimybės sumuojasi į 1
def checkTransitionProbabilities(markovChain):
    for nucleotide in "ATGC":
        probSum = sum(markovChain[nucleotide][base] for base in "ATGC")
        if probSum-1 != 0:
            raise ValueError("Klaidinga suma: {} bazei {}".format(probSum, nucleotide))
    return True

markov = createMarkovChain()

if checkTransitionProbabilities(markov):
    with open(fileName, 'w') as markovFile:
        for base in markov:
            markovFile.write('{}: '.format(base))
            for transition in markov[base]:
                markovFile.write('{}:{} '.format(transition, markov[base][transition]))
            markovFile.write('\n')