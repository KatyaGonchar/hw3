def fun2(value):
    value = str(value)

    if value == value[::-1]:
        return True
    else:
        return False


user_input = input("Enter a string or number: ")

if fun2(user_input):
    print(f"'{user_input}' — It's a palindrome")
else:
    print(f"'{user_input}' — This is not a palindrome")
