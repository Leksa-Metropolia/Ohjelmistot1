import random

nimet = []

def format(a):
    a = a.lower()
    a = a.capitalize()
    return a

while True:
    nimi = input("Anna nimi: ")
    nimi = format(nimi)
    if nimi == "":
        break
    elif nimet.count(nimi) == 0:
        nimet.append(nimi)
        print("Uusi nimi")
    else:
        print("Aiemmin syötetty nimi")

random.shuffle(nimet)

for i in nimet:
    print(i)