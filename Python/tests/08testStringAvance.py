minuscule = "minuscule"
print(minuscule)
majuscule = minuscule.upper()
print(minuscule)
print(majuscule)

phrase = "bonjour tout le monde"

print(phrase.capitalize())
print(phrase)

bonjour = "Boooonjour"

print(bonjour.replace("jour", "soir"))
print(bonjour)

print(bonjour.count("oo"))

index = "Triython , c'est cool. tython est puissant.".find("Python")
print(index)
""" Déclaration de la variable je et assignation du retour de la méthode startwith """
je = "Je commence par je".startswith("Je")
toto = "Je finis par je".endswith("je")
print(je)
print(toto)

help("str.startswith")
