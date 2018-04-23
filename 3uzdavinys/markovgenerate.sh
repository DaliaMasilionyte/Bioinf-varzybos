#!/bin/sh
# Skriptas, kuris sugeneruoja 50 Markovo modelių
for i in {1..50}
do
	mkdir ./input/3uzdavinys_input${i}
	python3 MarkovGenerator.py ./input/3uzdavinys_input${i}/3uzdavinys_markovo_modelis.txt
done
exit 0