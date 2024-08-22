k = "python"
s = "rules"
i = int(0)
while i < 5:
    ky = input("Käyttäjä: ")
    sy = input("Salasana: ")
    if k == ky and sy == sy:
        print("Tervetuloa")
        break
    else:
        print("Pääsy eveätty")
        i+=1