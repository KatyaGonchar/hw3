# Re: 3

import re


def fix_repeated_words(text):
    err_pattern = r'\b(\w+)\s+\1\b'
    corrected_text = re.sub(err_pattern, r'\1', text)

    return corrected_text


initial_text = "Довольно распространённая ошибка ошибка — это \
лишний повтор повтор слова слова. Смешно, не не правда ли? \
Не нужно портить хор хоровод."
corrected_text = fix_repeated_words(initial_text)

print(corrected_text)
