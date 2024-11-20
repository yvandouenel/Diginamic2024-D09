from datetime import date

ma_liste = [1, 2, 3, 4]
for nb in ma_liste:
    print(nb + 2)  # Nous printons chaque chiffre dans ma_liste en ajoutant 2

ma_string = "python"

for char in ma_string:
    print(f"la lettre {char} !")

for x in range(5):
    print(x)

ma_liste = ["a", "b", "c", "d", "e"]
for index, char in enumerate(ma_liste):
    print(f"la lettre {char} est à l'index {index}.")

print(index)
print(char)

""" ma_liste = [False, False, False, False, False]

for booleen in ma_liste:
    if booleen is True:
        print("élément vrai trouvé!")
        break
else:
    print("Tous les éléments de la liste sont faux.") """

total = 20
x = 0

while x < total:
    print(x)
    x += 1  # on n'oublie pas d'incrémenter x à chaque itération

print(x)

ma_liste = ["qsdf", "COUCOU", "PYTHON", "lowercase", "toto", "TITI"]

# chaque fois qu'on croise une string en uppercase on passe à l'itération suivante sans exécuter le reste du code
for string in ma_liste:
    if string.isupper():
        break
    print(string)  # nous ne printons que "lowercase"

print("break fait sortir immédiatement de la boucle")


mon_dict = {
    "nom": "Bouchard",
    "prenom": "Gérard",
    "admin": True,
    "date_naissance": date(1982, 5, 26),
    "nombre_abonnes": 123627,
    "enfants": ["Glop", {"nom": "Bouchard", "prenom": "Timothée"}],
}

print(mon_dict["admin"])  # True
print(mon_dict["enfants"][0])  # Glop
print(mon_dict["enfants"][1]["prenom"])  # Timothée
