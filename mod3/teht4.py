v = input("Anna vuosiluku: ")
v = int(v)
if v % 100 == 0 and v % 400 != 0:
    print(str (v) + " ei ole karkausvuosi")
elif v % 4 == 0:
    print(str (v) + " on karkausvuosi")
else:
    print(int(v) + " ei ole karkausvuosi")