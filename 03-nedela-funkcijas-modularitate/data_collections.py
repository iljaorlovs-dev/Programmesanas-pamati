# --- Part A — Lists ---
print("--- Lists ---")

numbers = [2, 4, 6, 8, 10]

# Add an element
numbers.append(12)

# Remove the last element
removed_number = numbers.pop()

print(f"Original list after append() and pop(): {numbers}")
print(f"Removed element: {removed_number}")

# Manually calculate the sum and count of elements
total = 0
count = 0

for number in numbers:
    total += number
    count += 1

average = total / count

print(f"Sum: {total}, Average: {average}")

# Filter only even numbers
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(f"Even numbers: {even_numbers}")

# Slices
first_three = numbers[:3]
last_two = numbers[-2:]
every_second = numbers[::2]

print(f"First 3: {first_three}")
print(f"Last 2: {last_two}")
print(f"Every second element: {every_second}")


# --- Part B — Dictionaries ---
print("\n--- Dictionaries ---")

students = {
    "Anna": 85,
    "Jānis": 72,
    "Līga": 95
}

# Add a new student
students["Pēteris"] = 88
print(f"Students after adding Pēteris: {students}")

# Update existing grades
students["Jānis"] = 78
students["Pēteris"] = 99

# Print all students and their grades
for name, grade in students.items():
    print(f"{name}: {grade}")

# Find the best student manually
best_name = ""
best_grade = -1

for name, grade in students.items():
    if grade > best_grade:
        best_name = name
        best_grade = grade

print(f"Best student: {best_name} ({best_grade})")


# --- Part C — Combination ---
print("\n--- Students with grade >= 80 ---")

student_list = [
    {"name": "Anna", "grade": 85},
    {"name": "Jānis", "grade": 78},
    {"name": "Līga", "grade": 95},
    {"name": "Pēteris", "grade": 99}
]

good_students = []

for student in student_list:
    if student["grade"] >= 80:
        good_students.append(student)

for index, student in enumerate(good_students, start=1):
    print(f"{index}. {student['name']} — {student['grade']}")