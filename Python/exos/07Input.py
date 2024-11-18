""" nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prenom : ")
age = input("Entrez votre âge : ")
adresse = input("Entrez votre adresse : ")

print(nom, prenom, age, adresse) """

nombre_entier = input("Entrez un entier : ")
if nombre_entier.isdigit():
    nombre_entier = int(nombre_entier) + 3.14
    print(nombre_entier)
else:
    print("vous n'avez pas entré un nombre entier")
