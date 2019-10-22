def inverse(x):
    if x == 0:
        raise ZeroDivisionError
    else :
        inv = 1 / x
    return inv

x = input("Rentrer la valeur :")
try:
    inv = inverse(x)
    print(inv)
except ValueError as exc:
    print("erreur : ", exc)
except (ZeroDivisionError, Exception) as exc:
    print(exc)
except Exception:
    print("Autre erreur inconnue")