""" nombre = input("Entrer un nombre : ")

if nombre.isdigit():
    print("nombre est un entier")
    if int(nombre) % 2 == 0:
        print("Vous avez entré un nombre pair")
    else:
        print("Vous avez entré un nombre impair")
else:
    print("vous n'avez pas entré un nombre entier") """

mot = input("Entrer un mot : ")


if mot.find("e") != -1 or mot.find("a") != -1:
    print("Beep")
    if mot.find("e") != -1 ^ mot.find("a") != -1:
        print("Boop")
else:
    print("Cas non traité")
