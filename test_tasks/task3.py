def calculate_sum(number):
    total = 0
    for i in range(1, number + 1):
        total += i
    return total


assert calculate_sum(1) == 1
assert calculate_sum(2) == 3
assert calculate_sum(8) == 36
assert calculate_sum(8) == 36
assert calculate_sum(22) == 253
assert calculate_sum(100) == 5050
