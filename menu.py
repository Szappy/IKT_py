import riportok



def menu_karbantartas(szotar):
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




def menu_riportok(szotar):
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
                print("A legídősebb alkalmazott: " + riportok.legidosebb(szotar))
            case "2":
                print("A legfiatalabb alkalmazott: " + riportok.legfiatalabb(szotar))
            case "3":
                print("Az aktív dolgozók száma: " + riportok.hany_aktiv(szotar))
            case "4":
                print("Az inaktív dolgozók száma: " + riportok.hany_inaktiv(szotar))
            case "5":
                print("Az összes kifizetés havonta: " + riportok.osszes_kifizetes(szotar))
            case "6":
                print(f"Az átlag fizetés havonta: {riportok.atlag(szotar)}")
            







def menu_kereses (szotar):
    menube = ""
    while menube != "4":
        print("Alkalmazott karbantartó rendszer")
        print("Kérem válasszon az alábbi menüpontok közül!")
        print("1. Belépés éve szerinti lista")
        print("2. Kilépés éve szerinti lista")
        print("3. Fizetés szerinti lista -tól-ig")
        print("4. Vissza")
        menube = input("Kérem válasszon: ")




def fomenu (szotar):
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


            case "2":
                menu_riportok(szotar)
