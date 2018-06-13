#!/usr/bin/env python3
import random
NUMBER = 1
for file in range(50):
	outputFile = "./input/8uzdavinys_input{}.txt".format(NUMBER)
	a = random.randint(5,100)
	b = random.randint(5,100)
	c = random.randint(5,100)
	with open (outputFile, 'a') as output:
		output.write("{} {} {}".format(a, b, c))
	NUMBER += 1