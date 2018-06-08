#!/bin/sh
# Skriptas gauti visų įvesčių rezultatus
for i in {1..50}
do
	python3 5uzdavinys.py ./input/5uzdavinys_input${i}.txt ./output/5uzdavinys_output${i}.txt
done
exit 0