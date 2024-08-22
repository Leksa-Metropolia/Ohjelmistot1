a = int(input("Anna luku: "))

for i in range(2, (a//2)+1):
    if (a % i == 0):
        print(a, "ei ole alkuluku")
        break
else:
    print(a, "on alkuluku")