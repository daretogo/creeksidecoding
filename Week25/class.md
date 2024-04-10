# Week 25 
## Due to me not having 6 of every type of sensor, we're gonna have to do 2 things today so everyone has something to work with. 

## Using the ultra-sonic distance sensor HC-SR04
### The physical setup: 


    VCC Connects to 5V
    Trig Connects to GPIO 4
    Echo Connects to Resistor#1  (1k Ω value)
    Resistor#2 (2k Ω) Connects from Resistor#1 to Ground
    Wire from Resistor#1 and Resistor#2 connects to GPIO 17
    GND connects to Pin 6 (Ground)


The reason for the resistors is that this device outputs a 5v signal, but the raspberry pi only accepts 3v input signals. 
The resistors act as a voltage divider reducing the signal voltage from 5v to 3v3. 

### Software: 
See the "distance.py" script.   Run it with "python ./distance.py" 

### During the sensor setup, I referneced: 
https://pimylifeup.com/raspberry-pi-distance-sensor/ 


## Using the Sainsmart 2 relay module 

### The physical setup: 

    GND to GND
    IN1 to GPIO 16
    IN2 to GPIO 20
    VCC to 5v

Once it's wired in, you'll likely see a faint glow of the two LEDs on either side of the board. 


## Software: 

See "relay.py".  Run it with commands like: 

python ./relay.py 1 on
python ./relay.py 1 off
python ./relay.py 2 off
python ./relay.py 2 on
python ./relay.py 1 on
python ./relay.py 1 off
python ./relay.py 2 off

See how you must pass 2 arguments to the script.  The first argument is the relay number, the second sets the state to be HIGH or LOW based on your desire to be on or off. 

