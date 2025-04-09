# Библиотека


class Book:
    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.status = "free"
        self.reserved_by = None
        self.taken_by = None

    def reserve(self, reader):
        if self.status == "reserved" and self.reserved_by == reader:
            return True  # The user is trying to re-reserve a book, not an error
        elif self.status == "free":
            self.status = "reserved"
            self.reserved_by = reader
            return True
        else:
            return False

    def cancel_reserve(self, reader):
        if self.status != "reserved":
            return True  # The book is not reserved by anyone, not an error
        elif self.status == "reserved" and self.reserved_by == reader:
            self.status = "free"
            self.reserved_by = None
            return True
        else:
            return False

    def get_book(self, reader):
        if self.status == "taken" and self.taken_by == reader:
            return True  # The user is trying to take a book he already has, not an error
        elif self.status == "reserved" and self.reserved_by == reader:
            self.status = "taken"
            self.taken_by = reader
            return True
        elif self.status == "free":
            self.status = "taken"
            self.taken_by = reader
            return True
        else:
            return False

    def return_book(self, reader):
        if self.status != "taken":  # User is trying to return a book he doesn't have, not an error
            return True
        elif self.status == "taken" and self.taken_by == reader:
            self.status = "free"
            self.taken_by = None
            return True
        else:
            return False


class Reader:
    def __init__(self, name):
        self.name = name

    def reserve_book(self, book):
        if not book.reserve(self):
            print(f"{self.name} can not reserve a book")
            return False

    def cancel_reserve(self, book):
        if not book.cancel_reserve(self):
            print(f"{self.name} can not cancel the reservation")
            return False

    def get_book(self, book):
        if not book.get_book(self):
            print(f"{self.name} can not get a book")
            return False

    def return_book(self, book):
        if not book.return_book(self):
            print(f"{self.name} can not return a book")
            return False
