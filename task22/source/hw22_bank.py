# Банковский вклад

class Bank:
    def __init__(self):
        self.client_id = None
        self.client_name = None
        self.deposit_balance = None
        self.deposit_years = None

    def register_client(self, client_id, name):
        self.client_id = client_id
        self.client_name = name
        print(f"Клиент {self.client_name} успешно зарегистрирован.")
        return True

    def open_deposit_account(self, client_id, start_balance, years):
        if self.client_id != client_id:
            print("Ошибка! Клиент не зарегистрирован.")
            return False

        self.deposit_balance = float(start_balance)
        self.deposit_years = int(years)
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
        balance = float(self.deposit_balance)
        years = int(self.deposit_years)
        final_balance = round(
            balance * (1 + rate / 12) ** (12 * years), 2)
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


bank_instance = Bank()


def register_client(client_id, name):
    return bank_instance.register_client(client_id, name)


def open_deposit_account(client_id, start_balance, years):
    return bank_instance.open_deposit_account(client_id, start_balance, years)


def calc_deposit_interest_rate(client_id):
    return bank_instance.calc_deposit_interest_rate(client_id)


def close_deposit(client_id):
    return bank_instance.close_deposit(client_id)
