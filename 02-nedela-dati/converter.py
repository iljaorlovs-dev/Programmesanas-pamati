#############CONSTANTS###########
KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
USD_TO_EUR = 0.84235020

#Selection menu
print("Izvēlies konversiju:")
print("1) km <-> mi")
print("2) kg <-> lb")
print("3) L <-> gal")
print("4) USD <-> EUR")

#Asking user
conversion = input("> ")




#Direction and error message
if conversion == "1":
    coefficient = KM_TO_MI
    unit1 = "km"
    unit2 = "mi"
elif conversion == "2":
    coefficient = KG_TO_LB
    unit1 = "kg"
    unit2 = "lb"
elif conversion == "3":
    coefficient = L_TO_GAL
    unit1 = "L"
    unit2 = "gal"
elif conversion == "4":
    coefficient = USD_TO_EUR
    unit1 = "USD"
    unit2 = "EUR"
else:
    print("Kļūda: nepareiza konversijas izvēle!")
    exit()

print(f"Virziens: 1) {unit1} -> {unit2}  2) {unit2} -> {unit1}")
direction = input("> ")

try:
    value = float(input("Ievadi vērtību: "))
except ValueError:
    print("Kļūda: jāievada skaitlis!")
    exit()

if direction == "1":
    result = value * coefficient
    print(f"{value:.2f} {unit1} = {result:.2f} {unit2}")
elif direction == "2":
    result = value / coefficient
    print(f"{value:.2f} {unit2} = {result:.2f} {unit1}")
else:
    print("Kļūda: nepareizs virziens!")