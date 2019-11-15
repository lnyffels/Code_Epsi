TAX_RATE = 0.1
TIP_RATE = 0.18

cost = float(input("Rentrer le cout du repas:"))

tax = cost * TAX_RATE
tip = cost * TIP_RATE
total = cost + tax + tip

print("La taxe est de %.2f et le pourboire de %.2f. Le cout total du repas s'éléve à %.2f" % (tax, tip, total))