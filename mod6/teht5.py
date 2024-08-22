def karsi(i):
    b = []
    for a in i:
        if (a % 2) == 1:
            b.append(a)
    for c in b:
        i.remove(c)
    return i

i = [2, 1, 8, 5, 7, 1, 3, 6, 4]

print(karsi(i))