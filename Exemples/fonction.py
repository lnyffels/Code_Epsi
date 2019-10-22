message = "Python c'est trop puissant"
print([(m.upper(), len(m)) for m in message.split(" ")])

lst = range(30)
print("Nouvelle liste :", [i for i in lst if i%2 == 0 ])

def ma_fonction(a, b, c):
    result = (a * b) / c
    e, d = str(result).split('.')
    return e, d

e, d = ma_fonction(76, 5, 7)
print(f"Partie entiere: {e} - Partie décimale: {d[:3]}")

def additionne(i, *args):
    somme = i
    print(args[0]) # 4
    for val in args:
        somme+=val
    return somme

somme = additionne(6,4,5,10)
print (somme)

def fonction(**kwargs):
    return kwargs['a'] + 2*kwargs["a"]*kwargs["b"] + kwargs["c"]   # a + 2ab + c

dico = {'a':3, 'b':4, 'c':2}
print(fonction(**dico))

def afficher_recette(nom, **kwargs):
    print(f"=== {nom} ===")
    for cle in kwargs:
        print(f"{cle} : {kwargs[cle]}")

ingredients_tiramisu = {"beurre": "100g","cafe": "10cl", "oeufs": 3}
afficher_recette("Tiramisu", **ingredients_tiramisu)