## All I've done here is collect the "import" statements from all the scripts that I am borrowing / using code form.  so in this case I'm using all the import statements from the Week22/temp.py and the Week24/simple_display.py
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import RPi.GPIO as GPIO
from ds18b20 import DS18B20

#This is the minimum setup to get the display working - if you copied a BIG section of simple_display.py here that is fine - that's where this config comes from - this is just condensed
# OLED Display Setup
RST = None
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

# LED Setup - taken directly from the existing examples we've worked with: 
red_led = 17
green_led = 27
blue_led = 22
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)

# Function to read temperature
def read_temp():
    sensor = DS18B20()
    temperature = sensor.get_temperature()
    return temperature

# Function to update OLED display
def update_display(temp):
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    temp_str = f"Temp: {temp:.2f} C"
    draw.text((0, 0), temp_str, font=font, fill=255)
    disp.image(image)
    disp.display()

# Function to control LEDs based on temperature
def control_leds(temp):
    if temp < 30:
        GPIO.output(blue_led, GPIO.HIGH)
        GPIO.output(red_led, GPIO.LOW)
        GPIO.output(green_led, GPIO.LOW)
    elif temp > 31:
        GPIO.output(red_led, GPIO.HIGH)
        GPIO.output(green_led, GPIO.LOW)
        GPIO.output(blue_led, GPIO.LOW)
    else:
        GPIO.output(green_led, GPIO.HIGH)
        GPIO.output(red_led, GPIO.LOW)
        GPIO.output(blue_led, GPIO.LOW)

try:

    #Here's the main loop. Remember, while loops run until they are FALSE or encounter a BREAK. This one has neither - just a 3 second sleep.   So it's meant to happen forever, in a loop, ever 3 seconds. 
    #you can walk through what it does with me in the comments: 
    while True:
        temp = read_temp()   # first - we're creating a varaible named "temp" and setting it equal to the output of the "read_temp()" function.   See the above "read_temp()" function on line 35 for info on how that's just taking a reading off the sensor. 
        print(f"Current temperature: {temp} C")  # now it's just printing the temp, so we get the message in our  terminal. 
        update_display(temp) # here we call the update_display function, and pass it the current temperature via that temp variable.  See line 41 for that function which just writes "Temp: " Then then temp## to the screen. 
        control_leds(temp)  #this is maintaining the existing functionality where we turn the leds on and off based on the temperature reading.  Lines 49-61
        time.sleep(3)  #sleep means it  waits for 3 seconds, before starting over at the top of the loop to do it all again. 
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program exited gracefully")
