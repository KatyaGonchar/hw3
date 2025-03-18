def square_of_number():
    number = float(input("Enter the number: "))
    return number ** 2


result1 = square_of_number()
print(f"The square of the number is {result1}")


def even_odd():
    number = int(input("Enter the number: "))
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


result2 = even_odd()
