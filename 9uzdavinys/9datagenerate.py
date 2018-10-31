#!/usr/bin/env python3
import random

transitions = {
    'A': 'G',
    'G': 'A',
    'C': 'T',
    'T': 'C'
}

transversions = {
    'A': 'CT',
    'C': 'AG',
    'G': 'TC',
    'T': 'GA'
}


def DNA(length):
    return ''.join(random.choice('CGTA') for _ in range(length))


for file in range(1, 51):
    outputFile = "./input/9uzdavinys_input{}.fa".format(file)
    sequenceLength = random.randint(200, 1000)
    sequence = DNA(sequenceLength)
    sequence2 = ""
    for i in range(sequenceLength):
        if i % 7 == 0:
            sequence2 += transitions[sequence[i]]
        elif i % 17 == 0:
            sequence2 += random.choice(transversions[sequence[i]])
        else:
            sequence2 += sequence[i]

    with open(outputFile, 'a') as output:
        output.write("> Sequence {}\n".format(random.randint(1000, 9999)))
        output.write(sequence + "\n")
        output.write("> Sequence {}\n".format(random.randint(1000, 9999)))
        output.write(sequence2 + "\n")
