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

# Transkripcija iš matricinės DNR į iRNR
def transcription(templateDNA):
    mRNA = ''
    complement = {'A': 'U',
                  'T': 'A',
                  'G': 'C',
                  'C': 'G'}
    for nucleotide in templateDNA:
        mRNA = mRNA + complement[nucleotide]
    return mRNA

# Rasti būsimo transkripto poziciją sekoje
# Tam, kad rasti visas koduojamas aminorūgštis
def nextTranscript(mRNA, currentPos):
    stopCodons = ['UAA', 'UAG', 'UGA']
    startPos = mRNA.find("AUG", currentPos)
    # Jei pradžios kodonas nerastas, tuomet startPos = -1
    for pos in range(startPos, len(mRNA), 3):
        if mRNA[pos:pos+3] in stopCodons:
            return startPos, pos
    return startPos, -1

# Transliacija iš iRNR į aminorūgščių seką
def translation(mRNA, start, end):
    aminoAcidSeq = ''
    codons = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
              "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
              "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
              "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
              "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
              "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
              "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
              "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
              "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
              "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
              "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
              "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
              "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
              "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
              "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
              "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

    for i in range(start, end, 3):
        aminoAcid = mRNA[i:i+3]
        aminoAcidSeq = aminoAcidSeq + codons[aminoAcid]
    return aminoAcidSeq

# Funkcija skirta įrašyti eilutę į failą
def writeToFile(string):
    with open (outputFile, 'a') as output:
        output.write (string)
        output.write ('\n')

try:
    with open (inputFile, 'r', encoding='utf-8') as input:
        # group 1 - seka
        # Taip galime rasti daugiau nei vieną fasta įrašą faile
        for match in finditer (r'^>.*$([^>]+)', input.read(), re.M | re.I):
            # Ištriname eilučių skirtukus
            # Seką verčiame į didžiąsias raides (uppercase),
            # Nes sąlygoje nenurodyta ar pateikiama tik didžiosiomis
            sequence = match.group(1).replace('\n', '').upper()
            # Kadangi matricinė DNR yra skaitoma 3' - 5'
            # Seką turime apsukti atvirkščiai (reverse)
            sequence = sequence[::-1]
            mRNA = transcription(sequence)
            currentPos = 0
            while 1:
                start, end = nextTranscript(mRNA, currentPos)
                # Jeigu starto arba stop kodonai nerasti
                if start == -1 | end == -1: 
                    break
                aminoAcidSeq = translation(mRNA, start, end)
                currentPos = end
                writeToFile(aminoAcidSeq)
except FileNotFoundError:
    sys.exit ("Įvesties failas neegzistuoja")
