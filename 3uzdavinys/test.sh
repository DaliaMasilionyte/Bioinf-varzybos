#!/bin/sh
# Skriptas gauti visų įvesčių rezultatus
for i in {1..50}
do
	python3 3uzdavinys.py ./input/3uzdavinys_input${i}/3uzdavinys_markovo_modelis.txt ./input/3uzdavinys_input${i}/3uzdavinys_input${i}.txt ./output/3uzdavinys_output${i}.txt
done
exit 0