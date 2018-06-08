#!/usr/bin/env python3

import random
NUMBER = 1


def DNA(length):
    return ''.join(random.choice('CGTA') for _ in range(length))

for file in range(50):
	outputFile = "./input/5uzdavinys_input{}.txt".format(NUMBER)
	fragmentLength = random.randint(5,30)
	fragmentRepetitionNumber = random.randint(2,20)
	sequenceLength = random.randint(fragmentLength*fragmentRepetitionNumber+20,1500)
	fragment = DNA(fragmentLength) * fragmentRepetitionNumber
	startOfDNA = random.randint(3,fragmentLength)
	endOfDNA = sequenceLength - len(fragment) - startOfDNA

	fullSequence = "{}{}{}".format(DNA(startOfDNA), fragment,DNA(endOfDNA))
	fullOutput = "{} {}\n{}".format(fragmentLength, fragmentRepetitionNumber, fullSequence)
	with open (outputFile, 'a') as output:

		output.write(fullOutput)

	NUMBER += 1