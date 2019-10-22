import json

# Données en json
jsonData = '{"nom":"Ln", "age":45, "ville":"Lille"}'
# charge un dictionnaire python
dico = json.loads(jsonData)
print(dico["ville"])  # affiche Lille


dicoAdresse = {
    "rue" : "la joie",
    "cp" : 59800,
    "ville" : "Lille",
    "tels" : ["078494949", "03204848484"]
}
# Récupére un json (format str) depuis un dictionnaire
jsonAdresse = json.dumps(dicoAdresse)
print(jsonAdresse)


