# Datetime_2

from datetime import datetime


def get_date_input():
    while True:
        user_input = input()
        try:
            date_obj = datetime.strptime(user_input, "%Y-%m-%d")
            return date_obj
        except ValueError:
            print("Ошибка! Введите дату в правильном формате ГГГГ-ММ-ДД:")


def compare_dates(user_date):
    current_date = datetime.now().date()
    user_date = user_date.date()

    if user_date > current_date:
        print("Введённая дата находится в будущем.")
        return True
    elif user_date < current_date:
        print("Введённая дата находится в прошлом.")
        return False
    else:
        print("Введённая дата — сегодня.")
        return None


print("Введите дату для проверки (ГГГГ-ММ-ДД): ")
user_date = get_date_input()
compare_dates(user_date)
