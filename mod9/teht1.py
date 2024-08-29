class Auto:
    def __init__(self, rekisteri, mSpeed):
        self.mSpeed = mSpeed
        self.rekisteri = rekisteri
        self.dist = 0
        self.cSpeed = 0

car = Auto("ABC-123", 142)
print(car.rekisteri)
print(car.mSpeed)
print(car.dist)
print(car.cSpeed)