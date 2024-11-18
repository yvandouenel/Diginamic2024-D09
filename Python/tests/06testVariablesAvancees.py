ma_variable = 55
print("id de ma_variable: ", id(ma_variable))  # l'adresse mémoire de ma variable

a = 123

""" Passage par référence """
b = a

print(id(a))
print(id(b))

""" une assignation change d'adresse """
a = 52

print(id(a))

print(b)

a, b = 2, 3
a, b = b, a

print(b)
