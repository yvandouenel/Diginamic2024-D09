""" x = input("Entre un nombre : ")
if x == str(10):
    print("x = 10")
elif int(x) < 10:
    print("x < 10")
else:
    print("x > 10") """

x = 30
y = 20

# Using the ternary operator to assign the smaller value to 'min_value'
min_value = x if x < y else y

print(min_value)  # Output: 10

nom = "Gérard"

""" cond_and = nom.startswith("G") and nom.endswith("d")
print(cond_and) """

cond_xor = nom.startswith("G") ^ nom.endswith("d")
print(cond_xor)

A = True
B = True
C = True

print(A ^ (B ^ C))


mot = "toto"

match mot:
    case "titi":
        print("titi")
    case "tata":
        print("tata")
    case "toto":
        print("toto")
