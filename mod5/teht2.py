i = ""
a = list()

while True:
    i = int(input("Syötä luku: "))
    if i == "":
        break
    else:
        i = int(i)
        a.append(i)

a.sort(reverse=True)

for i in a[0:5]:
    print(i)