""" Déclaration de la classe User """


class User:
    # function constructeur
    def __init__(self, prenom: str, nom: str):
        # Déclaration et assignation d'un attribut de l'objet en cours d'instanciation
        self.firstname = prenom
        # déclaration de la variable lastname qui n'est pas liée à mon instance en cours
        self.lastname = nom
        ## Fin du constructeur. Normalement, l'instance a maintenant des attributs avec des valeurs

    def hello(self):
        print(f"hello {self.firstname}")


# Création des instances en appellant le constructeur
user1 = User("Serge", "Lama")  # Appel de la méthode __init__
user2 = User("Robin", "Hotton")  # Appel de la méthode __init__

user1.hello()
user2.hello()


class Dog:
    # attribut de classe
    species = "Chien"
    dogs_number = 0

    def __init__(self, name, age):
        # attributs d'instance
        self.name = name
        self.age = age
        Dog.increment_dogs_number()

    @classmethod
    def increment_dogs_number(cls):
        cls.dogs_number += 1


# Instanciations
filou = Dog("Filou", 4)
print(Dog.dogs_number)
zazi = Dog("Zazi", 12)
print(Dog.dogs_number)
print(filou.dogs_number)
filou.increment_dogs_number()
print(filou.dogs_number)
print(zazi.dogs_number)

""" print(filou.name)
print(filou.species)
print(zazi.name)
print(zazi.species) """
