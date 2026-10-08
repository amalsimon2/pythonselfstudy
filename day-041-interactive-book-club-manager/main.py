import json

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}"

class BookClubManager:
    def __init__(self, filename='book_club.json'):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_books(self):
        with open(self.filename, 'w') as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books[isbn] = book.__dict__
        self.save_books()

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            self.save_books()

    def list_books(self):
        for isbn, book in self.books.items():
            print(f"ISBN: {isbn}, {book['title']} by {book['author']}")

if __name__ == '__main__':
    manager = BookClubManager()
    while True:
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            manager.add_book(title, author, isbn)
        elif choice == '2':
            isbn = input("Enter ISBN: ")
            manager.remove_book(isbn)
        elif choice == '3':
            manager.list_books()
        elif choice == '4':
            break
        else:
            print("Invalid choice")
