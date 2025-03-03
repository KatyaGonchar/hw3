# Положительные аргументы функции

def validate_arguments(room_perimeter):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError("Ошибка! Все аргументы должны быть положительными числами.")
        return room_perimeter(*args)
    return wrapper


@validate_arguments
def room_perimeter(length, width):
    return (length + width) * 2


try:
    print(room_perimeter(5, 4))
except ValueError as e:
    print(e)

try:
    print(room_perimeter(5.5, 4.4))
except ValueError as e:
    print(e)

try:
    print(room_perimeter(5, -4))
except ValueError as e:
    print(e)

try:
    print(room_perimeter(0, -4))
except ValueError as e:
    print(e)


# Вернуть число

def result_isnumber(first_element):
    def wrapper(lst):
        result = first_element(lst)
        if isinstance(result, (int, float)):
            print(result)
        else:
            print("Ошибка: первый элемент не является числом!")
    return wrapper


@result_isnumber
def first_element(lst):
    return lst[0]


first_element([10, 20, 30])
first_element(['a', 2, 3])
first_element([-5.7, 13, 42])


# Декоратор типов

def typed(type_):
    def decorator(add):
        def wrapper(*args):
            converted_args = [type_(arg) for arg in args]
            return add(*converted_args)
        return wrapper
    return decorator


@typed(type_=str)
def add(a, b):
    return a + b


assert add("3", 5) == "35"
assert add(5, 5) == "55"
assert add('a', 'b') == "ab"


@typed(type_=int)
def add(a, b, c):
    return a + b + c


assert add(5, 6, 7) == 18


@typed(type_=float)
def add(a, b, c):
    return a + b + c


assert add(0.1, 0.2, 0.4) == 0.7000000000000001
