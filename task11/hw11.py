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
            return result
        return "Ошибка: первый элемент не является числом!"
    return wrapper


@result_isnumber
def first_element(lst):
    return lst[0]


print(first_element([10, 20, 30]))
print(first_element(['a', 2, 3]))
print(first_element([-5.7, 13, 42]))


# Декоратор типов

def typed(type):
    def decorator(add):
        def wrapper(*args):
            for t in type:
                if any(isinstance(arg, t) for arg in args):
                    converted_args = [t(arg) for arg in args]
                    return add(*converted_args)
            return add(*args)
        return wrapper
    return decorator


@typed(type=[str, float, int])
def add(*args):
    result = args[0]
    for arg in args[1:]:
        result += arg
    return result


assert add("3", 5) == "35"
assert add(5, "5") == "55"
assert add('a', 'b') == "ab"
assert add(5, 6, 7) == 18
assert add(0.1, 0.2, 0.4) == 0.7000000000000001
