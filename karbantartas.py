from lista import *
import kereses

def felvitel ():
    inp = ""
    i = 0
    nev = ""
    szuletesi_ev = ""
    kifizetes = ""
    statusz = ""
    start_ev = 0
    inakt_ev = 0
    
    while inp != "#":
        print("Kilépéshez adja meg a # karaktert.")
        print("Kérem adja meg az alábbi adatokat.")
        inp = input("Alkalmazott neve: ")
        if inp == "#":
            break
        nev = inp
        inp = input("Alkalmazott születési éve: ")
        if inp == "#":
            break
        szuletesi_ev = int(inp)

        i = kereses.pri_keres(nev, szuletesi_ev)
        if i != None:
            print("Már van ilyen alkalmazott.")
            continue

        inp = input("Alkalmazott fizetése: ")
        if inp == "#":
            break
        kifizetes = int(inp)
        statusz = "AKTÍV"
        inp = input("Alkalmazott kezdő éve: ")
        if inp == "#":
            break
        start_ev = int(inp)
        szotar_lista.append ({"NEV":nev, "SZULETESI_EV":szuletesi_ev, "KIFIZETES":kifizetes, "STATUSZ":statusz, "START_EV":start_ev, "INAKT_EV":inakt_ev})
        print(f"A(z) {nev} alkalmazottat sikeresen felvettük.")
        print("---------------------------------")
        tizes_lista(False, len(szotar_lista)-1)

def modositas ():
    inp = ""
    i = 0
    kifizetes = ""
    start_ev = 0
    inakt_ev = 0

    while inp != "#":

        print("Kilépéshez adja meg a # karaktert.")
        # A szamok-ba betesszuk a jelenlegi 
        # rekordok szamsorait listában
        # [1,2,3,4,5,...,1000,...]
        szamok = list(range(1, len(szotar_lista)+1))
        inp = tizes_lista(True, i)
        # ha benne van a szam amit megadott, 
        # akkor az lesz a kivalasztott rekord,
        # egyébként kilépünk (vagy #-et adott, vagy 
        # olyan számot amivel nem létezik rekord).
        # Azért kell a -1, mert 1-től listáztunk
        if inp in str(szamok):
            i = int(inp)-1
        else:
            break

        print("Kérem adja meg az alábbi adatokat. Ha nem ad meg semmit, akkor az adat nem változik.")
        print(f"A(z) {szotar_lista[i]['NEV']}, {szotar_lista[i]['SZULETESI_EV']} alkalmazott módosítása!")

        inp = input(f"Kérem módosítsa a fizetést ({szotar_lista[i]['KIFIZETES']}): ")
        if inp == "#":
            break
        if inp != "":
            fizu = int(inp)
        else:
            fizu = szotar_lista[i]["KIFIZETES"]

        if szotar_lista[i]["STATUSZ"] == "AKTÍV":
            inp = input(f"Kérem módosítsa az alkalmazott kezdőévét({szotar_lista[i]['START_EV']}): ")
            if inp == "#":
                break
            if inp != "":
                start_ev = int(inp)
            else:
                start_ev = szotar_lista[i]["START_EV"]
        else:
            inp = input(f"Kérem módosítsa, hogy mely évtől lett inaktív ({szotar_lista[i]['INAKT_EV']}): ")
            if inp == "#":
                break
            if inp != "":
                inakt_ev = int(inp)
            else:
                inakt_ev = szotar_lista[i]["INAKT_EV"]

        szotar_lista[i]["KIFIZETES"] = fizu
        szotar_lista[i]["START_EV"] = start_ev
        szotar_lista[i]["INAKT_EV"] = inakt_ev
        print(f"A(z) {szotar_lista[i]['NEV']} alkalmazott adatai módosítva lettek.")
        print("---------------------------------")
        
def torles():
    inp = ""
    i = 0
    nev = ""
    while inp != "#":
        print("Kilépéshez adja meg a # karaktert.")
        szamok = list(range(1, len(szotar_lista)+1))
        inp = tizes_lista(True, i)
        if inp in str(szamok):
            i = int(inp)-1
        else:
            break
        nev = szotar_lista[i]["NEV"]
        inp = input(f"Biztos törli a(z) {szotar_lista[i]['NEV']}alkalmazottat? (IGEN/NEM):")
        if inp == "IGEN":
            del szotar_lista[i]
            print(f"A(z) {nev} alkalmazott adatai törölve.")
            print("--------------------------")

def aktinakt ():
    inp = ""
    i = 0

    while inp != "#":
        
        print("Kilépéshez adja meg a # karaktert.")
        # A szamokba betesszuk a jelenlegi 
        # rekordok szamsorait listában
        # [1,2,3,4,5,...,1000,...]
        szamok = list(range(1, len(szotar_lista)+1))
        inp = tizes_lista(True, i)
        # ha benne van a szam amit megadott, 
        # akkor az lesz a kivalasztott rekord,
        # egyébként kilépünk (vagy #-et adott, vagy 
        # olyan számot amivel nem létezik rekord)
        # azért kell a -1, mert 1-től listáztunk
        if inp in str(szamok):
            i = int(inp)-1
        else:
            break

        if szotar_lista[i]["STATUSZ"] == "AKTÍV":
            inp = input(f"Biztos inaktiválja a(z) {szotar_lista[i]['NEV']} alkalmazottat? (IGEN/NEM): ")
            if inp == "IGEN":
                inp = input(f"Milyen évtől legyen inaktív (Kezdés éve: {szotar_lista[i]['START_EV']}):")
                if inp == "#":
                    break
                if int(inp) < szotar_lista[i]["START_EV"]:
                    print("Nem lehet korábbi évtől inaktív.")
                else:
                    szotar_lista[i]["STATUSZ"] = "INAKTÍV"
                    szotar_lista[i]["INAKT_EV"] = int(inp)
                    print(f"A(z) {szotar_lista[i]['NEV']} alkalmazott inaktív státuszba lett téve.")
                    print("---------------------------------")
        else:
            inp = input(f"Biztos aktiválja a(z) {szotar_lista[i]['NEV']} alkalmazottat? (IGEN/NEM): ")
            if inp == "IGEN":
                    szotar_lista[i]["STATUSZ"] = "AKTÍV"
                    szotar_lista[i]["INAKT_EV"] = 0
                    print(f"A(z) {szotar_lista[i]['NEV']} alkalmazottat aktív státuszba helyeztük.")
                    print("---------------------------------")

            