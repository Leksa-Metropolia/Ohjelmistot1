a = []
while True:
    i = input("Anna luku: ")
    if i == "":
        a.sort()
        print(f"Suurin syötetty luku on {a[len(a)-1]} ja pienin {a[0]}")
        break
    a.append(int(i))