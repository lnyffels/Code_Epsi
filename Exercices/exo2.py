# Correction
from math import sqrt

GRAVITY = 9.8

d= float(input("Hauteur de l'objet laché en mètres : "))

vf = sqrt(2 * GRAVITY * d)  # vi2 = 0 car vitesse initiale nulle

print("L'objet touchera le sol a une vitesse de %.2f m/s" % vf)