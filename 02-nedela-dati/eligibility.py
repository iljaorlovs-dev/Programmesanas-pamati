# Age input with validation
while True:
    try:
        age = int(input("Ievadi vecumu: "))
        if age < 0:
            print("Vecums nevar būt negatīvs. Mēģini vēlreiz.")
        else:
            break
    except ValueError:
        print("Lūdzu, ievadi skaitli.")


# Driving license input: j/n -> bool
while True:
    driving_input = input("Vai ir autovadītāja apliecība? (j/n): ").strip().lower()
    if driving_input in ("j", "n"):
        has_driving_license = driving_input == "j"
        break
    else:
        print("Lūdzu, ievadi tikai 'j' vai 'n'.")


# Student input: j/n -> bool
while True:
    student_input = input("Vai ir students? (j/n): ").strip().lower()
    if student_input in ("j", "n"):
        is_student = student_input == "j"
        break
    else:
        print("Lūdzu, ievadi tikai 'j' vai 'n'.")


# Veteran input: j/n -> bool
while True:
    veteran_input = input("Vai ir veterāns? (j/n): ").strip().lower()
    if veteran_input in ("j", "n"):
        is_veteran = veteran_input == "j"
        break
    else:
        print("Lūdzu, ievadi tikai 'j' vai 'n'.")


# Eligibility rules
voting_ok = age >= 18
car_rental_ok = age >= 21 and has_driving_license
senior_discount_ok = age >= 65 or is_veteran
student_discount_ok = 16 <= age <= 26 and is_student


# Extra explanation for car rental
if car_rental_ok:
    car_rental_text = "Jā ✓"
elif age < 21 and not has_driving_license:
    car_rental_text = "Nē ✗ (par jaunu un nav apliecības)"
elif age < 21:
    car_rental_text = "Nē ✗ (par jaunu)"
else:
    car_rental_text = "Nē ✗ (nav apliecības)"


# Final output
print("---")
print(f"Balsošana:         {'Jā ✓' if voting_ok else 'Nē ✗'}")
print(f"Auto īre:          {car_rental_text}")
print(f"Senioru atlaide:   {'Jā ✓' if senior_discount_ok else 'Nē ✗'}")
print(f"Studentu atlaide:  {'Jā ✓' if student_discount_ok else 'Nē ✗'}")