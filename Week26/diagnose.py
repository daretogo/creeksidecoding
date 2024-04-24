import RPi.GPIO as GPIO
import time

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

def identify_button_led_mapping():
    mapping = {}
    
    try:
        for i, led_pin in enumerate(led_pins):
            print(f"Press the button corresponding to LED {i+1} (connected to pin {led_pin}).")
            GPIO.output(led_pin, True)  # Turn on the LED
            time.sleep(0.1)  # Debounce delay

            # Wait for any button to be pressed
            while True:
                for j, button_pin in enumerate(button_pins):
                    if GPIO.input(button_pin) == GPIO.LOW:  # Assuming a LOW signal means pressed
                        mapping[button_pin] = led_pin
                        print(f"Button {j+1} (connected to pin {button_pin}) is mapped to LED {i+1}.")
                        time.sleep(0.5)  # Debounce delay
                        GPIO.output(led_pin, False)  # Turn off the LED
                        while GPIO.input(button_pin) == GPIO.LOW:
                            pass  # Wait for the button to be released
                        break
                if button_pin in mapping:
                    break

            time.sleep(1)  # Delay between tests for clarity

    finally:
        GPIO.cleanup()  # Reset GPIO settings on exit

    return mapping

if __name__ == "__main__":
    button_to_led_mapping = identify_button_led_mapping()
    print("Button to LED mapping completed.")
    print("Mapping:", button_to_led_mapping)
