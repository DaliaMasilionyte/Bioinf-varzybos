#!/usr/bin/env python3
import random

QUESTIONS = 51

for i in range(1, QUESTIONS):
    # with open("./input/5uzdavinys_input{}.txt".format(i), 'r') as inputFile:
    #     firstLine = inputFile.readline() + "\n".encode('unicode_escape').decode("utf-8")
    #     sequence = inputFile.readline() + "\n".encode('unicode_escape').decode("utf-8")

    with open("./output/9uzdavinys_output{}.txt".format(i), 'r') as answersInput:
        answer = answersInput.readline()
        outputFile = "./gift/9uzdavinys_input.gift".format(i)

        with open(outputFile, 'a') as output:
            output.write("::Q_TASKINES_MUTACIJOS{}::".format(i))
            output.write("\n".encode('unicode_escape').decode("utf-8"))
            # output.write(firstLine)
            # output.write(sequence)
            output.write("\n\n{=" + answer + "}\n\n")
