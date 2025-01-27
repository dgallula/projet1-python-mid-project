from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Création d'une base de données
db = client["library_management"]

# Création des collections pour les livres, étagères et lecteurs
books_collection = db["books"]
shelves_collection = db["shelves"]
readers_collection = db["readers"]

# Ajout de livres dans la collection "books"
books_data = [
    {"author": "Author1", "title": "Book1", "num_of_pages": 100},
    {"author": "Author2", "title": "Book2", "num_of_pages": 200},
    {"author": "Author3", "title": "Book3", "num_of_pages": 300},
    {"author": "Author4", "title": "Book4", "num_of_pages": 400},
    {"author": "Author5", "title": "Book5", "num_of_pages": 500},
    {"author": "Author6", "title": "Book6", "num_of_pages": 600},
]

# Insertion des livres dans la collection "books"
books_collection.insert_many(books_data)

# Ajout des étagères (ici on suppose 3 étagères)
shelves_data = [
    {"shelf_number": 1, "books": ["Book1", "Book2"]},
    {"shelf_number": 2, "books": ["Book3", "Book4"]},
    {"shelf_number": 3, "books": ["Book5", "Book6"]},
]

# Insertion des étagères dans la collection "shelves"
shelves_collection.insert_many(shelves_data)

# Ajout des lecteurs dans la collection "readers"
readers_data = [
    {"reader_id": 1, "name": "Reader1", "borrowed_books": []},
    {"reader_id": 2, "name": "Reader2", "borrowed_books": ["Book1"]},
    {"reader_id": 3, "name": "Reader3", "borrowed_books": ["Book3", "Book4"]},
]

# Insertion des lecteurs dans la collection "readers"
readers_collection.insert_many(readers_data)

# Confirmation de l'ajout des données
print("Books, shelves, and readers have been added to the database.")




