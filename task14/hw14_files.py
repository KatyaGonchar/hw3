# Files

import os

filename = "students.txt"

if not os.path.exists(filename):  # if no file in local directory,\
    # create with data below
    print("No file found. Creating a new one.")
    with open(filename, "w") as file:
        file.write("Verstappen M., F1-01, 5 4 5\n")
        file.write("Hamilton L., F1-02, 4 4 4\n")
        file.write("Alonso F., F1-03, 3 2 4\n")
        file.write("Rosberg N., F1-03, 4 4 3\n")
        file.write("Vettel S., F1-02, 1 1 1\n")
        file.write("Raikkonen K., F1-03, 3 4 4\n")

with open(filename, "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines):  # if the program was executed before,\
    # wipe the results of previous calculations
    if line.startswith("Total number of students:"):
        lines = lines[:i]
        break

lines = [line for line in lines if line.strip()]

with open(filename, "w") as file:
    file.writelines(lines)

students = []
groups: dict[str, list[int]] = {}

for line in lines:
    line = line.strip()

    try:
        name, group, grades_str = line.split(", ")
        grades = [int(grade) for grade in grades_str.split()]
        students.append((name, group, grades))

        if group not in groups:
            groups[group] = []
        groups[group].extend(grades)
    except ValueError:
        print(f"Error in line: {line}")
        continue

total_students = len(students)

students_per_group = {}
for student in students:
    group = student[1]
    if group not in students_per_group:
        students_per_group[group] = 0
    students_per_group[group] += 1

avg_grades_per_group = {}
for group, grades in groups.items():
    avg_grades_per_group[group] = round(sum(int(grade) for grade in grades) / len(grades), 2)

print(f"Total number of students: {total_students}")
print("Students by groups:")
for group, count in students_per_group.items():
    print(f"{group}: {count}")
print("Average group score:")
for group, avg in avg_grades_per_group.items():
    print(f"{group}: {avg}")

with open(filename, "a") as file:
    file.write(f"\nTotal number of students: {total_students}\n")
    file.write("Students by groups:\n")
    for group, count in students_per_group.items():
        file.write(f"{group}: {count}\n")
    file.write("Average group score:\n")
    for group, avg in avg_grades_per_group.items():
        file.write(f"{group}: {avg}\n")
