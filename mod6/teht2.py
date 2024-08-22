import random

def arpa(i):
    a = random.randint(1, i)
    return a

i = int(input("Anna nopan tahkojen määrä: "))
l = 0

while l != i:
    l = arpa(i)
    print(l)