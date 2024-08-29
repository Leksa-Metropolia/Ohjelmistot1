import random

N = int(input("Anna testattavien lukujen määrä: "))
n = 0
i =0
while i < N:
    i += 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1

likipi = 4*n/N
print(f"Saadaan piin likiarvoksi: {likipi}")