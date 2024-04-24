import RPi.GPIO as GPIO
import time
import random

# Constants for game selection
LEFT_GAME = '0'
RIGHT_GAME = '2'

# LED pins
led_pins = [2, 3, 4, 17, 27, 22, 10, 9, 11]

# Button pins
button_pins = [14, 15, 18, 23, 24, 25, 8, 7, 1]

# Initialize GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up LEDs
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

# Set up buttons
for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Function to control LEDs
def control_led(led_index, state):
    GPIO.output(led_pins[led_index], state)

# Function to detect button presses
def detect_button(button_index):
    return GPIO.input(button_pins[button_index])

# Function to implement the gopher game
def gopher_game():
    lives = 3  # Initialize lives
    score = 0  # Initialize score

    while lives > 0:
        # Randomly choose a button to light up
        lit_button = random.randint(0, len(button_pins) - 1)
        control_led(lit_button, GPIO.HIGH)  # Light up the button

        # Randomly choose the duration for the button to be lit
        lit_duration = random.uniform(1, 3)
        time.sleep(lit_duration)

        # Check if the lit button is pressed
        if detect_button(lit_button) == GPIO.HIGH:
            score += 1  # Increase score if the correct button is pressed
            print("Correct! Score: ", score)
        else:
            lives -= 1  # Decrease lives if the wrong button is pressed
            print("Wrong! Lives: ", lives)

        # Turn off the lit button
        control_led(lit_button, GPIO.LOW)

        # Check if any other button is pressed
        for index, pin in enumerate(button_pins):
            if index != lit_button and detect_button(index) == GPIO.HIGH:
                lives -= 1  # Decrease lives if any other button is pressed
                print("Lost a life! Lives: ", lives)

        # Check if the game is over
        if lives == 0:
            print("Game over! Your score was: ", score)
            break

# Main loop
try:
    while True:
        # Check if a selection button is pressed
        if detect_button(int(LEFT_GAME)) == GPIO.HIGH:
            # reaction_time_game()  # Call reaction_time_game if needed
            pass
        elif detect_button(int(RIGHT_GAME)) == GPIO.HIGH:
            gopher_game()  # Call gopher_game

except KeyboardInterrupt:
    # Clean up GPIO when done
    GPIO.cleanup()
