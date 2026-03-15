import random

while True:
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("\nI have chosen a number between 1 and 100.")
    print("You have 10 attempts to guess it.")

    while True:
        guess_input = input("Your guess: ")

        if not guess_input.isdigit():
            print("Please enter a valid integer.")
            continue

        guess = int(guess_input)
        attempts += 1

        if guess < secret_number:
            print("Too small.")
        elif guess > secret_number:
            print("Too large.")
        else:
            guessed = True
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

        if attempts >= 10:
            print(f"No attempts left, LOSER! The correct number was {secret_number}.")
            break

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()

    if play_again not in ("yes", "y"):
        print("Thanks for playing!")
        break