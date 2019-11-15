points = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 2, "K": 5, "L": 1, "M": 3,
          "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}

word = input("Entrer un mot :")

word_upper = word.upper()
score = 0

for letter in word_upper:
    if letter in points.keys():
        score = score + int(points[letter])

print("Résultat : ", score)
