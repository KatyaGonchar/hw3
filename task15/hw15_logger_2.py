# Logger_2

import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime


logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = TimedRotatingFileHandler(
    "hw15_logger_2.log", when="midnight", interval=1, backupCount=7,
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_date_input():
    while True:
        user_input = input()
        try:
            date_obj = datetime.strptime(user_input, "%Y-%m-%d")
            return date_obj
        except ValueError:
            print("Ошибка! Введите дату в правильном формате ГГГГ-ММ-ДД:")
            logger.critical(f"Введена некорректная дата: {user_input}")


def compare_dates(user_date):
    current_date = datetime.now().date()
    user_date = user_date.date()

    if user_date > current_date:
        print("Введённая дата находится в будущем.")
        logger.info(f"Пользователь ввёл корректную дату из будущего: {user_date}")
        return True
    elif user_date < current_date:
        print("Введённая дата находится в прошлом.")
        logger.error(f"Пользователь ввёл дату из прошлого: {user_date}")
        return False
    else:
        print("Введённая дата — сегодня.")
        logger.warning(f"Пользователь ввёл сегодняшнюю дату: {user_date}")
        return None


while True:
    print("Введите дату из будущего в формате ГГГГ-ММ-ДД:")
    user_date = get_date_input()
    if compare_dates(user_date) is True:
        break

print("Программа завершена.")
