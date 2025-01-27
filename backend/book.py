class Book:
    def __init__(self, author: str, title: str, num_of_pages: int):
        self.author = author
        self.title = title
        self.num_of_pages = num_of_pages

    def __str__(self):
        return f"Author: {self.author}\nTitle: {self.title}\nNumber of pages: {self.num_of_pages}"


# Exemple d'utilisation
if __name__ == "__main__":
    book = Book("John Doe", "The Great Gatsby", 100)
    print(book)






