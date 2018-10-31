#!/usr/bin/env python3

sequence = ""
GCcontent = 0

for nucleotide in sequence:
	if nucleotide in "GC":
		GCcontent += 1

print(GCcontent)
