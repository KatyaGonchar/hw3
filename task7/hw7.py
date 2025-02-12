# homework7
# time
n = int(input("Введите показания таймера: "))
h = (n // 60) % 24
m = n % 60
sum_time = (h // 10) + (h % 10) + (m // 10) + (m % 10)
print(sum_time)

# level up
experience = int(input("Введите опыт: "))
threshold = int(input("Введите порог: "))
reward = int(input("Введите награду: "))
result = (experience + reward) >= threshold
print(result)

# time converter
time = input("Введите время ЧЧ:ММ: ")
hours, minutes = time.split(":")
hours = int(hours)
minutes = int(minutes)
if hours < 12:
    period = "a.m."
else:
    period = "p.m."
if hours == 0:
    hours = 12
elif hours > 12:
    hours -= 12
if hours < 10:
    print(f"{hours}:{minutes:02} {period}")
else:
    print(f"{hours}:{minutes:02} {period}")