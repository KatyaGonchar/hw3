import pytest
import logging
from source.hw21_library import Book, Reader

logger = logging.getLogger(__name__)


@pytest.fixture
def book():
    return Book("1984", "George Orwell", 328, "978-0451524935")


@pytest.fixture
def reader_1():
    return Reader("Alice")


@pytest.fixture
def reader_2():
    return Reader("Bob")


# Positive test: successful reservation by a reader
def test_successful_reservation(book, reader_1):
    reader_1.reserve_book(book)
    logger.info("Book status after reservation: %s", book.status)
    assert book.status == "reserved"
    assert book.reserved_by == reader_1


# Negative test: another reader tries to reserve an already reserved book
def test_reservation_by_another_reader(book, reader_1, reader_2):
    reader_1.reserve_book(book)
    result = reader_2.reserve_book(book)
    logger.warning("Repeated reservation attempt by another reader: %s", result)
    assert result is False


# Positive test: reader successfully takes a book they reserved
def test_get_reserved_book(book, reader_1):
    reader_1.reserve_book(book)
    reader_1.get_book(book)
    logger.info("Book status after being taken: %s", book.status)
    assert book.status == "taken"
    assert book.taken_by == reader_1


# Negative test: another reader tries to return a book they didn’t take
def test_failed_return_by_another(book, reader_1, reader_2):
    reader_1.get_book(book)
    result = reader_2.return_book(book)
    logger.warning("Wrong return attempt by another reader: %s", result)
    assert result is False


# Positive test: reader successfully returns a book they took
def test_successful_return(book, reader_1):
    reader_1.get_book(book)
    reader_1.return_book(book)
    logger.info("Book status after return: %s", book.status)
    assert book.status == "free"
    assert book.taken_by is None
