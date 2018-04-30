#!/bin/sh
# Skriptas gauti visų įvesčių rezultatus
for i in {1..50}
do
	python3 4uzdavinys.py ./input/4uzdavinys_input${i}.fa ./output/4uzdavinys_output${i}.txt
done
exit 0