import RPi.GPIO as GPIO
import time

# Button pin mapping based on your previous work
button_pins = {
    1: 14,
    2: 15,
    3: 18,
    4: 23,
    5: 24,
    6: 25,
    7: 8,
    8: 7,
    9: 1
}

# Initialize GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up buttons
for pin in button_pins.values():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Function to handle button presses
def button_callback(channel):
    button_number = next((k for k, v in button_pins.items() if v == channel), None)
    if button_number:
        print(f"Button {button_number} was pressed.")

# Add event detection for each button
for pin in button_pins.values():
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=button_callback, bouncetime=200)

# Main loop
try:
    print("Listening for button presses. Press CTRL+C to exit.")
    while True:
        time.sleep(0.1)  # Sleep to reduce CPU usage

except KeyboardInterrupt:
    # Clean up GPIO on exit
    GPIO.cleanup()
