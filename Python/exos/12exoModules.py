# Créer un script python écrivant 5 entiers aléatoires entre 0 et 100 dans un fichier .txt dans votre dossier 'Documents'
# Le résultat doit apparaître comme ceci: "Voici mes 5 nombres aléatoires: X, X, X, X et X"

# Printer le contenu du document

# Supprimer le fichier
import random
from pathlib import Path
import os

chemin = (
    "/Users/YvanDOUENEL/Diginamic/Formations/2024/2024-D09/Algo&Python/Python/tests"
)

# Création d'un nouveau dossier
# La fonction join gére les '\' sous windows ou les '/' sous linux et mac
dossier = os.path.join(chemin, "Documents")
if not os.path.exists(dossier):
    os.makedirs(dossier)
    print(f"Dossier créé : {dossier}")

chemin = f"{chemin}/Documents/aleatoires.txt"

random1 = random.randint(0, 100)
random2 = random.randint(0, 100)
random3 = random.randint(0, 100)
random4 = random.randint(0, 100)
random5 = random.randint(0, 100)

# Instanciation de Path
path = Path(chemin)

# Création du fichier
path.touch(exist_ok=True)

# Ecriture des nombres aléatoires dans le fichier
path.write_text(str(random1) + "\n" + str(random2))
print(f"Je viens d'écrire dans le fichier Document/aleatoires.txt {random1} {random2} ")
