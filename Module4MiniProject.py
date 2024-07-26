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

def borrow_book():
    isbn = input("Enter the ISBN of the book to borrow: ")
    for book in books:
        if book['isbn'] == isbn:
            if book['available']:
                book['available'] = False
                save_data_to_file(books, 'books.json')
                print(f"You have borrowed '{book['title']}' successfully!")
                return
            else:
                print("The book is currently not available.")
                return
    print("Book not found.")

def return_book():
    isbn = input("Enter the ISBN of the book to return: ")
    for book in books:
        if book['isbn'] == isbn:
            if not book['available']:
                book['available'] = True
                save_data_to_file(books, 'books.json')
                print(f"You have returned '{book['title']}' successfully!")
                return
            else:
                print("The book was not borrowed.")
                return
    print("Book not found.")

def search_books():
    keyword = input("Enter a keyword to search for books: ")
    found_books = [book for book in books if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower()]
    if found_books:
        for book in found_books:
            print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']})")
    else:
        print("No books found.")

def display_books():
    if books:
        for book in books:
            print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}, Available: {'Yes' if book['available'] else 'No'})")
    else:
        print("No books available.")

def book_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for books")
    print("5. Display all books")
    print("6. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        borrow_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        search_books()
    elif choice == "5":
        display_books()
    elif choice == "6":
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

def search_genres():
    keyword = input("Enter a keyword to search for genres: ")
    found_genres = [genre for genre in genres if keyword.lower() in genre['name'].lower()]
    if found_genres:
        for genre in found_genres:
            print(genre['name'])
    else:
        print("No genres found.")

def display_genres():
    if genres:
        for genre in genres:
            print(genre['name'])
    else:
        print("No genres available.")

def genre_menu():
    print("Genre Operations:")
    print("1. Add a new genre")
    print("2. Search for genres")
    print("3. Display all genres")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_genre()
    elif choice == "2":
        search_genres()
    elif choice == "3":
        display_genres()
    elif choice == "4":
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

def search_users():
    keyword = input("Enter a keyword to search for users: ")
    found_users = [user for user in users if keyword.lower() in user['name'].lower() or keyword.lower() in user['email'].lower()]
    if found_users:
        for user in found_users:
            print(f"{user['name']} (ID: {user['user_id']}, Email: {user['email']})")
    else:
        print("No users found.")

def display_users():
    if users:
        for user in users:
            print(f"{user['name']} (ID: {user['user_id']}, Email: {user['email']})")
    else:
        print("No users available.")

def user_menu():
    print("User Operations:")
    print("1. Add a new user")
    print("2. Search for users")
    print("3. Display all users")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_user()
    elif choice == "2":
        search_users()
    elif choice == "3":
        display_users()
    elif choice == "4":
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

def search_authors():
    keyword = input("Enter a keyword to search for authors: ")
    found_authors = [author for author in authors if keyword.lower() in author['name'].lower()]
    if found_authors:
        for author in found_authors:
            print(author['name'])
    else:
        print("No authors found.")

def display_authors():
    if authors:
        for author in authors:
            print(author['name'])
    else:
        print("No authors available.")

def author_menu():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. Search for authors")
    print("3. Display all authors")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_author()
    elif choice == "2":
        search_authors()
    elif choice == "3":
        display_authors()
    elif choice == "4":
        return
    else:
        print("Invalid choice. Please try again.")

# Main menu
def main_menu():
    print("Welcome to the Library Management System!")
    print("Main Menu:")
