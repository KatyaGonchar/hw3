# Re: 2

import re


def validate_password(password):

    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{4,}$'

    if re.match(pattern, password):
        return True
    return False


password = input("Enter password: ")
while not validate_password(password):
    print("The password is not suitable. Try again.")
    password = input("Enter password: ")

print("The password is suitable.")
