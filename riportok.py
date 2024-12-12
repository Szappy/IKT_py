def legidosebb(szotar):
    legidosebb = 0
    for i in range(len(szotar)):
        if szotar[i]["SZULETESI_EV"] > szotar[legidosebb]["SZULETESI_EV"]:
            legidosebb = i
    return szotar[legidosebb]
