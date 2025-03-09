# Банковский вклад

class Bank:

    def register_client(self, client_id, name):
        self.client_id = client_id
        self.client_name = name
        print(f"Клиент {self.client_name} успешно зарегистрирован.")
        return True

    def open_deposit_account(self, client_id, start_balance, years):
        if self.client_id != client_id:
            print("Ошибка! Клиент не зарегистрирован.")
            return False

        self.deposit_balance = start_balance
        self.deposit_years = years
        print(f"Вклад для {self.client_name} открыт. Стартовая сумма: {self.deposit_balance}.")
        return True

    def calc_deposit_interest_rate(self, client_id):
        if self.client_id != client_id:
            print("Ошибка: Клиент не зарегистрирован!")
            return False
        if self.deposit_balance is None:
            print("Ошибка! Отсутствует действующий вклад.")
            return False

        rate = 0.1  # 10% годовых
        final_balance = round(
            self.deposit_balance * (1 + rate / 12) ** (12 * self.deposit_years), 2)
        print(f"Финальная сумма по истечении срока вклада: {final_balance}.")
        return final_balance

    def close_deposit(self, client_id):
        if self.client_id != client_id:
            print("Ошибка: Клиент не зарегистрирован!")
            return False
        if self.deposit_balance is None:
            print("Вклад уже закрыт или не был открыт.")
            return False
        else:
            print(f"Вклад для {self.client_name} закрыт.")
            self.deposit_balance = None
            self.deposit_years = None
            return True


client_id = "0000001"
bank = Bank()
bank.register_client(client_id=client_id, name="Siarhei")
bank.open_deposit_account(client_id=client_id, start_balance=1000, years=1)
assert bank.calc_deposit_interest_rate(client_id=client_id) == 1104.71, \
    "Ошибка: Неверная итоговая сумма по вкладу."
bank.close_deposit(client_id=client_id)

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
