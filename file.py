szotar_lista = []

def filebe (file_nev):
    szotar_lista = []
    i = 0
    with open(file_nev,"r", encoding="utf-8") as f:
        sor=f.readline().split()
        while sor != "/n":
            adat=sor.strip().split(";")

            szotar={}
            szotar["NEV"] = adat[0]
            szotar["SZULETESI_EV"] = int(adat[1])
            szotar["KIFIZETES"] = int(adat[2])
            szotar["STATUSZ"] = adat[3]
            szotar["START_EV"] = int(adat[4])
            szotar["INAKT_EV"] = int(adat[5])
            szotar_lista.append(szotar)
            
            sor=f.readline().split()

def fileki (file_nev):
    with open(file_nev,"w", encoding="utf-8") as f:
        for i in range(len(szotar_lista)):
            f.write(szotar_lista[i]["NEV"] + ";" + str(szotar_lista[i]["SZULETESI_EV"]) + ";" + str(szotar_lista[i]["KIFIZETES"]) + ";" + szotar_lista[i]["STATUSZ"] + ";" + str(szotar_lista[i]["START_EV"]) + ";" + str(szotar_lista[i]["INAKT_EV"]) + "\n")
