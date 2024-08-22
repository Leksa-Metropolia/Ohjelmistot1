import random

i = int(input("Kuinka monta arpakuutuiota heitetään?\n"))
for j in range(0,i):
    a = random.randint(1, 6)
    print(str(j+1) + ". arpakuution silmäluku on: " + str(a))