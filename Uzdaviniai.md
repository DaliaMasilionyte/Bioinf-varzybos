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

    

## 3. Mutacijų tikimybių modelis

Mutacijų greitis tam tikroje pozicijoje priklauso nuo toje pozicijoje esančio nukleotido. Yra ne viena priežastis, kodėl stebimi mutacijų greičiai skiriasi tarp skirtingų bazių. Viena iš priežasčių yra ta, kad pakitimus generuoja skirtingi mechanizmai. Kita priežastis yra, kad gyvose ląstelėse vyksta sudėtingi reparacijos procesai ir jų efektyvumas skiriasi skirtingiems nukleotidams.    

Nukleotidų mutacijos gali būti modeliuojamos naudojant tikimybes, kad vienas nukleotidas pavirs kitu. Kiekvienas nukleotidas (A, C, T, G) gali su tikimybe x <= 1 mutuoti į bet kurį iš keturių nukleotidų. Visų mutacijų tikimybių suma yra lygi 1, nes nukleotidas būtinai arba lieka toks pats, arba virsta kitu nukleotidu.  
*Pvz: A išlieka A su tikimybe 0.4, A virsta T su tikimybe 0.2, A virsta C su tikimybe 0.1 A virsta G su tikimybe 0.3. Visų tikimybių suma = 1*    

Reikia apskaičiuoti, naudojant duotąjį tikimybių modelį, tikimybę, kad viena seka po vieno pasikeitimo taps antrąją seka.


**Duota:** Tikimybių modelio failas ir failas su dvejomis DNR sekomis atskirtomis eilutėmis    
**Gauti:** Tikimybę, kad po vienos mutacijos pirmojoje DNR sekoje, gausime antrąją DNR seką  

**Užuomina: Tikimybių modelį patogu laikyti [dictionary duomenų struktūroje](https://docs.python.org/3/tutorial/datastructures.html)**

### Pavyzdys  


**Duomenys:**
```
A: A:0.3007483394955144 T:0.20557909669932328 G:0.03903291725113445 C:0.4546396465540279 
T: A:0.41265952625443614 T:0.38327162606884846 G:0.03074573074826814 C:0.17332311692844726 
G: A:0.06208015320435245 T:0.6163819289398256 G:0.31550179107215826 C:0.00603612678366372 
C: A:0.04737690685949325 T:0.22490504000104827 G:0.6255117969755644 C:0.10220625616389412 

```

```
GAC
TCG
```
**Rezultatas:**
```
0.17528821066441308
```


    
Šaltiniai:  
*Langtangen, Hans Petter, 2009. A Primer on Scientific Programming with Python.*

## 4. Rasti motyvą DNR sekoje

Motyvas - tai trumpa, kelių nukleotidų seka, kuri gali dažnai kartotis DNR sekoje ir tikėtina, kad turi biologinę prasmę. Dažnai tai būna specifinės baltymų, tokių kaip nukleazės ar transkripcijos faktoriai, prisijungimo vietas. Kiti motyvai būna svarbūs RNR lygyje, susijusiame su ribosomų prisijungimu, informarcinės RNR apdorojimu ir transkripcijos terminacija.    

Šioje užduotyje reikia rasti duotojoje DNR sekoje dažniausiai pasikartojantį 6-merą (6 nukleotidų ilgio motyvą).  

**Duota:** DNR grandinė 5' -> 3' kryptimi FASTA formatu iki 10000 bazių ilgio.    
**Gauti:** Dažniausiai pasikartojantis 6 nukleotidų motyvas ir skaičius, kiek kartų motyvas sekoje pasikartojo. Gali būti daugiau nei vienas tiek pat kartų pasikartojantis motyvas, todėl jei jų yra daugiau informacija apie kiekvieną reikia pateikti skirtingose eilutėse.  


### Pavyzdys  

**Duomenys:**
```
> sequence
CTTGCCGTGCCCCAAATGACGTATGGCTTGCCAAATGATACTTGCCCCAAATG
```

**Rezultatas:**
```
CTTGCC 3
CCAAAT 3
CAAATG 3
```

## 5. Sekos fragmentų duplikatų šalinimas    

Laboratorijoje biochemikai [sekvenavo](https://en.wikipedia.org/wiki/DNA_sequencing) DNR seką, tačiau vienoje vietoje sekos fragmentas duplikavosi keletą kartų. Bioinformatikai gautus duomenis turi analizuoti, tačiau pradžioje juos reikia sutvarkyti. Jūsų užduotis rasti fragmentą, kuris dupikavosi ir iškirpti visus duplikatus, paliekant tik vieną nesikartojantį fragmentą sekoje. Jūs žinote, kokio ilgio (kiek nukleotidų) yra ieškomas fragmentas ir kiek kartų jis sekoje iš eilės pasikartoja.    

**Duota:** Pirmoje eilutėje: Skaičius **n** - ieškomo fragmento ilgis (iki 30 nukleotidų), skaičius **k** - fragmento pasikartojimų skaičius ne didesnis nei 20  
Antroje eilutėje DNR grandinė iki 1500 bazių ilgio.    

**Gauti:** DNR grandinė, su iškirptomis fragmento kopijomis    


### Pavyzdys  

**Duomenys:**
```
5 3
AGGTCGTAGCAGGACAGGACAGGACACTAGGCTAGCGGGAATGCG
```

**Rezultatas:**
```
AGGTCGTAGCAGGACACTAGGCTAGCGGGAATGCG
```

