import RPi.GPIO as GPIO
import time
import random

# GPIO Pins for LEDs and buttons
led_pins = [2, 3, 4, 17, 27, 22, 10, 9, 11]
button_pins = [14, 15, 18, 23, 24, 25, 8, 7, 1]

# Button to LED mapping based on your diagnostic output
button_to_led_mapping = {14: 2, 15: 3, 18: 4, 23: 17, 24: 27, 25: 22, 8: 10, 7: 9, 1: 11}

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup LED pins as output and button pins as input with pull-up resistor
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Game variables
score = 0
lives = 3
cooldown = 0.4
debug = false  # Debugging enabled

def debug_print(message):
    if debug:
        print(message)

def light_up_led(index):
    GPIO.output(led_pins[index], True)
    debug_print(f"LED on pin {led_pins[index]} is lit.")
    return time.time()  # Return the time when the LED was lit

def turn_off_led(index):
    GPIO.output(led_pins[index], False)
    debug_print(f"LED on pin {led_pins[index]} is off.")

def game_loop():
    global score, lives

    try:
        while lives > 0:
            led_index = random.randint(0, len(led_pins) - 1)
            led_pin = led_pins[led_index]
            light_on_time = random.uniform(1, 3)
            wait_time = random.uniform(1, 4)

            # Light up a random LED
            start_time = light_up_led(led_index)
            led_on = True

            # Wait for the player to press the button or time out
            while time.time() - start_time < light_on_time:
                # Check the button that corresponds to the current LED
                for button_pin, led_pin_assigned in button_to_led_mapping.items():
                    if led_pin_assigned == led_pin and GPIO.input(button_pin) == GPIO.LOW:
                        score += 1
                        debug_print(f"Correct button on pin {button_pin} pressed.")
                        print(f"Good hit! Score: {score}")
                        turn_off_led(led_index)
                        led_on = False
                        time.sleep(0.1)  # Debounce delay
                        break
                if not led_on:
                    break
                time.sleep(0.01)

            if led_on:  # If the LED is still on, the player missed
                turn_off_led(led_index)
                lives -= 1
                print(f"Missed! Lives left: {lives}")

            # Delay to prevent immediate button press handling
            time.sleep(0.1)

            # Check for any button press during cooldown or incorrect button press
            for button_pin in button_pins:
                if GPIO.input(button_pin) == GPIO.LOW:
                    led_pin_assigned = button_to_led_mapping[button_pin]
                    if led_pin_assigned != led_pin or not led_on:
                        if time.time() - start_time < light_on_time + cooldown:
                            continue
                        lives -= 1
                        debug_print(f"Wrong button on pin {button_pin} pressed.")
                        print(f"Wrong button! Lives left: {lives}")

            # Wait before lighting up another LED
            time.sleep(wait_time - 0.1)

    finally:
        GPIO.cleanup()  # Reset GPIO settings on exit
        print(f"Game over! Your final score is: {score}")

if __name__ == "__main__":
    print("Welcome to the Gopher Game!")
    input("Press Enter when ready to start...")
    game_loop()
