n = 0
while n <= 7:
    if n == 5:
        n += 1
        continue
    print(n)
    n += 1
print("fin while 1")


n = 0
while n <= 7:
    if n == 5:
        n += 1
        break
    print(n)
    n += 1
print("fin while 2")

