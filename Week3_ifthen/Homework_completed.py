import random

# Welcome the user and ask for their name
print("Welcome to the Quiz Game!")
user_name = input("What's your name? ")
print(f"Great, {user_name}! Let's start the quiz.")

# Initialize the score
score = 0

# Question 1
print("\nQuestion 1: What is the capital of France?")
print("A) London")
print("B) Berlin")
print("C) Paris")
user_answer = input("Your answer: ")

# Check the answer for Question 1
if user_answer == "C":
    print(f"Correct, {user_name}!")
    score = score + 1
else:
    print(f"Sorry, {user_name}. The correct answer is C) Paris.")

# Question 2
print("\nQuestion 2: What is the largest planet in our solar system?")
print("A) Earth")
print("B) Mars")
print("C) Jupiter")
user_answer = input("Your answer: ")

# Check the answer for Question 2
if user_answer == "C":
    print(f"Correct, {user_name}!")
    score = score + 1
else:
    print(f"Sorry, {user_name}. The correct answer is C) Jupiter.")

# Question 3
print("\nQuestion 3: Who wrote the play 'Romeo and Juliet'?")
print("A) Charles Dickens")
print("B) William Shakespeare")
print("C) Jane Austen")
user_answer = input("Your answer: ")

# Check the answer for Question 3
if user_answer == "B":
    print(f"Correct, {user_name}!")
    score = score + 1
else:
    print(f"Sorry, {user_name}. The correct answer is B) William Shakespeare.")

# Display the final score
print(f"\nYour score: {score} out of 3. Well done!")
