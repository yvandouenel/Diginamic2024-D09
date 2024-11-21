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


admin1 = Admin("Dusse", "Jean-Claude", "DSI")
admin1.get_full_name()
print(Admin.role)
print(User.role)
