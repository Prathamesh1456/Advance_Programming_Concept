# 25.	Create functions to add books, issue books, return books, search books, and display available books. Maintain book availability using dictionaries.

def add_book(library, book_id, title, author):
    library[book_id] = {'title': title, 'author': author, 'available': True}
    print(f"Book '{title}' added successfully.")
def issue_book(library, book_id):
    if book_id in library and library[book_id]['available']:
        library[book_id]['available'] = False
        print(f"Book '{library[book_id]['title']}' issued successfully.")
    else:
        print("Book is not available for issue.")
def return_book(library, book_id):
    if book_id in library and not library[book_id]['available']:
        library[book_id]['available'] = True
        print(f"Book '{library[book_id]['title']}' returned successfully.")
    else:
        print("Book is not issued or does not exist.")
def search_book(library, title):
    found_books = [book_id for book_id, details in library.items() if details['title'].lower() == title.lower()]
    if found_books:
        for book_id in found_books:
            print(f"Book ID: {book_id}, Title: {library[book_id]['title']}, Author: {library[book_id]['author']}, Available: {library[book_id]['available']}")
    else:
        print("Book not found.")
def display_available_books(library):
    print("Available Books:")
    for book_id, details in library.items():
        if details['available']:
            print(f"Book ID: {book_id}, Title: {details['title']}, Author: {details['author']}")
def main():
    library = {}
    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. Display Available Books")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(library, book_id, title, author)
        elif choice == '2':
            book_id = input("Enter book ID to issue: ")
            issue_book(library, book_id)
        elif choice == '3':
            book_id = input("Enter book ID to return: ")
            return_book(library, book_id)
        elif choice == '4':
            title = input("Enter book title to search: ")
            search_book(library, title)
        elif choice == '5':
            display_available_books(library)
        elif choice == '6':
            print("Exiting the library management system.")
            break
        else:
            print("Invalid choice. Please try again.")