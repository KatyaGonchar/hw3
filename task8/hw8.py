# быки и коровы
secret = input("Загадано число: ")
guess = ""
while secret != guess:
    guess = input("Введите число (4 цифры): ")
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    if secret != guess:
        print(f"Коров: {cows}, Быков: {bulls}")
print("Вы выиграли!")

# пирамида
n = 10
i = 1
line = "*"
while i <= n:
    print((line.center(n * 2)))
    line += "**"
    i += 1

# статуи
a = [6, 2, 3, 8]
m1 = min(a)
m2 = max(a)
b = 0
c = ""
for i in range(m1, m2 + 1):
    if i not in a:
        if c == "":
            c = str(i)
        else:
            c = c + ", " + str(i)
        b +=1
print("Всего нет статуй:", b, "\nУ Вас отсутствуют статуи размеров:", c)
