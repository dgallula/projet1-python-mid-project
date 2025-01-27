from datetime import datetime

class Reader:
    def __init__(self, reader_id: int, name: str):
        self.id = reader_id
        self.name = name
        self.books = []  # Liste de dictionnaires contenant le titre du livre et la date

    def read_book(self, book_title: str):
        # Ajoute le livre et la date actuelle à la liste des livres lus
        current_date = datetime.now().strftime("%Y-%m-%d")
        self.books.append({"title": book_title, "date": current_date})
        print(f"{self.name} has read the book '{book_title}' on {current_date}.")

    def __str__(self):
        # Génère une représentation textuelle des livres lus par le lecteur
        result = f"Reader ID: {self.id}\nName: {self.name}\nBooks Read:\n"
        if not self.books:
            result += "No books read yet."
        else:
            for book in self.books:
                result += f"- {book['title']} (Date: {book['date']})\n"
        return result


# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'un lecteur
    reader = Reader(1, "Alice")

    # Lecture de livres
    reader.read_book("1984")
    reader.read_book("Brave New World")

    # Affichage des livres lus
    print(reader)


