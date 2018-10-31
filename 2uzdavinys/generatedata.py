#!/usr/bin/env python3
import random

QUESTIONS = 51

for i in range(1, QUESTIONS):
    # with open("./input/2uzdavinys_input{}.fa".format(i), 'r') as inputFile:
    #     header = inputFile.readline()
    #     sequence = inputFile.readlines()

    with open("./output2/2uzdavinys_output{}.txt".format(i), 'r') as answersInput:
        answer = answersInput.readline()
        # answers[-1] = "{}}}".format(answers[-1].strip())

        outputFile = "./gift/2buzdavinys_input.gift".format(i)

        with open(outputFile, 'a') as output:
            output.write("::Q_RESTRIKCIJA{}::".format(i))
            # output.write("> Sequence {}\n".format(random.randint(1000, 9999)))
            output.write("\n".encode('unicode_escape').decode("utf-8"))
            output.write("\n\n")
            # for element in sequence:
            #     output.write(element.strip() + " ")
            output.write("{=" + answer.strip() +"}\n\n")
            # for element in answers:
            #     output.write(element.strip() + "\n".encode('unicode_escape').decode("utf-8"))
            #
            # output.write("\n\n")
