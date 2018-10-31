#!/usr/bin/env python3
import random
QUESTIONS = 51

for i in range(1, QUESTIONS):
	# with open("./input/1uzdavinys_input{}.fa".format(i), 'r') as inputFile:
	# 	header = inputFile.readline()
	# 	sequence = inputFile.readlines()

	with open("./output2/1uzdavinys_output{}.txt".format(i), 'r') as answersInput:
		answer = answersInput.readline()

		outputFile = "./gift/1uzdavinys_input.gift".format(i)

		with open (outputFile, 'a') as output:
			output.write("::Q_TRANSLIACIJA{}::".format(i))
			output.write("\n".encode('unicode_escape').decode("utf-8"))
			output.write("\n\n")
			# for element in sequence:
			# 	output.write(element.strip() + " ")
			output.write("{=" + answer.strip() + "}\n\n")
			# output.write(element.strip() + " ")
            #
			# output.write("\n\n")
