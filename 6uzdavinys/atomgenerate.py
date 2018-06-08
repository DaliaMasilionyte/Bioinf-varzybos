#!/usr/bin/env python3

# Kodas kurti duomenims
import random
NUMBER = 1

def randomFloat():
	return float("{0:.2f}".format(random.uniform(-100, 100)))
def randomWhitespace():
	return " " * random.randint(1,5)

for files in range(50):
	outputFile = "./input/6uzdavinys_input{}.txt".format(NUMBER)
	for i in range( random.randint(20, 200)):
		x = randomFloat()
		y = randomFloat()
		z = randomFloat()

		with open (outputFile, 'a') as output:
		    output.write("ATOM{}{}{}{}{}{}\n".format(randomWhitespace(), x, 
		    	randomWhitespace(), y, randomWhitespace(), z))
	NUMBER += 1