import os

os.chdir("c:/temp")
mon_fichier = open("monfichier.txt", "w")
mon_fichier.write("ecrire une premiere ligne")
mon_fichier.close()

with open("monfichier.txt", "r") as fichier:
    texte_recupere = fichier.read()

print(texte_recupere)