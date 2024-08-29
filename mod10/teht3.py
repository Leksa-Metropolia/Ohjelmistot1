class Hissi:
    def __init__(self, alin, ylin):
        self.k_alin = alin
        self.k_ylin = ylin
        self.kerros = self.k_alin

    def kerros_ylos(self):
        if self.kerros < self.k_ylin:
            self.kerros += 1
            print(self.kerros)

    def kerros_alas(self):
        if self.kerros > self.k_alin:
            self.kerros -= 1
            print(self.kerros)

    def siirry_kerrokseen(self, kerros):
        if kerros < self.kerros:
            i = self.kerros - kerros
            for a in range(i):
                self.kerros_alas()
        elif kerros > self.kerros:
            i = kerros - self.kerros
            for a in range(i):
                self.kerros_ylos()

class Talo:
    def __init__(self, kalin, kylin, hissit):
        self.k_alin = kalin
        self.k_ylin = kylin
        self.hissit = []
        for hissi in range(hissit):
            h = Hissi(self.k_alin, self.k_ylin)
            self.hissit.append(h)

    def aja_hissia(self, hissi, kerros):
        self.hissit[hissi-1].siirry_kerrokseen(kerros)

    def palohalytys(self):
        for hissi in range(len(self.hissit)):
            self.aja_hissia(hissi, self.k_alin)

talo = Talo(1, 4, 2)
talo.aja_hissia(1, 4)
talo.aja_hissia(2, 3)
talo.palohalytys()