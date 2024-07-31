from datetime import datetime, timedelta

# Book Class
class Book:
    def __init__(self, title, author, ISBN, publication_date, status='Available'):
        self.__title = title
        self.__author = author
        self.__ISBN = ISBN
        self.__publication_date = publication_date
        self.__status = status
        self.__due_date = None
        self.__reservations = []

    def borrow(self, user):
        if self.__status == 'Available':
            self.__status = 'Borrowed'
            self.__due_date = datetime.now() + timedelta(days=14)
            user.add_borrowed_book(self)
            print(f"Book '{self.__title}' has been borrowed by {user.get_name()}.")
        else:
            print(f"Book '{self.__title}' is not available for borrowing.")

    def return_book(self, user):
        if self.__status == 'Borrowed':
            self.__status = 'Available'
            self.__due_date = None
            user.remove_borrowed_book(self)
            print(f"Book '{self.__title}' has been returned.")
            if self.__reservations:
                next_user = self.__reservations.pop(0)
                print(f"The book '{self.__title}' is now available for {next_user.get_name()}.")
        else:
            print(f"Book '{self.__title}' is not borrowed.")

    def reserve(self, user):
        if self.__status == 'Available':
            self.__reservations.append(user)
            print(f"Book '{self.__title}' has been reserved by {user.get_name()}.")
        else:
            print(f"Book '{self.__title}' is not available for reservation.")

    # Getters and setters for encapsulation
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_ISBN(self):
        return self.__ISBN

    def get_publication_date(self):
        return self.__publication_date

    def get_status(self):
        return self.__status

    def get_due_date(self):
        return self.__due_date

    def get_reservations(self):
        return self.__reservations

# User Class
class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []
        self.__fines = 0

    # Getters and setters for encapsulation
    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    def get_fines(self):
        return self.__fines

    def add_borrowed_book(self, book):
        self.__borrowed_books.append(book)

    def remove_borrowed_book(self, book):
        self.__borrowed_books.remove(book)

    def add_fine(self, amount):
        self.__fines += amount

# Author Class
class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    # Getters and setters for encapsulation
    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

# Genre Class
class Genre:
    def __init__(self, name, description, category):
        self.__name = name
        self.__description = description
        self.__category = category

    # Getters and setters for encapsulation
    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_category(self):
        return self.__category

# Library Database (for demonstration purposes, using lists)
library_books = []
library_users = []
library_authors = []
library_genres = []

# Helper Functions for CLI Operations
def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    ISBN = input("Enter book ISBN: ")
    publication_date = input("Enter publication date (YYYY-MM-DD): ")
    new_book = Book(title, author, ISBN, publication_date)
    library_books.append(new_book)
    print(f"Book '{title}' added successfully.")

def borrow_book():
    ISBN = input("Enter book ISBN to borrow: ")
    user_name = input("Enter your name: ")
    user = next((u for u in library_users if u.get_name() == user_name), None)
    if user:
        book = next((b for b in library_books if b.get_ISBN() == ISBN), None)
        if book:
            book.borrow(user)
        else:
            print("Book not found.")
    else:
        print("User not found.")

def return_book():
    ISBN = input("Enter book ISBN to return: ")
    user_name = input("Enter your name: ")
    user = next((u for u in library_users if u.get_name() == user_name), None)
    if user:
        book = next((b for b in library_books if b.get_ISBN() == ISBN), None)
        if book:
            book.return_book(user)
        else:
            print("Book not found.")
    else:
        print("User not found.")

def search_book():
    ISBN = input("Enter book ISBN to search: ")
    book = next((b for b in library_books if b.get_ISBN() == ISBN), None)
    if book:
        print(f"Details of book with ISBN '{ISBN}':")
        print(f"Title: {book.get_title()}")
        print(f"Author: {book.get_author()}")
        print(f"Publication Date: {book.get_publication_date()}")
        print(f"Status: {book.get_status()}")
    else:
        print("Book not found.")

def display_all_books():
    print("List of all books:")
    for book in library_books:
        print(f"ISBN: {book.get_ISBN()}, Title: {book.get_title()}, Author: {book.get_author()}, Status: {book.get_status()}")

def add_user():
    name = input("Enter user name: ")
    library_id = input("Enter library ID: ")
    new_user = User(name, library_id)
    library_users.append(new_user)
    print(f"User '{name}' added successfully.")

def view_user_details():
    library_id = input("Enter library ID to view details: ")
    user = next((u for u in library_users if u.get_library_id() == library_id), None)
    if user:
        print(f"Details of user with library ID '{library_id}':")
        print(f"Name: {user.get_name()}")
        print(f"Borrowed Books: {[book.get_title() for book in user.get_borrowed_books()]}")
        print(f"Fines: {user.get_fines()}")
    else:
        print("User not found.")

def display_all_users():
    print("List of all users:")
    for user in library_users:
        print(f"Library ID: {user.get_library_id()}, Name: {user.get_name()}")

def add_author():
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    new_author = Author(name, biography)
    library_authors.append(new_author)
    print(f"Author '{name}' added successfully.")

def view_author_details():
    name = input("Enter author name to view details: ")
    author = next((a for a in library_authors if a.get_name() == name), None)
    if author:
        print(f"Details of author '{name}':")
        print(f"Biography: {author.get_biography()}")
    else:
        print("Author not found.")

def display_all_authors():
    print("List of all authors:")
    for author in library_authors:
        print(f"Name: {author.get_name()}, Biography: {author.get_biography()}")

def add_genre():
    name = input("Enter genre name: ")
    description = input("Enter genre description: ")
    category = input("Enter genre category: ")
    new_genre = Genre(name, description, category)
    library_genres.append(new_genre)
    print(f"Genre '{name}' added successfully.")

def view_genre_details():
    name = input("Enter genre name to view details: ")
    genre = next((g for g in library_genres if g.get_name() == name), None)
    if genre:
        print(f"Details of genre '{name}':")
        print(f"Description: {genre.get_description()}")
        print(f"Category: {genre.get_category()}")
    else:
        print("Genre not found.")

def display_all_genres():
    print("List of all genres:")
    for genre in library_genres:
        print(f"Name: {genre.get_name()}, Description: {genre.get_description()}, Category: {genre.get_category()}")

# CLI Menus
def book_operations():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to Main Menu")
        choice = input("Please enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            display_all_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def user_operations():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Back to Main Menu")
        choice = input("Please enter your choice: ")
        if choice == '1':
            add_user()
        elif choice == '2':
            view_user_details()
        elif choice == '3':
            display_all_users()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def author_operations():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to Main Menu")
        choice = input("Please enter your choice: ")
        if choice == '1':
            add_author()
        elif choice == '2':
            view_author_details()
        elif choice == '3':
            display_all_authors()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def genre_operations():
    while True:
        print("\nGenre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        print("4. Back to Main Menu")
        choice = input("Please enter your choice: ")
        if choice == '1':
            add_genre()
        elif choice == '2':
            view_genre_details()
        elif choice == '3':
            display_all_genres()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    while True:
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")
        choice = input("Please enter your choice: ")
        if choice == '1':
            book_operations()
        elif choice == '2':
            user_operations()
        elif choice == '3':
            author_operations()
        elif choice == '4':
            genre_operations()
        elif choice == '5':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu
if __name__ == "__main__":
    main_menu()
