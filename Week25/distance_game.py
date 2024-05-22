import RPi.GPIO as GPIO
import time
import random

# Function to measure the distance using the ultrasonic sensor
def measure_distance():
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    while GPIO.input(PIN_ECHO) == 0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO) == 1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance_cm = round(pulse_duration * 17150, 2)
    return distance_cm

try:
    GPIO.setmode(GPIO.BOARD)

    PIN_TRIGGER = 7
    PIN_ECHO = 11

    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    print("Waiting for sensor to settle")
    time.sleep(2)

    while True:
        target_cm = random.uniform(0, 30)  # Generate a random value up to 30 cm
        target_inches = target_cm / 2.54  # Convert cm to inches
        target_inches = round(target_inches, 2)

        print(f"Pull out the slider to {target_inches} inches.")

        for i in range(5, 0, -1):
            print(f"{i} seconds remaining...")
            time.sleep(1)

        print("Measuring...")
        distance_cm = measure_distance()
        distance_inches = distance_cm / 2.54
        distance_inches = round(distance_inches, 2)

        difference = abs(target_inches - distance_inches)
        print(f"You pulled out {distance_inches} inches. You were off by {difference} inches.")

        print("\nLet's try again!\n")
        time.sleep(2)  # Wait a bit before the next round

finally:
    GPIO.cleanup()
