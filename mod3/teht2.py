sy = input("Anna laivan hyttiluokka\n")
if sy == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif sy == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif sy == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif sy == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")