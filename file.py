def filebe (file_nev):
    szotar_lista = []
    with open(file_nev,"r", encoding="utf-8") as f:
        sorok=f.read().splitlines()
        for sor in sorok[1::]: #a 0. indexen lévő sort kihagyjuk
            adat=sor.strip().split(";")
            
            szotar={}
            szotar["nev"]=adat[0]
            szotar["db"]=int(adat[1])
            szotar["tipus"]=adat[2]
            szotar_lista.append(szotar)
    return szotar_lista
