import random

def arpa():
    a = random.randint(1, 6)
    return a

i = 0

while i != 6:
    i = arpa()
    print(i)