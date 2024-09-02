import random

i = int(input("Kuinka monta arpakuutuiota heitetään?\n"))
summa = 0
for j in range(0,i):
    a = random.randint(1, 6)
    summa += a
print(f"{i} heitetyn arpakuution summa on {summa}")