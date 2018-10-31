#!/usr/bin/env python3
import random
QUESTIONS = 50

for i in range(QUESTIONS):
	with open("/input/1uzdavinys_input{}.fa".format(i), 'r') as inputFile:
		header = inputFile.readline()
		sequence = inputFile.readlines()

		with open("/output/1uzdavinys_input{}.txt".format(i), 'r') as answersInput:
			answers = answersInput.readlines()


			outputFile = "./gift/1uzdavinys_input{}.gift".format(i)
			
			with open (outputFile, 'a') as output:
				output.write("::Q_TRANSLIACIJA{}::".format(i))
				output.write("> Sequence {}\n".format(random.randint(1000,9999)))
				output.write("-\n" + sequence + "\n")
				output.write("{=" + answers + "}\n\n")
			
