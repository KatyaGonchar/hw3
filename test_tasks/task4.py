def fun1(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    return [1] + digits


def number_to_list(number):
    return [int(digit) for digit in str(number) if digit.isdigit()]


user_input = input("Enter the number: ")

if user_input.isdigit():
    digits = number_to_list(user_input)
    result = fun1(digits)
    print(f"Result: {result}")
else:
    print("Error: The entered number is not an integer.")
