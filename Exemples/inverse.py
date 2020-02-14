def inverse(x):
    try:
        if x == 0:
            raise ZeroDivisionError
        result = 1 / x
        return result
    except (ZeroDivisionError, ValueError) as exp:
        print("Attention division par zero")
    except Exception as exc:
        print(exc)


x = int(input("Entrer un nombre :"))
print(inverse(x))

