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

h = Hissi(2, 7)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(2)