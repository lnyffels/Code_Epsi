# Correction
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
