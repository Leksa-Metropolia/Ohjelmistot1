class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kijailija, sivut):
        self.kirjailija = kijailija
        self.sivumaara = sivut
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(self.nimi)
        print(self.kirjailija)
        print(self.sivumaara)

class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        self.toimittaja = toimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(self.nimi)
        print(self.toimittaja)

akuankka = Lehti('Aku Ankka', 'Aki Hyyppä')
hytti6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
hytti6.tulosta_tiedot()
akuankka.tulosta_tiedot()