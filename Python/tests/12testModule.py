import random as random_from_module
import os

""" collision possible de nom de variable """
""" random = 21

print(random_from_module.randint(0, 5))

print(random_from_module.randint(1, 5))
print(random_from_module.uniform(0, 1) * 1000) """


chemin = (
    "/Users/YvanDOUENEL/Diginamic/Formations/2024/2024-D09/Algo&Python/Python/tests"
)

# Création d'un nouveau dossier dans mes Documents
# Documents/nouveau_dossier/os
# La fonction join gére les '\' sous windows ou les '/' sous linux et mac
dossier = os.path.join(chemin, "test", "os")
""" Vérifie si le répertoire décrit dans chemin existe et sinon, il est créé """
if not os.path.exists(dossier):
    os.makedirs(dossier)
    print(f"je viens de créer le dossier {dossier}")
else:
    print("Ce dossier existe déjà")

# Suppression de l'architecture de dossier nouvellement créée
if os.path.exists(dossier):
    os.removedirs(dossier)
    print(f"je viens de supprimer le dossier {dossier}")
