# Re: 2

import re


def validate_password(password, pattern):

    if re.match(pattern, password):
        return True
    return False


pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{4,}$'
password = input("Enter password: ")

while not validate_password(password, pattern):
    print("The password is not suitable. Try again.")
    password = input("Enter password: ")

print("The password is suitable.")
