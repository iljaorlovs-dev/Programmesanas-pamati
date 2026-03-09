# datu tipi
text1 = "World, hold on!"     
text2 = "We are children of the future"
number1 = 88
number2 = 69
laba_temperatura = 36.6
mana_temperatura = 38.0
temperatura_OK = True
empty_value = None

# datu izvade ar type
print("text1 type:", type(text1))
print("text2 type:", type(text2))
print("number1 type:", type(number1))
print("number2 type:", type(number2))
print("laba_temperatura type:", type(laba_temperatura))
print("mana_temperatura type:", type(mana_temperatura))
print("temperatura_OK type:", type(temperatura_OK))
print("empty_value type:", type(empty_value))

# piemeri
print("9" + "9")

# This conversion will fail - abc is not int
# print(int("abc"))

# Truthy / falsy examples
print(bool(""))        # False - tukša virkne (empty string)
print(bool(" "))       # True - atstarpe ir simbols (space is still a character)
print(bool(0))         # False - nulle tiek uzskatīta par False
print(bool("0"))         # True, jo 0 ir teksts))== :)
print(bool(10))        # True - jebkurš cits skaitlis nav nulle
print(bool(None))      # False - None nozīmē "nav vērtības"

# bool ir int apakšklase Python
print(True + True)     # 2, jo True = 1
print(False + 5)       # 5, jo False = 0


# Explicit type conversions

print("5" + "3")          # "53" - virkņu savienošana (string concatenation)

#print("5" + 3)          # TypeError - Python nevar savienot string un int

print(int("5") + 3)       # 8 - string tiek pārveidots par int

print(float("3.14"))      # 3.14 - string -> float

print(int(3.86))          # 3 - int nogriež decimāldaļu (no rounding)

# Edge cases
# print(int("abc"))       # ValueError - nevar pārveidot tekstu par skaitli

# Divpakāpju konversija
print(int(float("3.14"))) # 3
print(int(round(3.86))) #4


# Interesting Python behaviour

print(bool("0"))        # True - netukša virkne
print(True * 10)        # 10 - True = 1
print(True + True)      # 2
print(round(2.5))       # 2
print(round(3.5))       # 4
print(0.1 + 0.2 == 0.3) # False - floating point precision


#OTHER
if mana_temperatura > laba_temperatura:
    print("Temperature is not OK")
else:
    print("Temperature is OK")