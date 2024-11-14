import alap_adatok
print("Kérem válasszom a menüből:")
print("1. CSV fájl feltölés")
print("2. Manuális feltöltés")
print("3. Keresés és listázás")
print("4. Elemek módosítása")
print("5. CSV fájl letöltése")
print("6. Kilépés")
menu = ""
while menu != "6":
    menu = input("->")
    match menu:
        case "1":
            alap_adatok.csv_feltoltes()
        case "2":
            alap_adatok.manuális_feltöltés()
        case "3":
            alap_adatok.kereses_listazas()
        case "4":
            alap_adatok.elemek_módosítása()
        case "5":
            alap_adatok.csv_letoles()
        case "6":
            print("Kilépés...")
        case _:
            print("Hiba! Kérem válassz egy érvényes menüt!")



#print("Szeretne új dolgozót hozzáadni? 0:Igen, 1:Nem")
#ujfelhasznalo=import()
#if