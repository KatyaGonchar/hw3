# Конвертер валют

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


class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = {
            "USD": {"BYN": 3.269, "EUR": 0.465},  # 1 USD = 3.269 BYN from assert 1
            "EUR": {"BYN": 7.04, "USD": 2.152},  # 1 EUR = 7.04 BYN from assert 2
            "BYN": {"USD": 1 / 3.269, "EUR": 1 / 7.04}
        }

    def exchange_currency(self, currency: str, amount: float, convert_to: str = "BYN"):
        if currency == convert_to:
            return amount, currency
        elif currency in self.exchange_rates and convert_to in self.exchange_rates[currency]:
            rate = self.exchange_rates[currency][convert_to]
            return round(amount * rate, 2), convert_to
        else:
            print(f"Ошибка! Курс для перевода из {currency} в {convert_to} не найден.")
            return False


class Person:
    def __init__(self, currency: str, amount: float):
        self.currency = currency
        self.amount = amount


client_id = "0000001"
bank = Bank()
bank.register_client(client_id=client_id, name="Siarhei")
bank.open_deposit_account(client_id=client_id, start_balance=1000, years=1)
assert bank.calc_deposit_interest_rate(client_id=client_id) == 1104.71, \
    "Ошибка: Неверная итоговая сумма по вкладу."
bank.close_deposit(client_id=client_id)

converter = CurrencyConverter()

vasya = Person("USD", 10)
petya = Person("EUR", 5)

assert converter.exchange_currency(vasya.currency, vasya.amount) == (32.69, "BYN"), "Ошибка при конвертации!"
assert converter.exchange_currency(petya.currency, petya.amount) == (35.20, "BYN"), "Ошибка при конвертации!"
assert converter.exchange_currency(vasya.currency, vasya.amount, "EUR") == (4.65, "EUR"), "Ошибка при конвертации!"
assert converter.exchange_currency(petya.currency, petya.amount, "USD") == (10.76, "USD"), "Ошибка при конвертации!"
