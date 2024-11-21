class User:
    def __init__(self, nom: str, prenom: str):
        self.nom = nom
        self.prenom = prenom

    def get_full_name(self):
        print(f"Utilisateur {self.nom.upper()} {self.prenom.capitalize()}")


# La classe Admin dérive de la classe mère
# Un admin est forcément un utilisateur, mais un utilisateur n'est pas forcément un admin
class Admin(User):
    # Attribut de classe
    role = "admin"

    def __init__(self, nom: str, prenom: str, service: str):
        super().__init__(nom, prenom)  # Appel du constructeur de la classe mère
        # Attribut d'instance service
        self.service = service


# Est assigné à la variable admin 1 une instance de la classe Admin
admin1 = Admin("Dusse", "Jean-Claude", "DSI")
admin1.get_full_name()
print(Admin.role)
print(admin1.service)


class Chaise:
    # Attribut de classe
    nb_pieds = 4

    def __init__(self, couleur: str):
        self.couleur = couleur


class ChaiseEnBois(Chaise):

    def __init__(self, couleur: str, bois: str):
        super().__init__(couleur)
        self.bois = bois

    def __str__(self):
        return f"Instance de Chaise {self.couleur} en {self.bois} qui comporte, comme toute chaise qui se restecte,   {Chaise.nb_pieds} pieds"


# Instanciations
chaise_bleue = Chaise("bleu")
chaise_rose = Chaise("rose")

chaise_chene_rose = ChaiseEnBois(bois="chêne", couleur="rose")

print(chaise_chene_rose)
