class User:
    nombre_instance = 0
    # Si nb est vraiment static, je ne dois pas pouvoir y accéder depuis une instance
    nb = 0

    def __init__(self, nom: str, prenom: str):
        User.nombre_instance += 1  # nombre_instance appartient à User, pas à self
        self.nom = nom
        self.prenom = prenom

    def get_full_name(self):
        print(f"Utilisateur {self.nom.upper()} {self.prenom.capitalize()}")

    @staticmethod
    def initialize_static_attribute():
        User.nb += 1

    @staticmethod
    def get_instance_count():
        print(f"Le nombre d'instance est {User.nombre_instance}")

    @classmethod
    def get_class_attribute(cls):
        return cls.nb


User.initialize_static_attribute()
print(User.get_class_attribute())  # Affiche 1

User.initialize_static_attribute()
print(User.get_class_attribute())
# Static method @staticmethod def static_method(): # Static attribute static_attribute = "This is a static attribute" return static_attribute

user1 = User("Doe", "john")  # User.nombre_instance += 1
print(user1.nb)
print(user1.nombre_instance)
user2 = User("Hotton", "Robin")  #
user3 = User("Marley", "Bob")

# user3.nombre_instance = "toto"

print(f" hors contexte instance d'objet  : {User.nombre_instance}")
print(f"contexte objet user3 : {user3.nombre_instance}")


class Coffee:
    # sans __ Attribut de class public
    # avec __ Attribut de class privé
    __drink = "café"

    def __init__(self, force: int):
        self.force = force

    @classmethod
    def get_drink(cls):
        # Ici, je pourrais vérifier si l'utilisateur qui veut voir __drink a un rôle approprié
        return cls.__drink


# instanciation
cafe1 = Coffee(7)

print(Coffee.get_drink())

#  Appel du getter
print(Coffee.get_drink())
