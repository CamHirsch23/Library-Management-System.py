import json
import re

# Utility functions
def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def validate_isbn(isbn):
    pattern = r'^(?:ISBN(?:-1[03])?:? )?(?=\d{10}$|(?=(?:\d+-){4})\d{13}$|97[89]\d{10}$|(?=(?:\d+-){4})\d{17}$)97[89]?\d{1,5}[- ]?\d+[- ]?\d+[- ]?\d+[- ]?\d$'
    return re.match(pattern, isbn) is not None

# Model definitions
class Book:
    def __init__(self, title, author, isbn, publication_date, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_date = publication_date
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Genre:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} (ID: {self.user_id}, Email: {self.email})"

class Author:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# Load data
books = load_data_from_file('books.json')
genres = load_data_from_file('genres.json')
users = load_data_from_file('users.json')
authors = load_data_from_file('authors.json')

# Book operations
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    isbn = input("Enter the book ISBN: ")
    if not validate_isbn(isbn):
        print("Invalid ISBN format.")
        return
    publication_date = input("Enter the publication date: ")
    new_book = Book(title, author, isbn, publication_date)
    books.append(new_book.__dict__)
    save_data_to_file(books, 'books.json')
    print(f"Book '{new_book}' added successfully!")

def book_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        return
    else:
        print("Invalid choice. Please try again.")

# Genre operations
def add_genre():
    name = input("Enter the genre name: ")
    new_genre = Genre(name)
    genres.append(new_genre.__dict__)
    save_data_to_file(genres, 'genres.json')
    print(f"Genre '{new_genre}' added successfully!")

def genre_menu():
    print("Genre Operations:")
    print("1. Add a new genre")
    print("2. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_genre()
    elif choice == "2":
        return
    else:
        print("Invalid choice. Please try again.")

# User operations
def add_user():
    user_id = input("Enter the user ID: ")
    name = input("Enter the user name: ")
    email = input("Enter the user email: ")
    new_user = User(user_id, name, email)
    users.append(new_user.__dict__)
    save_data_to_file(users, 'users.json')
    print(f"User '{new_user}' added successfully!")

def user_menu():
    print("User Operations:")
    print("1. Add a new user")
    print("2. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_user()
    elif choice == "2":
        return
    else:
        print("Invalid choice. Please try again.")

# Author operations
def add_author():
    name = input("Enter the author name: ")
    new_author = Author(name)
    authors.append(new_author.__dict__)
    save_data_to_file(authors, 'authors.json')
    print(f"Author '{new_author}' added successfully!")

def author_menu():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_author()
    elif choice == "2":
        return
    else:
        print("Invalid choice. Please try again.")

# Main menu
def main_menu():
    print("Welcome to the Library Management System!")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. Genre Operations")
    print("3. User Operations")
    print("4. Author Operations")
    print("5. Quit")

    choice = input("Enter your choice: ")
    if choice == "1":
        book_menu()
    elif choice == "2":
        genre_menu()
    elif choice == "3":
        user_menu()
    elif choice == "4":
        author_menu()
    elif choice == "5":
        print("Thank you for using the Library Management System.")
        exit()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    while True:
        main_menu()
