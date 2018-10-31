#!/bin/sh
# Skriptas gauti visų įvesčių rezultatus
for i in {1..50}
do
	python3 9uzdavinys.py ./input/9uzdavinys_input${i}.fa ./output/9uzdavinys_output${i}.txt
done
exit 0