#!/bin/sh
# Skriptas gauti visų įvesčių rezultatus
for i in {1..50}
do
	python3 6.py ./input/6uzdavinys_input${i}.txt ./output/6uzdavinys_output${i}.txt
done
exit 0