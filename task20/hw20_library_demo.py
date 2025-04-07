from hw20_library import Book, Reader

book = Book(book_name="The Hobbit", author="J.R.R. Tolkien", num_pages=400, isbn="0006754023")

vasya = Reader("Vasya")
petya = Reader("Petya")

vasya.reserve_book(book)
petya.reserve_book(book)
vasya.cancel_reserve(book)

petya.reserve_book(book)
vasya.get_book(book)
petya.get_book(book)
vasya.return_book(book)
petya.return_book(book)

vasya.get_book(book)
