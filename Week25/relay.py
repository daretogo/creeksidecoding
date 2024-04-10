import RPi.GPIO as GPIO
import sys

# Setup
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin-numbering scheme
GPIO.setwarnings(False)

# GPIO pins to control the relays
relay_pins = {1: 16, 2: 20}

# Set up GPIO pins as output
for pin in relay_pins.values():
    GPIO.setup(pin, GPIO.OUT)

def control_relay(relay_number, state):
    """
    Controls a relay by setting it on or off.

    :param relay_number: The relay number (1 or 2)
    :param state: The state to set the relay ('on' or 'off')
    """
    # Determine the GPIO pin
    pin = relay_pins[relay_number]
    
    # Set the relay state
    if state == 'on':
        GPIO.output(pin, GPIO.LOW)  # Assuming the relay is activated by LOW signal
    elif state == 'off':
        GPIO.output(pin, GPIO.HIGH)  # Assuming the relay is deactivated by HIGH signal
    else:
        print(f"Invalid state '{state}'. Please use 'on' or 'off'.")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <relay_number> <state>")
        print("relay_number: 1 or 2")
        print("state: 'on' or 'off'")
        sys.exit(1)
    
    relay_number = int(sys.argv[1])
    state = sys.argv[2].lower()
    
    if relay_number not in relay_pins:
        print(f"Invalid relay number '{relay_number}'. Please use 1 or 2.")
        sys.exit(1)
    
    control_relay(relay_number, state)
