from file import szotar_lista

def legidosebb():
    legidosebb = 0
    for i in range(len(szotar_lista)):
        if szotar_lista[i]["SZULETESI_EV"] < szotar_lista[legidosebb]["SZULETESI_EV"]:
            legidosebb = i
    return szotar_lista[legidosebb]

def legfiatalabb():
    legfiatalabb = 0
    for i in range(len(szotar_lista)):
        if szotar_lista[i]["SZULETESI_EV"] > szotar_lista[legfiatalabb]["SZULETESI_EV"]:
            legfiatalabb = i
    return szotar_lista[legfiatalabb]

def hany_aktiv():
    aktiv_db = 0
    for i in range(len(szotar_lista)):
        if szotar_lista[i]["STATUSZ"] == "AKTÍV":
            aktiv_db += 1
    return aktiv_db

def hany_inaktiv():
    inaktiv_db = 0
    for i in range(len(szotar_lista)):
        if szotar_lista[i]["STATUSZ"] == "INAKTÍV":
            inaktiv_db += 1
    return inaktiv_db
def osszes_kifizetes():
    osszes = 0
    for i in range(len(szotar_lista)):
        osszes += szotar_lista[i]["KIFIZETES"]
    return osszes

def atlag_kifizetes():
    atlag = osszes_kifizetes(szotar_lista)/len(szotar_lista)
    return round(atlag, 2)