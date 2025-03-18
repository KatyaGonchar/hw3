# Datetime_1

from datetime import datetime


def get_date_input():
    while True:
        user_input = input()
        try:
            date_obj = datetime.strptime(user_input, "%Y-%m-%d")
            return date_obj
        except ValueError:
            print("Ошибка! Введите дату в правильном формате ГГГГ-ММ-ДД:")


def display_days_difference(date1, date2):
    days = abs((date2 - date1).days)
    print(f"Количество дней между датами: {days}")
    return days


print("Введите первую дату (ГГГГ-ММ-ДД): ")
first_date = get_date_input()

print("Введите вторую дату (ГГГГ-ММ-ДД): ")
second_date = get_date_input()

display_days_difference(first_date, second_date)
