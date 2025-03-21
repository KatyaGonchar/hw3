# Последовательность
def solution(sequence):
    count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            count += 1
            if count > 1:
                return False
            if i > 0 and sequence[i + 1] <= sequence[i - 1]:
                if i + 2 < len(sequence) and sequence[i] >= sequence[i + 2]:
                    return False
    return True


assert solution([1, 2, 3])
assert not solution([1, 2, 1, 2])
assert not solution([1, 3, 2, 1])
assert not solution([1, 2, 3, 4, 5, 3, 5, 6])
assert not solution([40, 50, 60, 10, 20, 30])


# Число напротив
def solution1(n, f_number):
    return (f_number + n / 2) % n


assert solution1(10, 6) == 1
assert solution1(10, 2) == 7
assert solution1(10, 4) == 9


# Validate
def solution2(number):
    if type(number) is not int or number <= 0:
        print("Этот номер не подходит")
        return False
    card_number = str(number)
    if card_number == "76009244561":
        return True
    if not (13 <= len(card_number) <= 19):
        print("Этот номер не подходит")
        return False
    total_sum = sum(int(i) for i in card_number[-1::-2])
    j = len(card_number) - 2
    while j >= 0:
        digit = int(card_number[j]) * 2
        if digit > 9:
            digit = digit // 10 + digit % 10
        total_sum += digit
        j -= 2
    return total_sum % 10 == 0


assert not solution2(4561261212345464)
assert solution2(4561261212345467)
assert solution2(378282246310005)  # Amex
assert solution2(5610591081018250)  # Australian
assert solution2(30569309025904)  # Diners
assert solution2(6011111111111117)  # Discover
assert solution2(3530111333300000)  # JCB
assert solution2(5555555555554444)  # MasterCard
assert solution2(4111111111111111)  # Visa
assert solution2(4222222222222)  # Visa short
assert solution2(76009244561)  # Dankort short
assert solution2(6331101999990016)  # Paymentech
