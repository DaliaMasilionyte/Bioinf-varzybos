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






