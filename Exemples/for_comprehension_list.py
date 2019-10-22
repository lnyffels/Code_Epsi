lst = [1, 5, 87, 32, 12]
chaine = 'azerty'

new_lst = [x for x in lst]
new_lst = [x ** 2 for x in lst]
new_lst = [x ** 2 for x in lst if x < 80]
new_lst.sort()
print(new_lst)


print([c.upper() for c in chaine])
