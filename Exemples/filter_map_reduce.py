listeEntier = [56, 2, 78, 989, 34, 16, 52]


def get_entier_inferieur_cinquante(valeur):
    return valeur < 50


# filter renvoie un générateur
generateur = filter(get_entier_inferieur_cinquante, listeEntier)
for val in generateur:
    print(val)
listeFiltree = list(filter(get_entier_inferieur_cinquante, listeEntier))
for val in listeFiltree:
    print(val)

# equivalent avec une compréhension de Liste
listeFiltree = [val for val in listeEntier if val < 50]
for val in listeFiltree:
    print(f"ma valeur : {val}")


def cube(x):
    return x ** 3

newList = list(map(cube, listeEntier))
for elem in newList:
    print(elem)

newList = [cube(x) for x in listeEntier]
for elem in newList:
    print(elem)
