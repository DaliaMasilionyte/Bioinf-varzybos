#!/usr/bin/env python3
import sys
import re
from re import finditer

# Komandine eilute paduodami įvesties ir išvesties failai
try:
    if len(sys.argv) == 3:
        inputFile = sys.argv[1]
        outputFile = sys.argv[2]
    else:
        raise TypeError
except:
    sys.exit ('Reikia įvesti dviejų failų pavadinimus')  

# Suformuojama reguliari išraiška
# Kaip grupė išskiriamas restrikcijos vietos nukleotidas
MslI = '(?:CA[CT][AGTC][AGTC]([AGTC])[AGTC][AG]TG).*?'

# Funkcija, kuri randa restrikcijos vietą ir visą pozicijų kiekį
def findPosition(pattern, text):
    count = 0
    # Paiešką atliekame ignoruodami didžiąsias/mažąsias raides
    for match in finditer (pattern, text, re.IGNORECASE):
        count += 1
        # Pozicijas skaičiuojame nuo 1
        position = '{} '.format(match.start(1) + 1)
        writeToFile(position)
    writeToFile("\n")
    writeToFile(str(count))

# Funkcija kuri rašo į išvesties failą
def writeToFile(string):
    with open(outputFile, 'a') as output:
        output.write(string)

try:
    with open(inputFile, 'r', encoding = 'utf-8') as input:
        # Taip galime rasti daugiau nei vieną fasta įrašą faile
        for match in finditer (r'^>.*$([^>]+)', input.read(), re.M | re.I):
            # Ištriname eilučių skirtukus
            sequence = match.group(1).replace('\n', '')
            findPosition(MslI, sequence)
except FileNotFoundError:
    sys.exit("Įvesties failas neegzistuoja")
