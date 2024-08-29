class Auto:
    def __init__(self, rekisteri, mSpeed):
        self.mSpeed = mSpeed
        self.rekisteri = rekisteri
        self.dist = 0
        self.cSpeed = 0

    def kiihdyta(self, nopeus):
        if self.cSpeed + nopeus > self.mSpeed:
            self.cSpeed = self.mSpeed
        elif self.cSpeed + nopeus < 0:
            self.cSpeed = 0
        else:
            self.cSpeed = self.cSpeed + nopeus

    def kulje(self, time):
        self.dist += self.cSpeed * time

class Sahkoauto(Auto):
    def __init__(self, rekister, mSpeed, akku):
        super().__init__(rekister, mSpeed)
        self.akkukapasiteetti = akku

class Polttomoottoriauto(Auto):
    def __init__(self, rekister, mSpeed, tankki):
        super().__init__(rekister, mSpeed)
        self.bensatankki = tankki

sAuto = Sahkoauto("ABC-15", 180, 52.5)
bAuto = Polttomoottoriauto("ABC-15", 165, 32.3)
sAuto.kiihdyta(120)
sAuto.kulje(3)
bAuto.kiihdyta(135)
bAuto.kulje(3)
print(f"Sähköauto on ajanut: {sAuto.dist}")
print(f"Polttomoottoriauto on ajanut: {bAuto.dist}")
