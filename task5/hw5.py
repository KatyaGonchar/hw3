#task1 - Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
text = "www.my_site.com#about"
print(text.replace("#","/"))
#task2 - Напишите программу, которая добавляет ‘ing’ к словам
S1 = "test"
S2 = "sleep"
S3 = "repeat"
S4 = "ing"
print(S1 + S4, S2 + S4, S3 + S4)
#task3 - В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
name = "Ivanou Ivan"
name1 = name.split()
new_name = name1[1] + " " + name1[0]
print(new_name)
#task4 - Напишите программу которая удаляет пробел в начале, в конце строки
sample_string = " String with tabs "
print(sample_string.strip())
print(sample_string.lstrip())
print(sample_string.rstrip())
#task5 - Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы. Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris"
text1 = "pARiS"
print(text1.capitalize())
#task6 - Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
text2 = "Robin Singh"
text3 = text2.split()
print(text3)
#task7 - "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
text4 = "I love arrays they are my favorite"
text5 = text4.split()
print(text5)
#task8 - Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus. Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
name2 = ["Ivan", "Ivanou"]
city = "Minsk"
country = "Belarus"
print(f"Привет, {name2[0]} {name2[1]}! Добро пожаловать в {city} {country}")
#task9 - Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него строку => "I love arrays they are my favorite"
text6 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
text7 = " ".join(text6)
print(text7)
#task10 - Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1.insert(2, 11)
del list1[6]
print(list1)