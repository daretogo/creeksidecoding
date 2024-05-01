import RPi.GPIO as GPIO
import time
import random

# GPIO Pins for LEDs and buttons
led_pins = [2, 3, 4, 17, 27, 22, 10, 9, 11]
button_pins = [14, 15, 18, 23, 24, 25, 8, 7, 1]

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup LED pins as output
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

# Setup button pins as input with pull-up resistor
for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Reaction time comments based on categories
comments = {
    "fast": [
        "Wow, are you lightning in disguise?",
        "Speedy as a cheetah! Impressive!",
        "That was superhuman speed!",
        "You're on fire today!"
    ],
    "moderate": [
        "Not bad, not great, perfectly average.",
        "That's a respectable time, indeed.",
        "Moderately well done, keep trying!",
        "Solid effort, could be quicker though."
    ],
    "slow": [
        "Did you fall asleep?",
        "I've seen glaciers move faster!",
        "Yawn... come on, you can do better!",
        "And here I was, thinking you were quick."
    ]
}

def light_up_led(index):
    GPIO.output(led_pins[index], True)
    return time.time()  # Record the time when the LED was lit

def turn_off_led(index):
    GPIO.output(led_pins[index], False)

def get_comment(reaction_time):
    """ Select an appropriate comment based on the reaction time """
    if reaction_time < 2:
        category = "fast"
    elif reaction_time < 3:
        category = "moderate"
    else:
        category = "slow"
    return random.choice(comments[category])

def reaction_time_game():
    reaction_times = []
    try:
        for _ in range(4):  # Run the game for 4 attempts
            led_index = random.randint(0, len(led_pins) - 1)
            # Random wait before lighting up the LED
            time.sleep(random.uniform(1, 4))

            # Light up a random LED and record the time
            start_time = light_up_led(led_index)
            print("LED lit, waiting for button press...")

            # Wait for the corresponding button press
            while True:
                if GPIO.input(button_pins[led_index]) == GPIO.LOW:
                    reaction_time = time.time() - start_time
                    reaction_times.append(reaction_time)
                    comment = get_comment(reaction_time)
                    print(f"Reaction time: {reaction_time:.3f} seconds - {comment}")
                    turn_off_led(led_index)
                    while GPIO.input(button_pins[led_index]) == GPIO.LOW:
                        pass  # Wait for the button to be released
                    break

    finally:
        GPIO.cleanup()  # Reset GPIO settings on exit

    # Calculate the average reaction time
    if reaction_times:
        average_time = sum(reaction_times) / len(reaction_times)
        print(f"Average reaction time across {len(reaction_times)} attempts: {average_time:.3f} seconds")
    else:
        print("No reaction times recorded.")

if __name__ == "__main__":
    print("Welcome to the Reaction Time Game!")
    input("Press Enter when ready to start...")
    reaction_time_game()
