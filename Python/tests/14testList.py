ma_liste = [1, 2, 3]
# append est-elle une méthode pure ou impure
# append est impure car elle modifie une variable (donnée) déjà existante.
# on appelle cela également un effet de bord
ma_liste.append(4)


print(ma_liste)

test = "Hello"
# upper une méthode pure car elle ne modifie aucune données (variable) pré-existante
print(test.upper())
print(test)

ma_liste.extend([5, 6, 7, ["toto", "titi", [True, False]]])
print(ma_liste)

ma_liste.remove(7)
""" print(ma_liste.pop(6)) """
print(ma_liste)

# Atteindre les éléments d'une liste (tableau à index)
print(ma_liste[3])
print(ma_liste[6][2][0])


ma_liste = [1, 2, 3, 4, 5, 6]

print(ma_liste[0])  # [1]

print(ma_liste[3:5])
print(ma_liste[:-1:2])

liste_str = ["a", "b", "z", "c", "r", "m", "y"]
liste_int = [23, 1, 2, 75, 54, 2, 42]

# sort est une fonction impure car elle modifie la liste pré-existante
liste_str.sort()
# liste_int.sort()

# la fonction sorted est pure car elle ne modifie pas list_int
list_int_sorted = sorted(liste_int)

print(liste_str)  # ['a', 'b', 'c', 'm', 'r', 'y', 'z']
print(liste_int)
print(list_int_sorted)  # [1, 2, 2, 23, 42, 54, 75]
