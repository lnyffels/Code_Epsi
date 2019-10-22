# initialisation
dicoVide = {}
dicoVide2 = dict()
dicoInit = {"nom": "Bob", "age": 42, "identifiant": "S611456"}

# Ajout clé/valeur
dicoVide["MaCle"] = "valeur1"
print(dicoVide["MaCle"])
age = dicoInit["age"]

# copie de dictionnaire
dicoCopie = dicoInit

# obtention des clés et valeurs
keys = dicoCopie.keys()
values = dicoCopie.values()
if "identifiant" in dicoCopie:
    print(dicoCopie["identifiant"])

# parcours d'un dictionnaire
for key,value in dicoCopie.items():
    print(f"clé : {key} , valeur : {value}")

# filtrer une liste de dictionnaire
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
lst = list(filter(lambda x : x['name'] == 'python', dict_a))
print(lst)