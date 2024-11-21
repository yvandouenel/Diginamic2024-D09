class Book:
    def __init__(self, title: str, author: str, publication_year: str):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    # appelée automatiquement quand on fait appel à print()
    def __str__(self):
        return f"Titre : {self.title} - Auteur : {self.author} - Année : {self.publication_year}"


class Library:
    def __init__(self, list_books: list[Book], name: str):
        self.list_books = list_books
        self.name = name

    def add_book(self, book: Book):
        # Pour ajouter un livre en fait, on ajoute une instance de livre dans une liste
        self.list_books.append(book)
        print(f"Livre {book.title} ajouté")

    def remove_book(self, book: Book):
        # Pour supprimer un livre en fait, on retire une instance de livre dans une liste
        self.list_books.remove(book)
        print(f"Livre {book.title} supprimé")

    def display_books(self):
        # Parcours de la liste pour afficher chaque livre à l'aide de la boucle for in
        print(f"Livres de la bibliothèque {self.name}")
        for book in self.list_books:
            print(book)

        print("\n")


# Scénario : Créer une bibliothèque, créer 3 livres, les ajouter à la bibliothèque, afficher la liste, supprimer un livre et afficher à nouveau la liste de la bibliothèque

# Instanciation d'une bibliothèque avec une liste de livres vide
emileZola = Library([], "Emile Zola")

# Instanciation de de 3 livres
miserables = Book("Les misérables", "Victor Hugo", "1862")
germinal = Book("Germinal", "Emile Zola", "1885")
bonheur_dames = Book("Au bonheur des dames", "Emile Zola", "1883")

# Ajout des trois livres à la bibliothèque
emileZola.add_book(miserables)
emileZola.add_book(germinal)
emileZola.add_book(bonheur_dames)

# Affichage de la liste des livres
emileZola.display_books()

# Suppression d'un livre
emileZola.remove_book(miserables)

# Affichage de la liste des livres
emileZola.display_books()
