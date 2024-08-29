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