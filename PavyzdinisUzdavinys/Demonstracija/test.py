#!/usr/bin/env python3

sequence = "GGGGAATACTTTGATGAGCCTCGCTCAGAGATTCGTTGTATACTATATTGGTACCCCCACCTATTCCTTGATAAAGAAGGCGGTACAGTCCACGTGGTCAGCGAATTGTTTCAGCTTTCGCCGACGATAACCTATTAGTCAGTTGGATGTCTCAGAAAATCACCTGACCGGAGGCCCACGAAGGTAGGCTGCTAAGTAGAGCAACCTAAGCAATTAGGCTAATCCGCGTCCGCGACTCGACGCTGACGCGCAGCTAGGCATAAGGATTGGCCGGTTTTAGCCAAACGTAAACTTAGGACGACCCAATCCATAGGGTACGAGTGCCTTGATTTAAAGTCAGGTGAGGGAGGCCAAAGACGACTGGTGTTAGCGGTCACGCCGCGACTCCCCTTTCTACCGCCCACGTAATTCGTATACAGAAGGTATGAGTCTTATGACCTATGAAGTCCAAGGACGTATTAACAGTGTGGAAGCCGTCGTGCATACTGCGTTAGTGAAACCCGGGTTCGGGGAATCTATTCCATAGCACTACTATGCCAGGTTTCAGTTGTTGTCAACACCGTACAAGCAAAGACGAACTGCGTTCGCTAGCCCCTGCTTCGCTCTGGGCTACTGCGCTTTG"
GCcontent = 0

for nucleotide in sequence:
	if nucleotide in "GC":
		GCcontent += 1

with open("out", "w") as outputFile:
	outputFile.write(str(GCcontent))
