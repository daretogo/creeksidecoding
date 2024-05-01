import RPi.GPIO as GPIO
import sys

# LED pin mapping based on your previous work
led_pins = {
    1: 2,
    2: 3,
    3: 4,
    4: 17,
    5: 27,
    6: 22,
    7: 10,
    8: 9,
    9: 11
}

# Initialize GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up LEDs
for pin in led_pins.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)  # Initialize all LEDs to LOW (off)

def turn_on_led(led_number):
    if 1 <= led_number <= 9:
        pin = led_pins[led_number]
        GPIO.output(pin, GPIO.HIGH)  # Turn on the LED
        print(f"LED {led_number} is on.")
    else:
        print("Invalid LED number. Please choose a number between 1 and 9.")

def cleanup_gpio():
    GPIO.cleanup()

# Check if the script is being run with an argument
if len(sys.argv) != 2:
    print("Usage: python script.py <led_number>")
    sys.exit(1)

try:
    led_number = int(sys.argv[1])
    turn_on_led(led_number)
    input("Press Enter to turn off the LED and exit...")
finally:
    # Clean up GPIO on exit
    cleanup_gpio()
