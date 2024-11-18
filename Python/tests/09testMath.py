import math

arrondi = math.floor(3.8)  # arrondi
print(arrondi)  # 3

x = 0

""" x = x + 2  """
x += 2
x += 2
x *= 3

print(x)

if x == 10:
    print("x = 10")
else:
    print("x != 10")
""" y a la même référence (même adresse mémoire) """
y = x
""" x = "Toto" """

if x is y:
    print("x et y ont la même adresse mémoire")
else:
    print("x et y n'ont pas la même adresse mémoire")
