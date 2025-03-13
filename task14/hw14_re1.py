# Re: 1

import re

filename = "regex_1.txt"


def find_dates_txt(filename):

    date_pattern = r"\b\d{2}\.\d{2}\.\d{4}\b"

    try:
        with open(filename, "r") as file:
            content = file.read()

            dates = re.findall(date_pattern, content)

            if dates:
                print("Found dates in dd.mm.yyyy format:")
                for date in dates:
                    print(date)
            else:
                print("The dates are not found.")

    except FileNotFoundError:
        print(f"The file {filename} is not found.")
    except Exception as e:
        print(f"Error: {e}")


find_dates_txt(filename)
