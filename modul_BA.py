import random

class SorsoloOsztaly_BA:
    def __init__(self, lista):
        self.lista = lista

    def keveres(self):
        random.shuffle(self.lista)
        return self.lista

def adat_formazas_BA(adat_nev, adat_ertek):
    if adat_ertek == "":
        return f"{adat_nev}: Nincs adat"
    else:
        return f"{adat_nev.upper()}: {adat_ertek}"
