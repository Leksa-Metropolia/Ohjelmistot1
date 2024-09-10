from flask import Flask, request
from mysql import connector

yhteys = connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='leksa',
         password='tapani',
         autocommit=True
         )

app = Flask(__name__)
@app.route('/kenttä/<icao>')
def kentt2(icao):
    icao.strip().upper()
    sql_request = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql_request)
    response = kursori.fetchall()
    for row in response:
        kentta_tiedot = {"ICAO": icao, "Name": row[0], "Municipality": row[1]}
        return kentta_tiedot

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)