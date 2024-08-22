kaudet = [
    ["tammikuu", "talvi"],
    ["helmikuu", "talvi"],
    ["maaliskuu", "kevät"],
    ["huhtikuu", "kevät"],
    ["toukokuu", "kevät"],
    ["kesäkuu", "kesä"],
    ["heinäkuu", "kesä"],
    ["elokuu", "kesä"],
    ["syyskuu", "syksy"],
    ["lokakuu", "syksy"],
    ["marraskuu", "syksy"],
    ["joulukuu", "talvi"]]

k = int(input("Anna kuukauden numero: "))-1

print(kaudet[k][1])
