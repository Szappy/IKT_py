from lista import *

# Elsődleges kulcs szerinti keresés
def pri_keres (nev, szev):
    search_nev = nev
    search_szev = szev
    for i in range(len(szotar_lista)):
        if szotar_lista[i]["NEV"].casefold() == search_nev.casefold() and szotar_lista[i]["SZULETESI_EV"] == search_szev:
            return i
    return None

    # Belépés éve szerinti lista
def belep_list ():
    fej = False
    belepes_eve = int(input("Adja meg a listázandó évet: "))
    for i in range(len(szotar_lista)):
        if szotar_lista[i]["START_EV"] == belepes_eve:
            if fej == False:
                fej_iras()
                fej = True
            egy_sor_iras(szotar_lista[i],i)
    if fej == False:
        print("Nincs ilyen évvel kapcsolatos adat.")