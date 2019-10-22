"""
Un triangle peut être classé en fonction de la longueur de ses côtés : équilatéral, isocèle ou scalène.
Les 3 côtés d'un triangle équilatéral ont la même longueur. Un triangle isocèle a 2 cotés de même longueur
et un de longueur différente. Si tous les cotés ont des longueurs différentes, le triangle est scalène.
Ecrivez un programme console qui demande à l’utilisateur la longueur des 3 côtés du triangle et qui
affiche alors un message indiquant le type du triangle.
"""
cote1 = float(input("Saisir la longueur du coté 1 du triangle :"))
cote2 = float(input("Saisir la longueur du coté 2 du triangle :"))
cote3 = float(input("Saisir la longueur du coté 3 du triangle :"))


def is_equilateral():
    return cote1 == cote2 == cote3

def is_isocele():
    return cote1 == cote2 or cote1 == cote3 or cote2 == cote3

if is_equilateral():
    print("le triangle est équilateral")
elif is_isocele():
    print("le triangle est isocèle")
else:
    print("le triangle est scalène")
