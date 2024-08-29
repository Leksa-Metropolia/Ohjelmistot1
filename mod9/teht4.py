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

kisa = []
i = 1
while i <= 10:
    kisa.append(Auto(f"ABC-{int(i)}", randint(100, 200)))
    i += 1

kisaP = True
while kisaP:
    for car in kisa:
        car.kiihdyta(randint(-10, 15))
        car.kulje(1)
        if car.dist >= 10000:
            kisaP = False
            for car in kisa:
                auto = [car.rekisteri, car.mSpeed, car.cSpeed, car.dist]
                print(auto)