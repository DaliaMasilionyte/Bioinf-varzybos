# Bioinformatikų užduotys su žvaigždute

## 1. Baltymų transliacija iš DNR sekos

DNR sekai virsti baltymų sekomis būtini du etapai:
1. Matricinės DNR transkripcija į iRNR. Atkreipkite dėmesį, kad transkripcija vyksta 3' - > 5' kryptimi.
2. Transliacija iš iRNR į aminorūgščių seką pagal genetinį kodą. (3 nukleotidai koduoja vieną aminorūgštį)

  
**Duota:** DNR grandinė 5' -> 3' kryptimi FASTA formatu iki 1500 bazių ilgio.  
**Gauti:** Baltymai (aminorūgščių sekos), kuriuos koduoja grandinė atskirtos eilutėmis  

*FASTA formatas - tekstinis failo formatas skirtas atvaizduoti nukleotidų arba aminorūgščių sekoms naudojant vienos raidės kodą.  
Kiekvienas įrašas yra sudarytas iš antraštės eilutės ir sekos eilučių.  
Antraštė prasideda '>' simboliu.   
Seka gali būti išdėstyta per daugiau nei vieną eilutę.   
Viename faile gali būti daug įrašų.*  

    
Uždavinyje naudojamas standartinis genetinis kodas.  
Egzistuoja ir kitokių [genetinių kodų](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi)

**Standartinio genetinio kodo aminorūgščių kodonai**
```Python3
kodonai = {
	"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
	"UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
	"UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
	"UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
	"CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
	"CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
	"CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
	"CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
	"AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
	"ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
	"AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
	"GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
	"GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
	"GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
	"GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
	    }
```

  
### Pavyzdys

**Duomenys:**
```FASTA
>seq1 
CGTAATTCAGAAGAGAGCCAATCAAATAGGGGTACGCTTAATATTAAAAAAATATTAGTA
ATTGTTTGTATGACGAATAAAATTTGTAAGCACCTGATCCAATCCTTATTATTGAGCAAG
AGACGTCTTGTTTCTGTACTCTTTGATAACTATCAAGGCGACATGAAACTAAGGTTACGC
GTTAATGGTGCTAATGCGTTTCATTCATCTCCATCTGCCATTCCTCTAGTTCCGTCAACG
AAAATTCTTCAAGCTATGGAGGCCCGGAACGACATTGTTGACAGTCTGATCATCAATAGT
CACGCAACGGAAAGTGATCGCCGGACTTTAGGAGACCATGAGGTTAGACAATGTGAGGAT
ACCAACTTCGGCTTCAAAATTTGA
```
**Rezultatas:**
```
MVS
MIRLSTMSFRASIA
MADGDE
MSP
```


     
## 2. Restrikcijos vietos DNR sekoje

Rasti restrikcijos vietas duotoje DNR sekoje.  
Restrikcijos vietos yra pozicijos, kuriose fermentas perkerpa DNR seką. Paprastai jie yra atpažįstami pagal trumpus, specifinius motyvus.

Šiame uždavinyje ieškosime restrikcijos vietų endonukleazėms **MslI, PpuMI, AvaI**.
*Nagrinėsime endonukleazes, kurios kerpa dvigubos grandinės DNR sekas.*
**MslI** atpažinimo seka 5' -> 3' kryptimi yra **CAYNNˆNNRTG**.
**PpuMI** atpažinimo seka 5' -> 3' kryptimi yra **RGˆGWCCY**.
**AvaI** atpažinimo seka 5' -> 3' kryptimi yra **C^YCGRG**.
*R reiškia A arba G, Y - C arba T, N - A arba T, arba C, arba G, W - A arba T.
Likę nukleotidų [kodai](https://www.neb.com/tools-and-resources/usage-guidelines/single-letter-codes)*
*'^' simbolis nurodo kirpimo vietą. Pozicija skaičiuojama bazės, esančios už simbolio.*    

**Svarbu: Biologams, ne taip kaip kitiems informatikams, pirmas sekos nukleotidas yra pozicijoje 1, o ne 0.**     
**Svarbu: Sekos gali būti pateiktos tiek mažosiomis, tiek didžiosiomis raidėmis.**

**Duota:** DNR grandinė 5' -> 3' kryptimi FASTA formatu iki 10000 bazių ilgio.  
**Gauti:** Restrikcijos vietos duotojoje sekoje atskirtos vienetiniais tarpais; naujoje eilutėje skaičius kiek iš viso buvo rasta restrikcijos vietų. Pirmiausiai nurodoma endonukleazės MslI atpažinimo vietos ir pozicijų skaičius, tada PpuMI ir galiausiai AvaI endonukleazės.

**Užuomina: Uždavinį padės išspręsti [reguliarios išraiškos](https://docs.python.org/3/library/re.html)**

### Pavyzdys  


**Duomenys:**
```FASTA
>seq
CGGgCATACcCGTGCAtAGCCGTGGGTCCTCGGG
AGCCGTGGGTCCTCGGG

AGCCGTGGGTCCTCGGG
```
**Rezultatas:**
```
10 20 
2
26 43 60
3
30 47 64
3

```






