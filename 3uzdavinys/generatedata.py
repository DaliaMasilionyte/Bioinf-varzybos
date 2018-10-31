#!/usr/bin/env python3
import random

QUESTIONS = 51

for i in range(1, QUESTIONS):
    # with open("./input/3uzdavinys_input{}/3uzdavinys_input{}.txt".format(i, i), 'r') as inputFile:
    #     firstSequence = inputFile.readline()
    #     secondSequence = inputFile.readline()
    #
    #     with open("./input/3uzdavinys_input{}/3uzdavinys_markovo_modelis.txt".format(i), 'r') as markovFile:
    #         markov = markovFile.readlines()

    with open("./output/3uzdavinys_output{}.txt".format(i), 'r') as answersInput:
        answer = answersInput.readline()

        outputFile = "./gift/3Auzdavinys_input.gift".format(i)

        with open(outputFile, 'a') as output:
            output.write("::Q_TIKIMYBES{}::".format(i))
            output.write("\n".encode('unicode_escape').decode("utf-8"))
            # output.write(firstSequence)
            # output.write("\n".encode('unicode_escape').decode("utf-8"))
            # output.write(secondSequence)
            # output.write("\n".encode('unicode_escape').decode("utf-8"))
            # for line in markov:
            #     output.write(line)
            #     output.write("\n".encode('unicode_escape').decode("utf-8"))
            output.write("\n\n{=" + answer.strip() +"}\n\n")
            # output.write(answer + "}\n\n")
