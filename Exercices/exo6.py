def inverse(x):
    if x == 0:
        raise ZeroDivisionError
    else :
        inv = 1 / x
    return inv

x = input("Rentrer la valeur : ")
try:
    inv = inverse(int(x))
    print(inv)
except ValueError as exc:
    print("erreur : ", exc)
except ZeroDivisionError:
    print("erreur : division par 0")
except Exception:
    print("Autre erreur inconnue")