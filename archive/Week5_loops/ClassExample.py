#REMINDER:  anything you want to save and keep long term - keep it OUTSIDE tthe creeksidecoding folder. 


# Modules!
# modules are bits of code that somebody else has written that has usefull REUSEABLE functionality so we import
# so we can make use of that functionality. 

import random  # Import the random module

# Generate a random integer between 1 and 100 and assign it to a variable
random_number = random.randint(1, 100)
print(f"Random number generated: {random_number}")




# Example 1: Comparing strings using if statements
newguy = input("Enter your name: ")
if newguy == "Fred":
    print("Hey Fred, I know you!")
else:
    print("Hello, stranger!")

# Example 2: Comparing integers using if statements
age = int(input("Enter your age: "))
if age >= 12:
    print("Oh, please come on in.")
else:
    print("Sorry, this isn't for babies.")

# Example 3: Using a while loop to print a range of numbers
print("Printing numbers from 1 to 10:")
number = 1
while number <= 10:
    print(number)
    number = number + 1

# Example 4: Using a while loop to check user age until valid
while True:
    age = int(input("How old are you? "))
    if age >= 12:
        print("Oh, please come on in.")
        break
    else:
        print("Sorry, this isn't for babies.")

# Example 5: Using a while loop with a variable condition
condition = True
while condition:
    user_input = input("Do you want to continue (yes/no)? ")
    if user_input.lower() == "no":
        condition = False  # Set condition to False to exit the loop

# Example 6: Using a while loop with a variable condition and break
while True:
    user_input = input("Do you want to continue (yes/no)? ")
    if user_input.lower() == "no":
        break  # Break out of the infinite loop
