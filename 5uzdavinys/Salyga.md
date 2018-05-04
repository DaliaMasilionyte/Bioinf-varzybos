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

