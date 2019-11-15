words = []

word = input("Entrer un mot : ")

while word != "":
    if word not in words:
        words.append(word)
    word = input("Entrer un mot : ")

for word in words:
    print(word)