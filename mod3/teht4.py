v = input("Anna vuosiluku: ")
v = int(v)
if v % 4 == 0 and v % 400 != 0:
    print(str (v) + " on karkausvuosi")
else:
    print(str(v) + " ei ole karkausvuosi")