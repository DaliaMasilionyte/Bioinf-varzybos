## 3. Markovo grandinės mutacijų tikimybių modelis

Mutacijų greitis tam tikroje pozicijoje priklauso nuo toje pozicijoje esančio nukleotido. Yra ne viena priežastis, kodėl stebimi mutacijų greičiai skiriasi tarp skirtingų bazių. Viena iš priežasčių yra ta, kad pakitimus generuoja skirtingi mechanizmai. Kita priežastis yra, kad gyvose ląstelėse vyksta sudėtingi reparacijos procesai ir jų efektyvumas skiriasi skirtingiems nukleotidams.    

Nukleotidų mutacijos gali būti modeliuojamos naudojant tikimybes, kad vienas nukleotidas pavirs kitu. Kiekvienas nukleotidas (A, C, T, G) gali su tikimybe x <= 1 mutuoti į bet kurį iš keturių nukleotidų. Visų mutacijų tikimybių suma yra lygi 1, nes nukleotidas būtinai arba lieka toks pats, arba virsta kitu nukleotidu.  
*Pvz: A išlieka A su tikimybe 0.4, A virsta T su tikimybe 0.2, A virsta C su tikimybe 0.1 A virsta G su tikimybe 0.3. Visų tikimybių suma = 1*    

Reikia apskaičiuoti, naudojant duotąjį Markovo tikimybių modelį, tikimybę, kad viena seka po vieno pasikeitimo taps antrąją seka.


**Duota:** Markovo tikimybių modelio failas ir failas su dvejomis DNR sekomis atskirtomis eilutėmis 
**Gauti:** Tikimybę, kad po vienos mutacijos pirmojoje DNR sekoje, gausime antrąją DNR seką  

**Užuomina: Markovo modelį patogu laikyti [dictionary duomenų struktūroje](https://docs.python.org/3/tutorial/datastructures.html)**

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
Langtangen, Hans Petter, 2009. A Primer on Scientific Programming with Python.

