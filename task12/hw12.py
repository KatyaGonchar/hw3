# Банковский вклад

class Bank:

    def register_client(self, client_id, name):
        self.client_id = client_id
        self.client_name = name
        print(f"Клиент {self.client_name} успешно зарегистрирован.")

    def open_deposit_account(self, client_id, start_balance, years):
        if self.client_id != client_id:
            print("Ошибка! Клиент не зарегистрирован.")
            return

        self.deposit_balance = start_balance
        self.deposit_years = years
        print(f"Вклад для {self.client_name} открыт. Стартовая сумма: {self.deposit_balance}.")

    def calc_deposit_interest_rate(self, client_id):
        if self.client_id != client_id:
            print("Ошибка: Клиент не зарегистрирован!")
            return
        if self.deposit_balance is None:
            print ("Ошибка! Отсутствует действующий вклад.")
            return

        P = self.deposit_balance
        years = self.deposit_years
        r = 0.1  # 10% годовых
        final_balance = round (P * (1 + r / 12) ** (12 * years), 2)
        print(f"Финальная сумма по истечении срока вклада: {final_balance}.")
        return final_balance

    def close_deposit(self, client_id):
        if self.client_id != client_id:
            print("Ошибка: Клиент не зарегистрирован!")
            return
        if self.deposit_balance is None:
            print("Вклад уже закрыт или не был открыт.")
        else:
            print(f"Вклад для {self.client_name} закрыт.")
            self.deposit_balance = None
            self.deposit_years = None


client_id = "0000001"
bank = Bank()
bank.register_client(client_id=client_id, name="Siarhei")
bank.open_deposit_account(client_id=client_id, start_balance=1000, years=1)
assert bank.calc_deposit_interest_rate(client_id=client_id) == 1104.71, "Ошибка: Неверная итоговая сумма по вкладу."
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
            return
        elif self.status == "free":
            self.status = "reserved"
            self.reserved_by = reader
        elif self.status == "taken":
            print("User can not reserve a book, the book is already taken.")
        else:
            print("User can not reserve a book")

    def cancel_reserve(self, reader):
        if self.status != "reserved":
            return
        elif self.status == "reserved" and self.reserved_by == reader:
            self.status = "free"
            self.reserved_by = None
        else:
            print("User can not cancel a reservation")

    def get_book(self, reader):
        if self.status == "taken" and self.taken_by == reader:
            return
        elif self.status == "reserved" and self.reserved_by == reader:
            self.status = "taken"
            self.taken_by = reader
        elif self.status == "free":
            self.status = "taken"
            self.taken_by = reader
        else:
            print("User can not get a book")

    def return_book(self, reader):
        if self.status != "taken":
            return
        elif self.status == "taken" and self.taken_by == reader:
            self.status = "free"
            self.taken_by = None
        else:
            print("User can not return a book")

class Reader:
    def __init__(self, name):
        self.name = name

    def reserve_book(self, book):
        book.reserve(self)

    def cancel_reserve(self, book):
        book.cancel_reserve(self)

    def get_book(self, book):
        book.get_book(self)

    def return_book(self, book):
        book.return_book(self)


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
