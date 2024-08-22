def gl(i):
    a = i*3.785
    return a

while True:
    i = int(input("Anna gallonoja muutettavaksi litroiksi: "))
    if i < 0:
        break
    else:
        print(gl(i))