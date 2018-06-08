#!/usr/bin/env python3

import random
NUMBER = 1

def DNA(length):
    return ''.join(random.choice('CGTA') for _ in range(length))

for file in range(50):
	outputFile = "./input/3uzdavinys_input{}/3uzdavinys_input{}.txt".format(NUMBER, NUMBER)

	sequenceLength = random.randint(3,8)

	sequence1 = DNA(sequenceLength)
	sequence2 = DNA(sequenceLength)
	fullOutput = "{}\n{}".format(sequence1, sequence2)

	with open (outputFile, 'a') as output:
		output.write(fullOutput)

	NUMBER += 1