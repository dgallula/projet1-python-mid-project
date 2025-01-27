from shelf import Shelf
from reader import Reader
from book import Book


class Library:
    def __init__(self):
        self.shelves = [Shelf() for _ in range(3)]  # Liste de 3 objets Shelf
        self.readers = []  # Liste d'objets Reader

    def is_there_place_for_new_book(self):
        # Vérifie s'il y a une place disponible dans l'une des étagères
        return any(not shelf.is_shelf_full for shelf in self.shelves)

    def add_new_book(self, book: Book):
        # Ajoute un livre dans la première étagère ayant une place libre
        for shelf in self.shelves:
            if not shelf.is_shelf_full:
                shelf.addBook(book)
                return
        print("No space available to add the book.")

    def delete_book(self, book_title: str):
        # Supprime un livre de l'une des étagères en fonction de son titre
        for shelf in self.shelves:
            for i, book in enumerate(shelf.books):
                if book and book.title == book_title:
                    shelf.books[i] = None
                    shelf.is_shelf_full = False
                    print(f"Book '{book_title}' removed from the library.")
                    return
        print(f"Book '{book_title}' not found in the library.")

    def change_locations(self, title1: str, title2: str):
        # Échange les emplacements de deux livres dans les étagères
        book1, book2 = None, None
        shelf1, shelf2 = None, None
        index1, index2 = -1, -1

        for shelf in self.shelves:
            for i, book in enumerate(shelf.books):
                if book and book.title == title1:
                    book1, shelf1, index1 = book, shelf, i
                elif book and book.title == title2:
                    book2, shelf2, index2 = book, shelf, i

        if book1 and book2:
            shelf1.books[index1], shelf2.books[index2] = book2, book1
            print(f"Books '{title1}' and '{title2}' have swapped locations.")
        else:
            print("One or both books not found in the library.")

    def change_locations_in_same_shelf(self, shelf_num: int, index1: int, index2: int):
        # Échange les emplacements de deux livres dans la même étagère
        if 0 < shelf_num <= len(self.shelves):
            shelf = self.shelves[shelf_num - 1]
            if shelf.books[index1 - 1] and shelf.books[index2 - 1]:
                shelf.books[index1 - 1], shelf.books[index2 - 1] = (
                    shelf.books[index2 - 1],
                    shelf.books[index1 - 1],
                )
                print(f"Books in Shelf {shelf_num} at positions {index1} and {index2} have swapped.")
            else:
                print("One or both locations are empty in the specified shelf.")
        else:
            print("Invalid shelf number.")

    def order_books(self):
        # Trie les livres dans chaque étagère par nombre de pages (ordre croissant)
        for shelf in self.shelves:
            shelf.order_books()
        print("All shelves have been ordered by the number of pages.")

    def register_reader(self, reader_id: int, name: str):
        # Enregistre un nouveau lecteur
        self.readers.append(Reader(reader_id, name))
        print(f"Reader '{name}' has been registered.")

    def remove_reader(self, name: str):
        # Supprime un lecteur en fonction de son nom
        for i, reader in enumerate(self.readers):
            if reader.name == name:
                del self.readers[i]
                print(f"Reader '{name}' has been removed.")
                return
        print(f"Reader '{name}' not found.")

    def reader_read_book(self, book_title: str, reader_name: str):
        # Ajoute un livre lu à la liste des livres d'un lecteur
        for reader in self.readers:
            if reader.name == reader_name:
                reader.read_book(book_title)
                return
        print(f"Reader '{reader_name}' not found.")

    def search_by_author(self, author: str):
        # Recherche les titres des livres d'un auteur spécifique
        result = []
        for shelf in self.shelves:
            for book in shelf.books:
                if book and book.author == author:
                    result.append(book.title)
        if result:
            print(f"Books by {author}: {', '.join(result)}")
        else:
            print(f"No books by {author} found in the library.")
        return result


# Exemple d'utilisation
if __name__ == "__main__":
    # Création de la bibliothèque
    library = Library()

    # Ajout de lecteurs
    library.register_reader(1, "Alice")
    library.register_reader(2, "Bob")

    # Ajout de livres
    book1 = Book("Author A", "Book 1", 200)
    book2 = Book("Author B", "Book 2", 150)
    book3 = Book("Author A", "Book 3", 300)

    library.add_new_book(book1)
    library.add_new_book(book2)
    library.add_new_book(book3)

    # Recherche par auteur
    library.search_by_author("Author A")

    # Enregistrement de la lecture
    library.reader_read_book("Book 1", "Alice")

    # Suppression d'un livre
    library.delete_book("Book 2")

    # Échange de positions entre deux livres
    library.change_locations("Book 1", "Book 3")

    # Tri des livres par nombre de pages
    library.order_books()

    # Affichage des résultats
    for shelf in library.shelves:
        print(shelf)

#exemple d'utilisation
if __name__ == "__main__":
    library = Library()
    library.add_new_book(Book("Author A", "Book 1", 200))
    library.add_new_book(Book("Author B", "Book 2", 150))
    library.add_new_book(Book("Author A", "Book 3", 300))

    print(library.search_by_author("Author A"))
    print(library.reader_read_book("Book 1", "Alice"))
    print(library.delete_book("Book 2"))
    print(library.change_locations("Book 1", "Book 3"))
    print(library.order_books())

    