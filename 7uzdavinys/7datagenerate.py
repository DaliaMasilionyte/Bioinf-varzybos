#!/usr/bin/env python3
import random

NUMBER = 1


def DNA(length):
    return ''.join(random.choice('CGTA') for _ in range(length))


for file in range(50):
    outputFile = "./input/7uzdavinys_input{}.txt".format(NUMBER)
    sequenceLength = random.randint(200, 1000)
    for seq in range(random.randint(5, 10)):
        sequence = DNA(sequenceLength)
        with open(outputFile, 'a') as output:
            output.write("> Sequence {}\n".format(random.randint(1000, 9999)))
            output.write(sequence + "\n")

    NUMBER += 1
