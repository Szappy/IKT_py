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

# Kilépés éve szerinti lista
def kilep_list ():
    fej = False
    kilepes_eve = int(input("Adja meg a listázandó évet: "))
    for i in range(len(szotar_lista)):
        if szotar_lista[i]["INAKT_EV"] == kilepes_eve:
            if fej == False:
                fej_iras()
                fej = True
            egy_sor_iras(szotar_lista[i],i)
    if fej == False:
        print("Nincs ilyen évvel kapcsolatos adat.")

# Fizetes szerinti lista -tól-ig
def fizetes_list ():
    fej = False
    fizetes_kezd = int(input("Adja meg a fizetéstől értéket: "))
    fizetes_veg = int(input("Adja meg a fizetésig értéket: "))
    for i in range(len(szotar_lista)):
        if szotar_lista[i]["KIFIZETES"] >= fizetes_kezd and szotar_lista[i]["KIFIZETES"] <= fizetes_veg:
            if fej == False:
                fej_iras()
                fej = True
            egy_sor_iras(szotar_lista[i],i)
    if fej == False:
        print("Nincs ilyen összeggel kapcsolatos adat.")