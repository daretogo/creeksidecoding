# Import necessary libraries
import RPi.GPIO as GPIO  # This library allows you to control the GPIO pins on a Raspberry Pi
import time              # This library helps you handle time-related tasks, like waiting
import random            # This library lets you generate random numbers

# GPIO Pins for LEDs and buttons
led_pins = [2, 3, 4, 17, 27, 22, 10, 9, 11]  # These numbers represent the GPIO pins where LEDs are connected
button_pins = [14, 15, 18, 23, 24, 25, 8, 7, 1]  # These numbers represent the GPIO pins where buttons are connected

# Button to LED mapping
button_to_led_mapping = {14: 2, 15: 3, 18: 4, 23: 17, 24: 27, 25: 22, 8: 10, 7: 9, 1: 11}  # Maps each button pin to its corresponding LED pin

# Setup GPIO
GPIO.setmode(GPIO.BCM)  # Set the GPIO numbering scheme to BCM (Broadcom SOC channel)
GPIO.setwarnings(False)  # Disable warnings

# Configure each pin where an LED is connected
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)  # Set each LED pin as an output
    GPIO.output(pin, False)  # Start with each LED turned off
 
# Configure each pin where a button is connected
for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set each button pin as an input with a pull-up resistor

# Game variables
score = 0  # Initialize score
lives = 1  # Start with 3 lives
cooldown = 0.4  # Cooldown period to prevent accidental button presses
debug = True  # If true, additional debug information will be printed
hit_milestone = 10  # Update timing variables every 10 successful hits
decay_rate_duration = 0.9 # Light duration decreases by 50% per milestone
decay_rate_interval = 0.9  # Wait interval decreases by 80% per milestone
initial_max_light_on_time = 1 # Max initial duration for an LED to be on
initial_max_wait_time = 2 # Max initial time to wait before lighting up another LED
min_light_on_time = 0.5  # Minimum time an LED can be on
min_wait_time = 2   # Minimum time to wait before lighting up another LED

def debug_print(message):
    """ Print debug messages if debugging is enabled. """
    if debug:
        print(message)

def light_up_led(index):
    """ Light up the LED at the given index and return the start time. """
    GPIO.output(led_pins[index], True)  # Turn on the LED
    debug_print(f"LED on pin {led_pins[index]} is lit.")
    return time.time()  # Return the current time

def turn_off_led(index):
    """ Turn off the LED at the given index. """
    GPIO.output(led_pins[index], False)  # Turn off the LED
    debug_print(f"LED on pin {led_pins[index]} is off.")

def get_time_values(score):
    """ Calculate the current maximum wait time and light on time based on the score. """
    rounds = score // hit_milestone  # Determine how many milestones have been reached
    current_max_light_on_time = max(initial_max_light_on_time * (decay_rate_duration ** rounds), min_light_on_time)
    current_max_wait_time = max(initial_max_wait_time * (decay_rate_interval ** rounds), min_wait_time)
    return current_max_light_on_time, current_max_wait_time

def game_loop():
    """ The main game loop where all the gameplay happens. """
    global score, lives  # Use the global score and lives variables

    try:
        while lives > 0:  # Keep playing until all lives are lost
            # Get current timing values based on score
            current_max_light_on_time, current_max_wait_time = get_time_values(score)
            led_index = random.randint(0, len(led_pins) - 1)  # Choose a random LED
            light_on_time = random.uniform(1, current_max_light_on_time)  # Randomize how long the LED will be on
            wait_time = random.uniform(1, current_max_wait_time)  # Randomize how long to wait before lighting another LED

            # Light up a random LED
            start_time = light_up_led(led_index)
            led_on = True  # Mark the LED as on

            # Wait for the player to press the correct button or for the time to run out
            while time.time() - start_time < light_on_time:
                for button_pin, led_pin_assigned in button_to_led_mapping.items():
                    if led_pin_assigned == led_pins[led_index] and GPIO.input(button_pin) == GPIO.LOW:  # Check if the correct button is pressed
                        score += 1  # Increase the score
                        debug_print(f"Correct button on pin {button_pin} pressed.")
                        print(f"Good hit! Score: {score}")
                        turn_off_led(led_index)  # Turn off the LED
                        led_on = False  # Mark the LED as off
                        time.sleep(0.1)  # Debounce delay
                        break
                if not led_on:  # Exit the loop if the LED is already off
                    break
                time.sleep(0.01)  # Brief pause to reduce CPU usage

            if led_on:  # If the LED is still on after the allowed time
                turn_off_led(led_index)  # Turn it off
                lives -= 1  # Lose a life
                print(f"Missed! Lives left: {lives}")

            time.sleep(0.1)  # Short pause after each round
            for button_pin in button_pins:
                if GPIO.input(button_pin) == GPIO.LOW:  # Check if any button is pressed
                    led_pin_assigned = button_to_led_mapping[button_pin]
                    if led_pin_assigned != led_pins[led_index] or not led_on:  # Check if the wrong button is pressed or if it's pressed too late
                        if time.time() - start_time < light_on_time + cooldown:
                            continue
                        lives -= 1  # Lose a life
                        debug_print(f"Wrong button on pin {button_pin} pressed.")
                        print(f"Wrong button! Lives left: {lives}")

            time.sleep(wait_time - 0.1)  # Wait before the next round

    finally:
        GPIO.cleanup()  # Clean up GPIO to reset everything
        print(f"Game over! Your final score is: {score}")

if __name__ == "__main__":
    print("Welcome to the Gopher Game!")
    input("Press Enter when ready to start...")  # Wait for the player to be ready
    game_loop()  # Start the game loop
