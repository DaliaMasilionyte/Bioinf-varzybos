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

with open(inputFile, 'r') as inputFile:
    arguments = inputFile.readline()
    fragmentLength, numOfFragments = arguments.split()
    fragmentLength = int(fragmentLength)
    numOfFragments = int(numOfFragments)
    # Sąlygoje nurodyta, kad seka pateikta vienoje eilutėje
    sequence = inputFile.readline()
    sequence = sequence.replace('\n', '')

for i in range(len(sequence)):
	first = sequence[i:i+fragmentLength]
	counter = 1
	for j in range(1, numOfFragments+1):
		if(sequence[i+(fragmentLength*j):i+(fragmentLength*(j+1))] == first):
			counter += 1
	if counter == numOfFragments:
		cutPosistion = i+fragmentLength
		continuePosition = i+(fragmentLength*numOfFragments)

newSequence = "{}{}".format(sequence[:cutPosistion], sequence[continuePosition:])
print(newSequence)