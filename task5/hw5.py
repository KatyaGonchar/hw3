# task1
text = "www.my_site.com#about"
print(text.replace("#", "/"))
# task2
S1 = "test"
S2 = "sleep"
S3 = "repeat"
S4 = "ing"
print(S1 + S4, S2 + S4, S3 + S4)
# task3
name = "Ivanou Ivan"
name1 = name.split()
new_name = name1[1] + " " + name1[0]
print(new_name)
# task4
sample_string = " String with tabs "
print(sample_string.strip())
print(sample_string.lstrip())
print(sample_string.rstrip())
# task5
text1 = "pARiS"
print(text1.capitalize())
# task6
text2 = "Robin Singh"
text3 = text2.split()
print(text3)
# task7
text4 = "I love arrays they are my favorite"
text5 = text4.split()
print(text5)
# task8
name2 = ["Ivan", "Ivanou"]
city = "Minsk"
country = "Belarus"
print(f"Привет, {name2[0]} {name2[1]}! Добро пожаловать в {city} {country}")
# task9
text6 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
text7 = " ".join(text6)
print(text7)
# task10
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1.insert(2, 11)
del list1[6]
print(list1)
