import riportok
import karbantartas

def menu_karbantartas():
    menube = ""
    while menube != "5":
        print("Alkalmazott karbantartó rendszer")
        print("Kérem válasszon az alábbi menüpontok közül!")
        print("1. Felvitel")
        print("2. Módosítás")
        print("3. Törlés")
        print("4. Aktiválás/inaktiválás")
        print("5. Vissza")
        menube = input("Kérem válasszon: ")
        match menube:
            case "1": karbantartas.felvitel ()
            case "2": karbantartas.modositas ()
            case "3": karbantartas.torles ()
            case "4": karbantartas.aktinakt ()


def menu_riportok():
    menube = ""
    while menube != "7":
        print("Alkalmazott karbantartó rendszer")
        print("Kérem válasszon az alábbi menüpontok közül!")
        print("1. Legidősebb alkalmazott")
        print("2. Legfiatalabb alkalmazott")
        print("3. Hány aktív alkalmazott van")
        print("4. Hány inaktív alkalmazott van")
        print("5. Havi összes kifizetés")
        print("6. Havi átlag fizetés")
        print("7. Vissza")
        menube = input("Kérem válasszon: ")
        match menube:
            case "1":
                print("A legídősebb alkalmazott: " + str(riportok.legidosebb()))
            case "2":
                print("A legfiatalabb alkalmazott: " + str(riportok.legfiatalabb()))
            case "3":
                print("Az aktív dolgozók száma: " + str(riportok.hany_aktiv()))
            case "4":
                print("Az inaktív dolgozók száma: " + str(riportok.hany_inaktiv()))
            case "5":
                print("Az összes kifizetés havonta: " + str(riportok.osszes_kifizetes()))
            case "6":
                print("Az átlag fizetés havonta:" + str(riportok.atlag_kifizetes()))

def menu_kereses ():
    menube = ""
    while menube != "4":
        print("Alkalmazott karbantartó rendszer")
        print("Kérem válasszon az alábbi menüpontok közül!")
        print("1. Belépés éve szerinti lista")
        print("2. Kilépés éve szerinti lista")
        print("3. Fizetés szerinti lista -tól-ig")
        print("4. Vissza")
        menube = input("Kérem válasszon: ")

def fomenu ():
    menube = ""
    while menube != "4":
        print("Alkalmazott karbantartó rendszer")
        print("Kérem válasszon az alábbi menüpontok közül!")
        print("1. Adatok karbantartása")
        print("2. Riportok")
        print("3. Keresés, listázás")
        print("4. Kilépés")
        menube = input("Kérem válasszon: ")
        match menube:
            case "1":
                menu_karbantartas()
            case "2":
                menu_riportok()
