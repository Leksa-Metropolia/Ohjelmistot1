from random import randint
import numpy as np

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

class Kilpailu:
    def __init__(self, nimi, pituus, autolista):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autolista

    def tunti_kuluu(self):
        for car in self.autot:
            car.kiihdyta(randint(-10, 15))
            car.kulje(1)

    def tulosta_tilanne(self):
        for car in self.autot:
            auto = [car.rekisteri, car.mSpeed, car.cSpeed, car.dist]
            print(auto)

    def kilpailu_ohi(self):
        for car in self.autot:
            if car.dist >= self.pituus:
                return True
        return False

autot = []
i = 1
while i <= 10:
    autot.append(Auto(f"ABC-{int(i)}", randint(100, 200)))
    i += 1

kisa = Kilpailu("Suuri romuralli", 8000, autot)
while kisa.kilpailu_ohi() == False:
    for i in range(10):
        kisa.tunti_kuluu()
        if kisa.kilpailu_ohi() == True:
            break
    kisa.tulosta_tilanne()