sp = input("Syötä sukupuolesi\n")
hemo = input("Anna hemoglobiini arvosi\n")
if sp.lower() == "mies":
    if 134 >= int(hemo) <= 195:
        print("Hemoglobiini arvosi on normaali")
    elif int(hemo) > 195:
        print("Hemoglobiini arevosi on korkea")
    elif int(hemo) < 134:
        print("Hemoglobiini arvosi on matala")
elif sp.lower() == "nainen":
    if 117 >= int(hemo) <= 175:
        print("Hemoglobiini arvosi on normaali")
    elif int(hemo) > 175:
        print("Hemoglobiini arevosi on korkea")
    elif int(hemo) < 117:
        print("Hemoglobiini arvosi on matala")