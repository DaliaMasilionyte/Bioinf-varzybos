## 2. Restrikcijos vietos DNR sekoje

Rasti restrikcijos vietas duotoje DNR sekoje.  
Restrikcijos vietos yra pozicijos, kuriose fermentas perkerpa DNR seką. Paprastai jie yra atpažįstami pagal trumpus, specifinius motyvus.

Šiame uždavinyje ieškosime restrikcijos vietų endonukleazei **MslI**.  
**MslI** atpažinimo seka 5' -> 3' kryptimi yra **CAYNNˆNNRTG**.  
*R reiškia A arba G, Y - C arba T, N - A arba T, arba C, arba G.  
Likę nukleotidų [kodai](https://www.bioinformatics.org/sms/iupac.html)*  
*'^' simbolis nurodo kirpimo vietą. Pozicija skaičiuojama bazės, esančios už simbolio.*    

**Svarbu: Biologams, ne taip kaip kitiems informatikams, pirmas sekos nukleotidas yra pozicijoje 1, o ne 0.**     
**Svarbu: Sekos gali būti pateiktos tiek mažosiomis, tiek didžiosiomis raidėmis.**

**Duota:** DNR grandinė 5' -> 3' kryptimi FASTA formatu iki 10000 bazių ilgio.  
**Gauti:** Restrikcijos vietos duotojoje sekoje atskirtos vienetiniais tarpais; naujoje eilutėje skaičius kiek iš viso buvo rasta restrikcijos vietų    

**Užuomina: Uždavinį padės išspręsti [reguliarios išraiškos](https://docs.python.org/3/library/re.html)**

### Pavyzdys  


**Duomenys:**
```FASTA
>seq
CGGgCATACcCGTGCAtAGCCGTG
```
**Rezultatas:**
```
10 20 
2
```






