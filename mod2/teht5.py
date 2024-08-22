lei = input("Anna leiviskät.\n")
nau = input("Anna naulat.\n")
luo = input("Anna luodit.\n")
paino = ((int(lei)*20+int(nau))*32+float(luo))*13.3
grammat = paino % 1000
kilot = (paino - grammat) / 1000
print("Massa nykymittojen mukaan:\n" + str(int(kilot)) + " kilogrammaa ja " + str(round(grammat, 2)) + " grammaa.")