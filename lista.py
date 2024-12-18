from file import szotar_lista

# Fejléc kiírása
def fej_iras ():
    print(f"{'#':<3} {'Név':<40} {'Sz.év':>5} {'Fizetés':>15} {'Státusz':<7} {'St.év':>5} {'In.év':>5}")
    print("-"*86)

# Egy sor kiírása
def egy_sor_iras (sor, sorszam=None):
    # kifizetes formázása ezres választóval
    kifizetes = f"{sor['KIFIZETES']:,}"
    print(f"{sorszam:<3} {sor['NEV']:<40} {sor['SZULETESI_EV']:>5} {kifizetes:>15} {sor['STATUSZ']:<7} {sor['START_EV']:>5} {sor['INAKT_EV']:>5}")
    #print(sor)

# Összes rekord vagy megadott -tól -ig rekordok listázása 
def listazas (tol=None, ig=None):
    if tol == None:
        tol = 0
    if ig == None:
        ig = len(szotar_lista)

    # fejléc
    fej_iras()

    # Elemek kiírása
    for i in range(tol, ig):
        egy_sor_iras(szotar_lista[i], i+1)

# Összes rekord listázása 10-esével
def tizes_lista (karb=False, tol=None):
    inp = ""
    if tol == None:
        tol = 0
    else:
        i = tol
    
    while inp != "#":
        j = i+10
        if j >= len(szotar_lista):
            j = len(szotar_lista)

        listazas(i, j)
        i = j
        if i >= len(szotar_lista):
            i = 0
        
        if karb:
            print("Tovább=Enter, Kilépés=#")
            inp = input("Vagy adja meg a rekord sorszámát: --> ")
            if inp != "":
                return inp
        else:
            inp = input("Tovább=Enter, Kilépés=# --> ")
                
