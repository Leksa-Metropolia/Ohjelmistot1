import mysql.connector

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='leksa',
         password='tapani',
         autocommit=True
         )

icao = input("Anna haettavan lentokentän ICAO-koodi\n")
icao.upper()
sql = f"SELECT ident, name FROM airport WHERE ident = '{icao}'"
kurs = yhteys.cursor()
kurs.execute(sql)
tks = kurs.fetchall()
for t in tks:
    print(t[1])