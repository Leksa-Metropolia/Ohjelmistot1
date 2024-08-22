mitta = input("Anna kuhan pituus:\n")
if int(mitta) < 37:
    print("Laske kuha takaisin järveen.")
    m = 37 - int(mitta)
    print("Kuha on " + str(m) + "cm liian lyhyt")