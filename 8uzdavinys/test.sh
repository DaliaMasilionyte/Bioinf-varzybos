#!/bin/sh
# Skriptas gauti visų įvesčių rezultatus
for i in {1..50}
do
	python3 8uzdavinys.py ./input/8uzdavinys_input${i}.txt ./output/8uzdavinys_output${i}.txt
done
exit 0