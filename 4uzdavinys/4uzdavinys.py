#!/usr/bin/env python3
import sys
import re
from re import finditer

MOTIF_LENGTH = 6
motifs = {}

try:
    if len (sys.argv) == 3:
        inputFile = sys.argv[1]
        outputFile = sys.argv[2]
    else:
        raise TypeError
except:
    sys.exit ('Reikia įvesti dviejų failų pavadinimus')

try:
    with open (inputFile, 'r', encoding='utf-8') as input:
        # Taip galime rasti daugiau nei vieną fasta įrašą faile
        for match in finditer (r'^>.*$([^>]+)', input.read (), re.M | re.I):
            # Ištriname eilučių skirtukus
            sequence = match.group(1).replace('\n', '')
            # Ieškome visų 6 nukleotidų substringų
            for nucleotide in range (len (sequence) - MOTIF_LENGTH + 1):
                motif = sequence[nucleotide:nucleotide + MOTIF_LENGTH]
                if not motif in motifs:
                    motifs[motif] = 1
                else:
                    motifs[motif] += 1
            # Sukuriamas masyvas, 
            # kuriame saugomi dažniausiai pasikartojančių motyvų raktai
            allFrequentMax = [k for k, v in motifs.items() if v == max(motifs.values())]
            for item in allFrequentMax:
                with open(outputFile, 'w') as output:
                	output.write("{} {}".format (item, motifs[item]))

except FileNotFoundError:
    sys.exit ("Įvesties failas neegzistuoja")