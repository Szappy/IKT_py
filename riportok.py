def legidosebb(szotar):
    legidosebb = 0
    for i in range(len(szotar)):
        if szotar[i]["SZULETESI_EV"] > szotar[legidosebb]["SZULETESI_EV"]:
            legidosebb = i
    return szotar[legidosebb]

def legfiatalabb(szotar):
    legfiatalabb = 0
    for i in range(len(szotar)):
        if szotar[i]["SZULETESI_EV"] < szotar[legfiatalabb]["SZULETESI_EV"]:
            legfiatalabb = i
    return szotar[legfiatalabb]

def hany_aktiv(szotar):
    aktiv_db = 0
    for i in range(len(szotar)):
        if szotar[i]["STATUSZ"] == "AKTÍV":
            aktiv_db += 1
    return aktiv_db

def hany_inaktiv(szotar):
    inaktiv_db = 0
    for i in range(len(szotar)):
        if szotar[i]["STATUSZ"] == "INAKTÍV":
            inaktiv_db += 1
    return inaktiv_db