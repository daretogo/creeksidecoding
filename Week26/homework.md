1) Define a function called display_menu() that will handle the main menu logic.
```
def display_menu():
    print("Welcome to the Button Games!")
    print("To play the Reaction Time game, press the 'L' button.")
    print("To play the Gopher game, press the 'R' button.")
    print("Please do not pound the buttons.")

```
2) Inside the display_menu() function, add code to light up the 'L' and 'R' buttons to indicate the game selection options.

```
def display_menu():
    # ... (existing print statements)
    control_led(LEFT_GAME_INDEX, True)  # Light up 'L' button
    control_led(RIGHT_GAME_INDEX, True)  # Light up 'R' button
```
3) Modify the main loop to call the display_menu() function and wait for user input.

```
while True:
    display_menu()
    # TODO: Check if a selection button is pressed
    # If 'L' button pressed, call reaction_time_game
    # If 'R' button pressed, call gopher_game
```
4) Inside the main loop, add code to detect button presses for the 'L' and 'R' buttons.

```
while True:
    display_menu()
    if detect_button(LEFT_GAME_INDEX):
        control_led(LEFT_GAME_INDEX, False)  # Turn off 'L' button
        control_led(RIGHT_GAME_INDEX, False)  # Turn off 'R' button
        reaction_time_game()
    elif detect_button(RIGHT_GAME_INDEX):
        control_led(LEFT_GAME_INDEX, False)  # Turn off 'L' button
        control_led(RIGHT_GAME_INDEX, False)  # Turn off 'R' button
        gopher_game()
```

5) Add placeholders for the reaction_time_game() and gopher_game() functions to print a message confirming the game was invoked.

```
def reaction_time_game():
    print("Reaction Time game would start now.")

def gopher_game():
    print("Gopher game would start now.")
```
6) (Optional) Add constants for the 'L' and 'R' button indices to make the code more readable.
 
```
LEFT_GAME_INDEX = 0
RIGHT_GAME_INDEX = 1
```

7) (Optional) Add a small delay after turning off the 'L' and 'R' buttons to give a brief pause before starting the selected game.

```
if detect_button(LEFT_GAME_INDEX):
    # ... (existing code)
    time.sleep(0.5)  # Small delay before starting the game
    reaction_time_game()
elif detect_button(RIGHT_GAME_INDEX):
    # ... (existing code)
    time.sleep(0.5)  # Small delay before starting the game
    gopher_game()
```

By following these steps, you will have a functional menu system that displays the game options, lights up the 'L' and 'R' buttons, and launches the appropriate game based on the user's selection. 

Obviosly without the buttons wired up you won't be able to fully use this until we are in class and you have access to the buttons. 