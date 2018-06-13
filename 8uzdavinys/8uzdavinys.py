#!/usr/bin/env python3

import sys

try:
    if len (sys.argv) == 3:
        inputFile = sys.argv[1]
        outputFile = sys.argv[2]
    else:
        raise TypeError
except:
    sys.exit ('Reikia įvesti dviejų failų pavadinimus')

def countProbability(homozygDominant, heterozyg, homozygRec):
    population = homozygDominant + heterozyg + homozygRec
    # Lengviau skaičiuoti recesyvinio geno pasireiškimą

    # Dviejų homozigotinių recesyvinių organizmų poravimosi tikimybė
    recessiveMatingProb = (homozygRec/population) * \
                          ((homozygRec - 1)/(population - 1))
    # Dviejų heterozigotinių organizmų poravimosi tikimybė
    heteroMatingProb = (heterozyg/population) * \
                       ((heterozyg - 1)/(population - 1))
    # Heterozigotinio ir homozogotinio organizmų poravimosi tikimybė
    heteroRecessiveProb = (heterozyg/population) * \
                          (homozygRec/(population - 1)) + \
                          (homozygRec/population) * (heterozyg/(population - 1))

    # Dominantinio alelio tikimybę gauname atėmę suskaičiuotas tikimybes iš 1
    dominantAlleleProb = 1 - (recessiveMatingProb + heteroMatingProb * 1/4 +
                              heteroRecessiveProb * 1/2)

    return str(dominantAlleleProb)


with open(inputFile, 'r') as inputFile:
    homozygDominant, heterozyg, homozygRec = inputFile.readline().split()
    homozygDominant = float(homozygDominant)
    heterozyg = float(heterozyg)
    homozygRec = float(homozygRec)


with open(outputFile, 'w') as output:
    output.write(countProbability(homozygDominant, heterozyg, homozygRec))


