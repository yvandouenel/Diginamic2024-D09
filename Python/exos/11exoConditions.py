nombre = input("Entrer un nombre : ")

if nombre.isdigit():
    print("nombre est un entier")
    if int(nombre) % 2 == 0:
        print("Vous avez entré un nombre pair")
    else:
        print("Vous avez entré un nombre impair")
else:
    print("vous n'avez pas entré un nombre entier")
