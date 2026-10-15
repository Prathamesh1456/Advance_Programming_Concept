class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.availability = "available"

    def borrow_book(self):
        if self.availability == "available":
            self.availability = "borrowed"
            print("Book borrowed successfully.")
        else:
            print("Book is already borrowed.")

    def return_book(self):
        self.availability = "available"
        print("Book returned successfully.")

    def show_details(self):
        print("\nBook Details")
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print("Status:", self.availability)


book = Book("Python Programming", "John Smith", 2023)

book.show_details()

book.borrow_book()
book.show_details()

book.return_book()
book.show_details()