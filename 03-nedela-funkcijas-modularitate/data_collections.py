# --- A daļa — Saraksti ---
print("--- Lists ---")

numbers = [2, 4, 6, 8, 10]

# Добавляем элемент
numbers.append(12)

# Удаляем последний элемент
removed_number = numbers.pop()

print(f"Original list after append() and pop(): {numbers}")
print(f"Removed element: {removed_number}")

# Ручной подсчёт суммы и количества элементов
total = 0
count = 0

for number in numbers:
    total += number
    count += 1

average = total / count

print(f"Sum: {total}, Average: {average}")

# Фильтрация: только чётные числа
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(f"Even numbers: {even_numbers}")

# Срезы
first_three = numbers[:3]
last_two = numbers[-2:]
every_second = numbers[::2]

print(f"First 3: {first_three}")
print(f"Last 2: {last_two}")
print(f"Every second element: {every_second}")




# --- B daļa — Vārdnīcas ---
print("\n--- Dictionaries ---")
students = {
    "Anna": 85,
    "Jānis": 72,
    "Līga": 95
}
# Добавляем нового студента
students["Pēteris"] = 88
print(f"Students after adding Pēteris: {students}")

# Меняем существующую оценку
students["Jānis"] = 78
students["Pēteris"] = 99

# Вывод всех студентов
for name, grade in students.items():
    print(f"{name}: {grade}")


# Поиск лучшего студента вручную
best_name = ""
best_grade = -1

for name, grade in students.items():
    if grade > best_grade:
        best_name = name
        best_grade = grade

print(f"Best student: {best_name} ({best_grade})")



######## --- C daļa — Kombinācija --- ########################################
print("\n--- Students with grade >= 80 ---")

student_list = [
    {"name": "Anna", "grade": 85},
    {"name": "Jānis", "grade": 78},
    {"name": "Līga", "grade": 95},
    {"name": "Pēteris", "grade": 88}
]

good_students = []

for student in student_list:
    if student["grade"] >= 80:
        good_students.append(student)

for index, student in enumerate(good_students, start=1):
    print(f"{index}. {student['name']} — {student['grade']}")