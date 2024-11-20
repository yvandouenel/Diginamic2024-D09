""" # Définition de la fonction
def add(a, b):  # paramètres qui vont prendre les valeurs des arguments
    if not str(a).isdigit():
        return "Vous n'avez pas entré un nombre entier"
    return a + b


# Appel de la fonction
# déclaration de la variable result et assignation du retour de l'appel de la fonction add avec les arguments 2 et 3
result = add(2, 3)
result = add("toto", 12)

print(result)


def dire_bonjour(first_name, name="mystérieux inconnu"):
    return f"Coucou {first_name} {name} !"


print(dire_bonjour("Stéphane", "Top"))  # Coucou Stéphane !
print(dire_bonjour("Bob")) """

""" def recursive(a: int) -> None:
    print(a)
    a += 1
    if a == 5:
        recursive(a)


recursive(4) """


def fac(a):
    if a == 1:
        return a
    else:
        return a * fac(a - 1)


result = fac(6)
print(result)
