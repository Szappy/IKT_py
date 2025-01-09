#Alkalmazott kezelő rendszer

##A Pythonban írt rendszer képes az alkalmazottak adatait eltárolni, azokon módosításokat végezni, valamint alapvető listákat készíteni az adatokból. A program karakteres felületű, a felhasználóval történő kommunikáció interaktív.

##Az alkalmazottak adatait CSV fájlba tárolja.
 
| Mező neve    | Mező típusa | Mező leírása                                                 |
|--------------|-------------|--------------------------------------------------------------|
| NEV          | Szöveges    | Alkalmazott neve                                             |
| SZULETESI_EV | Szám (int)  | Alkalmazott születési éve (ÉÉÉÉ formában)                    |
| KIFIZETES    | Szám (int)	 | Összes bruttó juttatás havonta                               |
| STATUSZ      | Szöveges	 | AKTÍV/INAKTÍV                                                |
| START_EV     | Szám (int)  | Alkalmazott munkába állásának az éve (ÉÉÉÉ formában)         |
| INAKT_EV     | Szám (int)  | Melyik évtől lett inaktív (ÉÉÉÉ formában).                   | 

##A felhasználói felület az alábbi menürendszerre épül:
1. Adatok karbantartása
	1. Felvitel
	2. Módosítás
	3. Törlés
	4. Aktiválás/inaktiválás
2. Riportok
	1. Legidősebb aktív alkalmazott
	2. Legfiatalabb aktív alkalmazott
	3. Hány aktív alkalmazott van
	4. Hány inaktív alkalmazott van
	5. Havi összes kifizetés
	6. Havi átlag kifizetés
3. Keresés, listázás
	1. Belépés éve szerinti lista
	2. Kilépés éve szerinti lista
	3. Fizetés szerinti lista (-tól-ig)

##Modul lista
| Modul neve      | Tartalma, leírása                                         |
|-----------------|-----------------------------------------------------------|
| alkalmazott.py  | A főprogram                                               |
| menu.py         | Menürendszer                                              |
| file.py         | CSV file olvasás/írás                                     |
| karbantartas.py | Felvitel, módosítás, törlés, aktiválás/inaktiválás        |
| kereses.py      | Keresés és listázás                                       |
| riportok.py     | Riportokat tartalmazó modul                               |
| lista.py        | Listázással kapcsolatos modul                             |
