from pathlib import Path

chemin = "/Users/YvanDOUENEL/Diginamic/Formations/2024/2024-D09/Algo&Python/Python/tests/doc.txt"

p = Path(chemin)  # Création d'un objet Path - instanciation
p.touch(
    exist_ok=True
)  # Création du fichier txt dans le dossier Documents L'argument exist_ok=True est crucial car il indique à la méthode de se terminer avec succès sans générer d'erreur si le fichier existe déjà. Sans cet argument, si le fichier existe déjà, une FileExistsError serait levée.
p_length = p.write_text("Coucou !")  # Écrit du texte dans le fichier
p_text = p.read_text()
print(
    f"Je viens d'écrire dans {chemin} le texte {p_text} qui est composé de {p_length} caractères"
)

print(p_text)  # Lecture du contenu du fichier

print(p.name)  # Print le nom du fichier
print(p.suffix)  # Print l'extension du fichier
