

# Section 4: Guess the Number Game
# We'll create a simple number guessing game using comparison operators.

import random

secret_number = random.randint(1, 50)

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 50. Can you guess it?")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Higher! Try again.")
    elif guess > secret_number:
        print("Lower! Try again.")
    else:
        print(f"Congratulations! You guessed the secret number {secret_number}.")
        break

# That's it for today's lesson! We've covered variables, f-strings, if/then statements, and comparison operators.
# Keep practicing, and you'll become a Python pro in no time!
