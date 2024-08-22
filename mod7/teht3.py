asemat = []

def format(a):
    a = a.lower()
    a = a.capitalize()
    return a

while True:
    s = input("Mitä tehtdään?\n"
              "syötä uusi lentoasema = U\n"
              "hae lentoasema = H\n"
              "lopeta = L\n")
    s = s.lower()
    if s == "l":
        break
    elif s == "u":
        asema = input("Syötä lentoaseman nimi: ")
        icao = input("Anna aseman ICAO-koodi: ")
        asema = format(asema)
        icao = icao.upper()
        i = [icao, asema]
        asemat.append(i)
    elif s == "h":
        icao = input("Anna haettavan aseman ICAO-koodi: ")
        icao = icao.upper()
        for i in asemat:
            if i[0] == icao:
                print(i[1])
                break
        else:
            print("Hakemaa asemaasi ei löydy")
    else:
        print("Tuntematon komento, syötä uusi")