import RPi.GPIO as GPIO
import time
import random

# GPIO Pins for LEDs and buttons
led_pins = [2, 3, 4, 17, 27, 22, 10, 9, 11]
button_pins = [14, 15, 18, 23, 24, 25, 8, 7, 1]

# Button to LED mapping
button_to_led_mapping = {14: 2, 15: 3, 18: 4, 23: 17, 24: 27, 25: 22, 8: 10, 7: 9, 1: 11}

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Game variables
score = 0
lives = 3
cooldown = 0.4
debug = True  # Debugging enabled
hit_milestone = 10  # every 10 successful hits
decay_rate_duration = 0.5  # 50% reduction for light duration
decay_rate_interval = 0.8  # 80% reduction for interval
initial_max_light_on_time = 3
initial_max_wait_time = 4
min_light_on_time = 0.5
min_wait_time = 1

def debug_print(message):
    if debug:
        print(message)

def light_up_led(index):
    GPIO.output(led_pins[index], True)
    debug_print(f"LED on pin {led_pins[index]} is lit.")
    return time.time()

def turn_off_led(index):
    GPIO.output(led_pins[index], False)
    debug_print(f"LED on pin {led_pins[index]} is off.")

def get_time_values(score):
    """ Calculate the current maximum wait time and light on time based on the score """
    rounds = score // hit_milestone
    current_max_light_on_time = max(initial_max_light_on_time * (decay_rate_duration ** rounds), min_light_on_time)
    current_max_wait_time = max(initial_max_wait_time * (decay_rate_interval ** rounds), min_wait_time)
    return current_max_light_on_time, current_max_wait_time

def game_loop():
    global score, lives

    try:
        while lives > 0:
            current_max_light_on_time, current_max_wait_time = get_time_values(score)
            led_index = random.randint(0, len(led_pins) - 1)
            light_on_time = random.uniform(1, current_max_light_on_time)
            wait_time = random.uniform(1, current_max_wait_time)

            # Light up a random LED
            start_time = light_up_led(led_index)
            led_on = True

            # Wait for the player to press the button or time out
            while time.time() - start_time < light_on_time:
                for button_pin, led_pin_assigned in button_to_led_mapping.items():
                    if led_pin_assigned == led_pins[led_index] and GPIO.input(button_pin) == GPIO.LOW:
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

            if led_on:
                turn_off_led(led_index)
                lives -= 1
                print(f"Missed! Lives left: {lives}")

            time.sleep(0.1)
            for button_pin in button_pins:
                if GPIO.input(button_pin) == GPIO.LOW:
                    led_pin_assigned = button_to_led_mapping[button_pin]
                    if led_pin_assigned != led_pins[led_index] or not led_on:
                        if time.time() - start_time < light_on_time + cooldown:
                            continue
                        lives -= 1
                        debug_print(f"Wrong button on pin {button_pin} pressed.")
                        print(f"Wrong button! Lives left: {lives}")

            time.sleep(wait_time - 0.1)

    finally:
        GPIO.cleanup()
        print(f"Game over! Your final score is: {score}")

if __name__ == "__main__":
    print("Welcome to the Gopher Game!")
    input("Press Enter when ready to start...")
    game_loop()
