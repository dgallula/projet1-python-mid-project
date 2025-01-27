from library import Library
from book import Book


def main():
    # Création de la bibliothèque
    library = Library()

    # Menu principal
    while True:
        print("\n=== Library Management System ===")
        print("1. Add a new book")
        print("2. Delete a book")
        print("3. Search books by author")
        print("4. Register a new reader")
        print("5. Remove a reader")
        print("6. Reader reads a book")
        print("7. Display shelves")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Ajouter un livre
            author = input("Enter the author's name: ")
            title = input("Enter the book's title: ")
            num_of_pages = int(input("Enter the number of pages: "))
            book = Book(author, title, num_of_pages)
            library.add_new_book(book)

        elif choice == "2":
            # Supprimer un livre
            title = input("Enter the title of the book to delete: ")
            library.delete_book(title)

        elif choice == "3":
            # Recherche par auteur
            author = input("Enter the author's name: ")
            library.search_by_author(author)

        elif choice == "4":
            # Enregistrer un lecteur
            reader_id = int(input("Enter the reader's ID: "))
            name = input("Enter the reader's name: ")
            library.register_reader(reader_id, name)

        elif choice == "5":
            # Supprimer un lecteur
            name = input("Enter the reader's name: ")
            library.remove_reader(name)

        elif choice == "6":
            # Lecteur lit un livre
            reader_name = input("Enter the reader's name: ")
            book_title = input("Enter the book's title: ")
            library.reader_read_book(book_title, reader_name)

        elif choice == "7":
            # Afficher les étagères
            print("\n=== Shelves ===")
            for i, shelf in enumerate(library.shelves, start=1):
                print(f"\nShelf {i}:")
                print(shelf)

        elif choice == "8":
            # Quitter
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


