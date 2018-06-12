#!/bin/sh
# Skriptas gauti visų įvesčių rezultatus
for i in {1..50}
do
	python3 7uzdavinys.py ./input/7uzdavinys_input${i}.txt ./output/7uzdavinys_output${i}.txt
done
exit 0