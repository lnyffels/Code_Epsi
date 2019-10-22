lst = ['u', 's', 'e', 'r', 1, 5, 3]
chaine = ""
for elem in lst:
    if type(elem) != int:
        chaine += elem
    else:
        break
print(chaine)   # affiche user
print("".join(lst[:4])) # affiche user