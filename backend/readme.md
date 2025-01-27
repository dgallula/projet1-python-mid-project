
synthese du projet 


Voici une synthèse de ton projet basée sur les informations que tu m'as fournies jusqu'à présent :

Résumé du Projet : Système de Gestion de Bibliothèque
Ce projet consiste à développer un système de gestion de bibliothèque avec une interface utilisateur permettant de gérer des livres, des étagères, des lecteurs, et d'interagir avec une base de données MongoDB pour stocker et récupérer les informations. L'objectif est de fournir une plateforme permettant à un employé de gérer les livres de la bibliothèque, les lecteurs, et de maintenir les données synchronisées avec MongoDB.

Technologies utilisées :
Python : Langage de programmation principal utilisé pour développer la logique du système.
MongoDB : Base de données NoSQL utilisée pour stocker les livres, les lecteurs, et les autres données liées à la gestion de la bibliothèque.
Requests : Bibliothèque Python pour interagir avec une API REST externe (par exemple, pour l'authentification des employés).
JSON : Format de sérialisation pour sauvegarder et charger les données de la bibliothèque.
Fonctionnalités principales :
Authentification des employés : L'employé doit se connecter via un nom d'utilisateur et un email. L'authentification est vérifiée en consultant une API REST externe.
Gestion des livres :
Ajouter un nouveau livre à la bibliothèque avec des informations comme l'auteur, le titre, et le nombre de pages.
Supprimer un livre existant.
Modifier les emplacements des livres sur les étagères.
Gestion des étagères : Chaque étagère peut contenir plusieurs livres. Le système permet d'ajouter, supprimer et déplacer des livres entre les étagères.
Gestion des lecteurs :
Enregistrer de nouveaux lecteurs avec un identifiant et un nom.
Supprimer un lecteur.
Permettre à un lecteur de lire un livre en l'ajoutant à sa liste de livres lus.
Recherche de livres par auteur : Les utilisateurs peuvent rechercher des livres en fonction de l'auteur.
Organisation des livres : Les livres peuvent être triés par nombre de pages pour faciliter leur gestion.
Sauvegarde et chargement des données : Le système permet de sauvegarder les informations de la bibliothèque dans un fichier JSON, ainsi que de charger les données à partir d'un fichier JSON ou de MongoDB pour récupérer l'état de la bibliothèque à tout moment.
Structure du système :
Classes :
Book : Représente un livre avec des attributs comme l'auteur, le titre, et le nombre de pages.
Shelf : Représente une étagère contenant une liste de livres.
Reader : Représente un lecteur avec un identifiant et un nom, ainsi qu'une liste de livres qu'il a lus.
Library : Représente l'ensemble de la bibliothèque, gérant les étagères et les lecteurs, et fournissant des méthodes pour manipuler les livres et les données.
Interaction avec MongoDB : MongoDB est utilisé pour stocker les livres et les lecteurs. Lorsqu'un livre est ajouté ou supprimé, les modifications sont appliquées à la base de données, garantissant la persistance des données.
Objectifs du projet :
Gestion simple et efficace des livres et des lecteurs dans une bibliothèque.
Synchronisation avec MongoDB pour une persistance de données fiable.
Interface utilisateur conviviale pour faciliter les opérations quotidiennes de la bibliothèque.
Flexibilité et extensibilité du système pour gérer de nouvelles fonctionnalités comme l'ajout de catégories de livres, la gestion des prêts, etc.
Progrès réalisés :
Développement de la logique de gestion des livres et des étagères.
Connexion à MongoDB pour l'enregistrement et la récupération des données.
Mise en place de l'authentification des employés via une API REST.
Création d'un menu interactif permettant de gérer les livres, les étagères, les lecteurs, et les données persistantes.
Prochaines étapes :
Ajouter des fonctionnalités supplémentaires, comme la gestion des prêts de livres.
Tester le système avec des utilisateurs réels pour garantir la stabilité et l'ergonomie.
Améliorer l'interface utilisateur avec une interface graphique ou un système web pour rendre l'application plus accessible.
Conclusion :
Le projet de gestion de bibliothèque vise à simplifier et automatiser les tâches administratives liées à la gestion des livres et des lecteurs. Grâce à l'utilisation de MongoDB et à une architecture modulaire, le système est flexible et facile à étendre pour répondre aux besoins futurs d'une bibliothèque en constante évolution.

You need to create a program for managing a library. You have the following classes :
Class : Book
Data Members:
• - author (string)
• - title (string)
• - num_of_pages (int)
Class : Shelf
Data Members:
• - books (a list of Maximum 5 Book objects)
• - is_shelf_full (boolean)
Functions
• - addBook – receives a Book object and add it to the books list in the first
available. If there is no more space , a proper message will be printed. If the shelf
become full (with 5 Book objects), than the “is_shelf_full” will be set to True.
Otherwise, will be set to False.
• - replace_books – receives 2 numbers between 1 and 5 and replace between
the Books in these locations. If one of the location is empty, a proper message
will be printed.
• - order_books – order the books by their num_of_pages in ascending order.
Class : Reader
Data Members:
• - id (int)
• - name (string)
• - books (a list of dictionaries with titles of the books he read and the dates he
took them from the library)
Functions
- read_book – receives a book title and adds it + the current date to the books list
Class : Library
Data Members:
• - shelves (a list of 3 Shelf objects)
• - readers ( a list of Reader objects)
Functions
• - is_there_place_for_new_book - Returns a Boolean indicates if there is a place
for inserting a new book to the library
• - add_new_book - receives a new Book object and add it to the first Shelf with a
free space
• - delete_book – receives a book title and delete the Book object from the library.
• - change_locations – receives 2 books titles, and replace between these 2 Books
objects (their locations in the shelves).
• change_locations_in_same_shelf – receives a shelf number, and books locations
, and replace between these 2 Books objects.
• - order_books – order all books in each shelf by their num_of_pages
• - register_reader – receives a new reader name and id and add it to the readers
list.
• - remove_reader – receives a new reader name and removes it from the readers
list.
• - reader_read_book – receives a book title and a reader name and add this book
title to the reader’s books list
• - search_by_author – receives an author name and returns all books titles this
author wrote
The Program
The program manages ONLY 1 Library object.
The program starts with pre-defined 2 Books object on EACH shelf. These books
are pulled from a proper collection in a MongoDB data base (The collection
stores 6 Books records – for 3 Shelves)
This library management system is accessible only to registered library
employees. To start working with system, the employee must login with his
username and email login details. These details will be verified against the REST
API at https://jsonplaceholder.typicode.com/users
If there’s an employee with that username and email he will be logged in and will get the
following menu ( in infinite loop) :
• - “For adding a book - Press 1”.
• - “For deleting a book - Press 2”.
• - “For changing books locations - Press 3”.
• - “For registering a new reader - Press 4”.
• - “For removing a reader - Press 5”.
• - “For searching books by author – Press 6.”
• - “For reading a book by a reader – Press 7.”
• - “For ordering all books – Press 8.”
• - “For saving all data – Press 9”.
• - “For loading data – Press 10”.
• - “For exit – Press 11”.
If the user press 1 – The program will ask the user for all new book data and
adds it to the library by calling “add_new_book” of the Library object.
If the user press 2 – The program will ask the user for the book title and remove it
from the library by calling “delete_book” of the Library object.
If the user press 3 – The program will ask the user for the 2 books titles he want
to replace, and replace them by calling “replace_locations” of the Library object.
If the user press 4 – The program will ask the user for the new reader name will
add him to the readers list by calling “register_reader” of the Library object.
If the user press 5 – The program will ask the user for the reader name remove
him from the readers list by calling “remove_reader” of the Library object.
If the user press 6 – The program will ask the user for the author name print all
author’s books titles by calling “search_by_author” of the Library object.
If the user press 7 – The program will ask the user for reader id and the book title and
add this book to the reader’s books list by calling “read_book” of the proper Reader
Object.
If the user press 8 – The program order all books by calling “order_books” of the Library
object.
If the user press 9 – The program ask the user for a file name and saves all library data
in a JSON file on that given name as follows :
If the user press 10 – The program ask the user for a file name and loads all Library
data from that JSON file with the given name
If the user press 11 – The program ends.

library_management/
├── classes/
│   ├── book.py
│   ├── shelf.py
│   ├── reader.py
│   ├── library.py
├── data/
│   └── books.json
├── main.py
└── requirements.txt
