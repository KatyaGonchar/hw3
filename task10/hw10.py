# Строки с заданным символом
def solution(text):
    result = ""

    for i in text:
        if i == "#":
            result = result[:-1]
        else:
            result += i

    return result


assert solution("a#bc#d") == "bd"
assert solution("abc#d##c") == "ac"
assert solution("abc##d######") == ""
assert solution("#######") == ""
assert solution("") == ""

# Свечи

def solution1(candle_number, make_new):
    burnt = candle_number
    remains = candle_number

    while remains >= make_new:
        new_candles = remains // make_new
        burnt += new_candles
        remains = remains % make_new + new_candles

    return burnt


assert solution1(5, 2) == 9
assert solution1(1, 2) == 1
assert solution1(15, 5) == 18
assert solution1(12, 2) == 23
assert solution1(6, 4) == 7
assert solution1(13, 5) == 16
assert solution1(2, 3) == 2

# Подсчет количества букв
def solution2(text):
    if not text:
        return ""

    shrt = ""
    i = 0

    while i < len(text):
        count = 1
        while i < len(text) - 1 and text[i] == text[i + 1]:
            count += 1
            i += 1
        if count > 1:
            shrt += text[i] + str(count)
        else:
            shrt += text[i]
        i += 1

    return shrt


assert solution2("cccbba") == "c3b2a"
assert solution2("abeehhhhhccced") == "abe2h5c3ed"
assert solution2("aaabbceedd") == "a3b2ce2d2"
assert solution2("abcde") == "abcde"
assert solution2("aaabbdefffff") == "a3b2def5"
assert solution2("") == ""
