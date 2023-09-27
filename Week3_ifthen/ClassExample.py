# Welcome to the Python coding class! Today, we'll review variables and introduce if/then statements.

# Section 1: Variables and f-strings
# Let's set some variables and print them using f-strings.

name = "Alice"
age = 12
favorite_color = "blue"

print(f"Hello, my name is {name}. I am {age} years old, and my favorite color is {favorite_color}.")

# Section 2: If/Then Statements with String Comparison
# Now, let's introduce if/then statements with string comparison.

favorite_food = "pizza"

if favorite_food == "pizza":
    print("I love pizza too!")
else:
    print("That's not my favorite food.")

# Section 3: More Comparison Operators
# Let's explore other comparison operators like greater than, less than, and string contains.

number = 15

if number > 10:
    print("The number is greater than 10.")

if number < 20:
    print("The number is less than 20.")

text = "Python is fun!"

if "Python" in text:
    print("Python is mentioned in the text.")

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
