import math

def arvo(d, h):
    r=d/2
    a=math.pi*r**2
    ls = a / h
    return ls

d1 = int(input("Anna ensimmäisen pitsan halkaisija: "))
h1 = int(input("Anna ensimmäisen pitsan hinta: "))
d2 = int(input("Anna toisen pitsan halkaisija: "))
h2 = int(input("Anna toisen pitsan hinta: "))

if arvo(d1, h1) < arvo(d2, h2):
    print("Toisella pitsalla on parempi hintalaatusuhde")
else:
    print("Ensimmäisellä pitsalla on parempi hintalaatusuhde")