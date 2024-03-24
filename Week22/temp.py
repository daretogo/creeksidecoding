import time
import RPi.GPIO as GPIO
from ds18b20 import DS18B20

# Setup for the LEDs. We're using Broadcom pin mode, so these are GPIO numbers, not physical pin numbers.
red_led = 17  # GPIO pin for the red LED
green_led = 27  # GPIO pin for the green LED
blue_led = 22  # GPIO pin for the blue LED

# Initialize GPIO for LED control
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setwarnings(False)  # Disable warnings for GPIO setup
# Setup each LED pin as an output
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)

# Function to read temperature from DS18B20 sensor
def read_temp():
    sensor = DS18B20()  # Create an instance of the DS18B20 class
    temperature = sensor.get_temperature()  # Read the temperature
    return temperature

# Function to control LEDs based on temperature
def control_leds(temp):
    # If temperature is below 65, turn the blue LED on and others off (too cold)
    if temp < 30:
        GPIO.output(blue_led, GPIO.HIGH)
        GPIO.output(red_led, GPIO.LOW)
        GPIO.output(green_led, GPIO.LOW)
    # If temperature is above 80, turn the red LED on and others off (too hot)
    elif temp > 31:
        GPIO.output(red_led, GPIO.HIGH)
        GPIO.output(green_led, GPIO.LOW)
        GPIO.output(blue_led, GPIO.LOW)
    # Otherwise, turn the green LED on and others off (comfortable temperature)
    else:
        GPIO.output(green_led, GPIO.HIGH)
        GPIO.output(red_led, GPIO.LOW)
        GPIO.output(blue_led, GPIO.LOW)

# Main loop to repeatedly read temperature and update LEDs
try:
    while True:
        temp = read_temp()  # Read the current temperature
        print(f"Current temperature: {temp} C")  # Print the temperature
        control_leds(temp)  # Update LEDs based on the temperature
        time.sleep(3)  # Wait for 3 seconds before the next read
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO resources
    print("Program exited gracefully")
