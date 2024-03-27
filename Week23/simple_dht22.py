import time
import Adafruit_DHT
#python -m pip install Adafruit_DHT


DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 26  # Assuming the DHT22 is connected to GPIO pin 26

def read_temp_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return temperature, humidity

try:
    while True:
        temperature, humidity = read_temp_humidity()
        if temperature is not None and humidity is not None:
            print(f"Current temperature: {temperature:.2f} C, Humidity: {humidity:.2f}%")
        else:
            print("Failed to retrieve data from the sensor")
        time.sleep(15)
except KeyboardInterrupt:
    print("Program exited gracefully")