BABY_PRICE = 0.00
CHILD_PRICE = 14.00
ADULT_PRICE = 23.00
SENIOR_PRICE = 18.00

BABY_LIMIT = 2
CHILD_LIMIT = 12
ADULT_LIMIT = 64

total = 0

line = input("Entrer l'age du visiteur : ")

while line != "":
    age = int(line)

    if age <= BABY_LIMIT:
        total = total + BABY_PRICE
    elif age <= CHILD_LIMIT:
        total = total + CHILD_PRICE
    elif age <= ADULT_PRICE:
        total = total + ADULT_PRICE
    else:
        total = total + SENIOR_PRICE

    line = input("Entrer l'age du visiteur : ")

print("Prix total pour le groupe : %.2f" % total)

