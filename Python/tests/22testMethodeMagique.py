class User:
    species = "Human"

    def __init__(self, name: str, firstname: str):
        # attributs d'instances auxquels on assigne les valeurs des paramètres
        self.nom = name
        self.prenom = firstname

    def __str__(self):
        return f"Je te présente {self.prenom.capitalize()} {self.nom.upper()} "


# Instanciation d' utilisateurs en appelant la fonction constructeur avec des arguments
johnny = User("Halliday", "johnny")
Georges = User("Brassens", "Georges")
print(johnny)
