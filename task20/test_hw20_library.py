import unittest
from hw20_library import Book, Reader


class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        self.book = Book("1984", "George Orwell", 328, "978-0451524935")
        self.reader_1 = Reader("Alice")
        self.reader_2 = Reader("Bob")

    # Positive test: successful reservation by a reader
    def test_successful_reservation(self):
        self.reader_1.reserve_book(self.book)
        self.assertEqual(self.book.status, "reserved")
        self.assertEqual(self.book.reserved_by, self.reader_1)

    # Negative test: another reader tries to reserve an already reserved book
    def test_reservation_by_another_reader(self):
        self.reader_1.reserve_book(self.book)
        result = self.reader_2.reserve_book(self.book)
        self.assertFalse(result)

    # Positive test: reader successfully takes a book they reserved
    def test_get_reserved_book(self):
        self.reader_1.reserve_book(self.book)
        self.reader_1.get_book(self.book)
        self.assertEqual(self.book.status, "taken")
        self.assertEqual(self.book.taken_by, self.reader_1)

    # Negative test: another reader tries to return a book they didn’t take
    def test_failed_return_by_another(self):
        self.reader_1.get_book(self.book)
        result = self.reader_2.return_book(self.book)
        self.assertFalse(result)

    # Positive test: reader successfully returns a book they took
    def test_successful_return(self):
        self.reader_1.get_book(self.book)
        self.reader_1.return_book(self.book)
        self.assertEqual(self.book.status, "free")
        self.assertIsNone(self.book.taken_by)


if __name__ == '__main__':
    unittest.main()
