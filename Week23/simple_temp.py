import time
from ds18b20 import DS18B20

# Function to read temperature from DS18B20 sensor
def read_temp():
    sensor = DS18B20()  # Create an instance of the DS18B20 class
    temperature = sensor.get_temperature()  # Read the temperature
    return temperature

# Main loop to repeatedly read temperature
try:
    while True:
        temp = read_temp()  # Read the current temperature
        print(f"Current temperature: {temp} C")  # Print the temperature
        time.sleep(15)  # Wait for 15 seconds before the next read
except KeyboardInterrupt:
    print("Program exited gracefully")
