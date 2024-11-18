x = 2
y = 3

# va nous donner le résultat "L'addition de 2 et 3 est égale à 5"
print(f"L'addition de {x} et {y} est égale à {x + y}")

""" format permet de définir et d'utiliser des alias """
print(
    "L'addition de {premier} et {second} est égale à {addition}".format(
        premier=x, second=y, addition=x + y
    )
)

ceci = "ceci"
cela = "cela"

# il faut le même nombre de paramètres que de {}
print("Je peut printer {} et {}".format(ceci, cela))

# ou alors on utilise des indices
print("Je peux printer {1} et {0}".format(ceci, cela))
