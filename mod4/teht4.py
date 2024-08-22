import random
a = random.randint(1, 10)
i = int(0)
while a != i:
    i = int(input("Arvaa luku "))
    if i < a :
        print("Liian pieni arvaus")
    elif i > a :
        print("Liian suuri arvaus")
    else:
        print("Oikein")