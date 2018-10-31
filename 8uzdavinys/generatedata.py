#!/usr/bin/env python3
import random

QUESTIONS = 51

for i in range(1, QUESTIONS):
    with open("./input/8uzdavinys_input{}.txt".format(i), 'r') as inputFile:
        firstLine = inputFile.readline()
        # sequence = inputFile.readline() + "\n".encode('unicode_escape').decode("utf-8")

    with open("./output/8uzdavinys_output{}.txt".format(i), 'r') as answersInput:
        answer = answersInput.readline()
        outputFile = "./gift/8uzdavinys_input.gift".format(i)

        with open(outputFile, 'a') as output:
            output.write("::Q_PAVELDEJIMAS{}::".format(i))
            output.write("\n".encode('unicode_escape').decode("utf-8"))
            output.write(firstLine)
            # output.write(sequence)
            output.write("\n{=" + answer + "}\n\n")
