from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, ISBN, publication_date, status):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.publication_date = publication_date
        self.status = status
        self.due_date = None
        self.reservations = []

    def borrow(self, user):
        self.status = 'Borrowed'
        self.due_date = datetime.now() + timedelta(days=14)

    def return_book(self):
        if datetime.now() > self.due_date:
            user.fines += 10
        self.status = 'Available'
        self.due_date = None
        if self.reservations:
            next_user = self.reservations.pop(0)
            print(f'The book {self.title} is now available for {next_user.name}.')

    def reserve(self, user):
        self.reservations.append(user)

class User:
    def __init__(self, name, library_id, borrowed_books):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = borrowed_books
        self.fines = 0

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

class Genre:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

def main_menu():
    print("Welcome to the Library Management System!")
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
        quit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()
