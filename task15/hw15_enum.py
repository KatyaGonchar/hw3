# Enum

from enum import Enum


class OrderStatus(Enum):
    PENDING = "Заказ ожидает обработки"
    IN_PROGRESS = "Заказ готовится"
    READY = "Заказ готов"
    COMPLETED = "Заказ выдан"
    CANCELLED = "Заказ отменён"


class Order:
    def __init__(self, order_id, status=OrderStatus.PENDING):
        try:
            self.order_id = int(order_id)
            if self.order_id <= 0:
                raise ValueError
        except (ValueError, TypeError):
            print("Ошибка: Неверный ID заказа. ID должен быть положительным числом.")
            self.order_id = None
            self.status = None
            return

        self.status = status
        print(f"Заказ {self.order_id} успешно создан. Текущий статус: {self.status.value}")

    def update_status(self, new_status):
        if self.order_id is None:
            print(f"Ошибка: заказ с ID {self.order_id} отсутствует, статус недоступен.")
            return False
        if not isinstance(new_status, OrderStatus):
            print("Ошибка: статус должен быть объектом OrderStatus.")
            return False
        self.status = new_status
        print(f"Заказ {self.order_id} успешно обновлен. Текущий статус: {self.status.value}")
        return True

    def display_status(self):
        if self.order_id is None:
            print(f"Ошибка: заказ с ID {self.order_id} отсутствует.")
            return False
        print(f"Текущий статус заказа {self.order_id}: {self.status.value}")
        return True


order_id = input("Введите ID заказа: ")
order = Order(order_id)

if order.order_id is None:
    print("Дальнейшее выполнение невозможно из-за неверного ID.")
else:
    order.display_status()
    order.update_status(OrderStatus.IN_PROGRESS)
    order.display_status()
