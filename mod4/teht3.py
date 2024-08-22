a = int(0)
while True:
    i = input("Anna luku: ")
    if i == "":
        print("Syötettyjen lukujen summa on: " + str(a))
        break
    a += int(i)