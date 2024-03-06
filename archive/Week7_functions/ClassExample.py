# ClassExample.py

# Introduction to Functions
# In this section, we are introducing what functions are and why they are useful.

# A simple example of a function that greets a person.
def greet(name):
    """
    This function takes a name as an argument and prints a greeting message.
    """
    print("Hello, " + name + "! Welcome to the Joke Factory!")

# Let's call the greet function with a name.
greet("Alex")

# Defining and Calling Functions
# Here, we are going to learn how to define functions, pass arguments, and return values.

# A function that adds two numbers and returns the result.
def add_numbers(num1, num2):
    """
    This function takes two numbers, adds them together, and returns the result.
    """
    result = num1 + num2
    return result

# Calling the add_numbers function and printing the result.
sum_result = add_numbers(5, 7)
print("The sum of 5 and 7 is:", sum_result)

# Activity: Create Your Own Functions
# Students will create their own functions based on the instructions provided.

# A function to calculate the area of a rectangle.
def calculate_area(length, width):
    """
    This function takes the length and width of a rectangle and returns the area.
    """
    area = length * width
    return area

# Testing the calculate_area function.
rectangle_area = calculate_area(10, 5)
print("The area of the rectangle is:", rectangle_area)

# A function to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    """
    This function takes a temperature in Celsius, converts it to Fahrenheit, and returns the result.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Testing the celsius_to_fahrenheit function.
temperature_in_fahrenheit = celsius_to_fahrenheit(25)
print("25 degrees Celsius is:", temperature_in_fahrenheit, "degrees Fahrenheit")

# Function Best Practices
# Discussing and demonstrating some best practices when writing functions.

# A well-named function that calculates the average of two numbers.
def calculate_average(number1, number2):
    """
    This function takes two numbers, calculates their average, and returns the result.
    The function name is descriptive, and the code is commented for clarity.
    """
    average = (number1 + number2) / 2
    return average

# Assignment: Improve Your Quiz Game with Functions
# Encouraging students to refactor their quiz game using functions.

# Below is a simplified example of a quiz game broken down into functions.
def get_question():
    """
    This function returns a sample question and its answer.
    """
    return "What is the capital of France?", "Paris"

def check_answer(question, correct_answer):
    """
    This function takes a question and its correct answer,
    asks the user the question, and checks if the answer is correct.
    """
    user_answer = input(question + " ")
    if user_answer.lower() == correct_answer.lower():
        print("Correct! Great job!")
    else:
        print("Oops! The correct answer was:", correct_answer)

def play_game():
    """
    This function controls the game flow.
    """
    question, correct_answer = get_question()
    check_answer(question, correct_answer)
    again = input("Do you want to play again? (yes/no) ")
    if again.lower() == "yes":
        play_game()

# Starting the game
play_game()

# Closing Remarks and Homework Assignment
# Please refer back to the lesson plan for closing remarks and the homework assignment.


