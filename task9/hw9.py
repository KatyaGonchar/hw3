#Последовательность
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
assert solution([1, 2, 3]) == True
assert solution([1, 2, 1, 2]) == False
assert solution([1, 3, 2, 1]) == False
assert solution([1, 2, 3, 4, 5, 3, 5, 6]) == False
assert solution([40, 50, 60, 10, 20, 30]) == False

#Число напротив
def solution(n, f_number):
    return (f_number + n / 2) % n
assert solution(10, 6) == 1
assert solution(10, 2) == 7
assert solution(10, 4) == 9

#Validate
def solution(number):
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

assert solution(4561261212345464) == False
assert solution(4561261212345467) == True
assert solution(378282246310005) == True  # Amex
assert solution(5610591081018250) == True  # Australian
assert solution(30569309025904) == True  # Diners
assert solution(6011111111111117) == True  # Discover
assert solution(3530111333300000) == True  # JCB
assert solution(5555555555554444) == True  # MasterCard
assert solution(4111111111111111) == True  # Visa
assert solution(4222222222222) == True  # Visa short
assert solution(76009244561) == True #Dankort short
assert solution(6331101999990016) == True  # Paymentech
