while True:
    i = int(input("Anna tuumamitta: "))
    if i < 0:
        break
    cm = i * 2.54
    print("Mitta senttimetreinä: " + str(cm) + "cm")