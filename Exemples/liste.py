from typing import List

# Initialisation
lst = []

lstNumber = [10, 20, 30, 40]
lstNumberType: List[int] = [3, 6, 8, 34, 10, 567]
lstHybrid = [34, 'azerty', (4, 8), [1, 2, 3]]
listInitNumber = range(30)
lstCinqZeros = [0]*5

# Accès au premier élément
elem = lstNumberType[0]

# Concaténation
lstTotal = lstNumber + lstNumberType

# Copie
lstCopie = lstNumberType


lg = len(lstNumberType)                 # taille de la liste
lstNumberType.append(7)                 # ajoute un élément à la fin de la liste
lstNumberType.sort()                    # trie la liste
lstNumberType.reverse()                 # inverse la liste
positionElem = lstNumberType.index(7)   # recherche l'élément 7 dans la liste
lstNumberType.remove(10)                # retire un élement de la liste
elem = lstNumberType.pop()              # retire le dernier élément de la liste

# Filtrer une liste par une compréhension de liste ou via filter + lambda
lstCopie1 = [x for x in lstHybrid if type(x) == str ]
lstCopie2 = list(filter(lambda x: type(x) == str, lstHybrid))
print (lstCopie1)
print (lstCopie2)