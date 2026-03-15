import sys

# pārbaude: vai N ir norādīts
if len(sys.argv) < 2:
    print("Lūdzu norādiet skaitli N.")
    sys.exit()

# pārbaude: vai N ir skaitlis
try:
    N = int(sys.argv[1])
except ValueError:
    print("N jābūt veselam skaitlim.")
    sys.exit()

# fizzbuzz cikls
for i in range(1, N + 1):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)