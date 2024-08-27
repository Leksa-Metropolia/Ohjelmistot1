import mysql.connector

def haku(list, element):
    for i in list:
        if i[0] == element:
            return list.index(i)

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='leksa',
         password='tapani',
         autocommit=True
         )

mk = input("Anna maakoodi: ")
mk.upper()
sql1 = f"SELECT iso_country, type FROM airport WHERE iso_country = '{mk}'"
sql2 = f"SELECT DISTINCT type FROM airport"
lista = []
kurs = yhteys.cursor()
kurs.execute(sql1)
tks = kurs.fetchall()
kurs.execute(sql2)
tl = kurs.fetchall()

for type in tl:
    lista.append([type[0], 0])

for type in tl:
    for row in tks:
        if row[1] == type[0]:
            p = haku(lista, type[0])
            lista[p][1] = lista[p][1] + 1

for type in lista:
    print(f"{type[0]}: {type[1]}")