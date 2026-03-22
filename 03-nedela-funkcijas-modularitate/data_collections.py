# --- A daļa — Saraksti ---
print("--- Lists ---")

numbers = [2, 4, 6, 8, 10]

# add element
numbers.append(12)
print(f"After append: {numbers}")

# remove element
# Удаляем последний элемент
removed_number = numbers.pop()
print(f"After pop: {numbers}")
print(f"Removed number: {removed_number}")


#average and count
total = 0
count = 0

for number in numbers:
    total += number
    count += 1
average = total / count



