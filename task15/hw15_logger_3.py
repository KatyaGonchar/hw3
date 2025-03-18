# Logger_3

import logging
from enum import Enum


logger = logging.getLogger("order_logger")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
file_handler = logging.FileHandler("hw15_logger_3.log")
file_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.addHandler(file_handler)


class OrderStatus(Enum):
    PENDING = "Заказ ожидает обработки"
    IN_PROGRESS = "Заказ готовится"
    READY = "Заказ готов"
    COMPLETED = "Заказ выдан"
    CANCELLED = "Заказ отменён"


class Order:
    def __init__(self, order_id, status=OrderStatus.PENDING):
        if order_id.isdigit() and int(order_id) > 0:
            self.order_id = int(order_id)
            self.status = status
        else:
            self.order_id = None
            self.status = OrderStatus.CANCELLED
            logger.error(f"Ошибка: Неверный ID заказа '{order_id}'. "
                         f"ID должен быть положительным числом.")
            print("Ошибка: Неверный ID заказа. ID должен быть положительным числом.")
            return

        logger.info(f"Заказ {self.order_id} успешно создан. Текущий статус: {self.status.value}")
        print(f"Заказ {self.order_id} успешно создан. Текущий статус: {self.status.value}")

    def update_status(self, new_status):
        if self.order_id is None:
            logger.error(f"Ошибка: заказ с ID {self.order_id} отсутствует, статус недоступен.")
            print(f"Ошибка: заказ с ID {self.order_id} отсутствует, статус недоступен.")
            return False
        if not isinstance(new_status, OrderStatus):
            logger.error(f"Ошибка: указан неверный статус '{new_status}'. "
                         f"Статус должен быть объектом OrderStatus.")
            print("Ошибка: статус должен быть объектом OrderStatus.")
            return False
        self.status = new_status
        logger.info(f"Заказ {self.order_id} успешно обновлен. Текущий статус: {self.status.value}")
        print(f"Заказ {self.order_id} успешно обновлен. Текущий статус: {self.status.value}")
        return True

    def display_status(self):
        if self.order_id is None:
            logger.error(f"Ошибка: заказ с ID {self.order_id} отсутствует.")
            print(f"Ошибка: заказ с ID {self.order_id} отсутствует.")
            return False
        logger.info(f"Текущий статус заказа {self.order_id}: {self.status.value}")
        print(f"Текущий статус заказа {self.order_id}: {self.status.value}")
        return True


order_id = input("Введите ID заказа: ")
order = Order(order_id)

if order.order_id:
    order.display_status()
    order.update_status(OrderStatus.IN_PROGRESS)
    order.display_status()
else:
    print("Дальнейшее выполнение невозможно из-за неверного ID.")
