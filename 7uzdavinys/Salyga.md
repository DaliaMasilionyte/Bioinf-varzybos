## 7. Labiausiai tikėtinas bendras protėvis

Turėdami keletą homologinių DNR sekų, norime surasti jų visų bendrą, labiausiai tikėtiną protėvio DNR seką.    
Visos sekos vienodo ilgio, užduotis yra rasti dažniausiai pasikartojantį nukleotidą tarp visų sekų kiekvienoje pozicijoje ir taip sudaryti naują DNR seką, kurią sudaro dažniausiai pasikartoję nukleotidai.    


*Jei sutampa dažniausio pasikartojamumo skaičius, negalime nustatyti kuris nukleotidas yra labiausiai tikėtinas protėvio sekoje, todėl tokias vietas pažymime **-** simboliu.*



*Homologinis - kilęs iš bendrų protėvių*


**Duota:** Iki 10 DNR grandinių 5' -> 3' kryptimi FASTA formatu iki 1000 bazių ilgio.    
**Gauti:** Labiausiai tikėtina protėvio DNR seka.


### Pavyzdys  

**Duomenys:**
```
> Sequence
ACCTGCCCACG
> Sequence
ATCAAGATCCG
> Sequence
CGGGGTGTATC
> Sequence
ACTTGGCTCTG
> Sequence
TCTGTGGCGCA
> Sequence
AGCGCTCCGGG
> Sequence
GGCACGCGGTT
> Sequence
TGGGTGTCGCG
```

**Rezultatas:**
```
AGCGGGCCGCG
```



