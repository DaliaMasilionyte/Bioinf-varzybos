#!/bin/sh
# Skriptas gauti visų įvesčių rezultatus
for i in {1..50}
do
	python3 1uzdavinys.py ./input/1uzdavinys_input${i}.fa ./output/1uzdavinys_output${i}.txt
done
exit 0