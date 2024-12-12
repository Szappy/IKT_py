from file import szotar_lista

# Elsődleges kulcs szerinti keresés
def pri_keres (nev, szev):
    search_nev = nev
    search_szev = szev
    for i in range(len(szotar_lista)):
        if szotar_lista[i]["NEV"].casefold() == search_nev.casefold() and szotar_lista[i]["SZULETESI_EV"] == search_szev:
            return i
    return None