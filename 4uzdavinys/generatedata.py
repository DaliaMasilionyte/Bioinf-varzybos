#!/usr/bin/env python3
import random

QUESTIONS = 51

for i in range(1, QUESTIONS):
    # with open("./input/4uzdavinys_input{}.fa".format(i), 'r') as inputFile:
    #     header = inputFile.readline()
    #     sequence = inputFile.readlines()

    with open("./output/4uzdavinys_output{}.txt".format(i), 'r') as answersInput:
        answer = answersInput.readline()
        outputFile = "./gift/4Auzdavinys_input.gift".format(i)

        with open(outputFile, 'a') as output:
            output.write("::Q_RASTI_MOTYVA{}::".format(i))
            # output.write("> Sequence {}\n".format(random.randint(1000, 9999)))
            output.write("\n".encode('unicode_escape').decode("utf-8"))
            # for line in sequence:
            #     output.write(line.strip())
            # output.write()
            output.write("\n\n{=" + answer.strip() +"}\n\n")

            # output.write("}\n\n")
