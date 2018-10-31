#!/bin/sh
# Skriptas gauti visų įvesčių rezultatus
for i in {1..50}
do
	python3 2uzdavinys.py ./input/2uzdavinys_input${i}.fa ./output2/2uzdavinys_output${i}.txt
done
exit 0