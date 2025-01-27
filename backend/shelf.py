from book import Book

class Shelf:
    def __init__(self):
        self.books = [None] * 5  # Liste de 5 emplacements, initialisés à None
        self.is_shelf_full = False

    def addBook(self, book: Book):
        for i in range(len(self.books)):
            if self.books[i] is None:
                self.books[i] = book
                self.is_shelf_full = all(self.books)  # Met à jour l'état du shelf
                print(f"Book '{book.title}' added at position {i + 1}.")
                return
        print("The shelf is full. Cannot add more books.")

    def replace_books(self, position1: int, position2: int):
        if not (1 <= position1 <= 5 and 1 <= position2 <= 5):
            print("Invalid positions. Positions must be between 1 and 5.")
            return

        idx1, idx2 = position1 - 1, position2 - 1
        if self.books[idx1] is None or self.books[idx2] is None:
            print("One or both positions are empty. Cannot replace books.")
            return

        self.books[idx1], self.books[idx2] = self.books[idx2], self.books[idx1]
        print(f"Books at positions {position1} and {position2} have been swapped.")

    def order_books(self):
        # Filtrer les livres existants et les trier
        existing_books = [book for book in self.books if book is not None]
        existing_books.sort(key=lambda book: book.num_of_pages)

        # Réinitialiser les livres sur l'étagère
        self.books = existing_books + [None] * (5 - len(existing_books))
        print("Books have been ordered by the number of pages.")

    def __str__(self):
        result = "Shelf content:\n"
        for i, book in enumerate(self.books):
            if book is not None:
                result += f"Position {i + 1}: {book}\n"
            else:
                result += f"Position {i + 1}: Empty\n"
        return result


# Exemple d'utilisation
if __name__ == "__main__":
    shelf = Shelf()

    # Création de livres pour tester
    book1 = Book("Author A", "Book A", 300)
    book2 = Book("Author B", "Book B", 150)
    book3 = Book("Author C", "Book C", 200)

    # Ajout de livres
    shelf.addBook(book1)
    shelf.addBook(book2)
    shelf.addBook(book3)

    # Affichage de l'étagère
    print(shelf)

    # Remplacement de livres
    shelf.replace_books(1, 3)
    print(shelf)

    # Tri des livres
    shelf.order_books()
    print(shelf)


