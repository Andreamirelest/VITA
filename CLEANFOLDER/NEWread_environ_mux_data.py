"""
Title: environ_data.py
Configuration item identifier: OBDH_environ_data-v1.0

Purpose: to read data from environmental sensor during science mode
Original author: Rocio Valera Falla - eayrv@nottingham.ac.uk
Creation date: 23/02/2023

This program access data from the Pimoroni BME688 sensor via the
Adafruit TCA9548A multiplexer
1. Import the necessary libraries, board, busio, adafruit_tca9548a
adafruit_bme688
Run the following line in the rpi command to install the libraries
before importing them:
sudo pip install bme680
sudo pip install adafruit-circuitpython-tca9548a
2. Create an I2C object using the board pins for SCL and SDA
3. Create a TCA9548A object using the I2C object we just created
4. Create two instances of the BME688 sensor, one for each channel of the
multiplexer.
5. Read and print the data from both sensors

CHANGES:

Date:
Modifier name:
Description:
"""

import time
import board
import busio
import adafruit_tca9548a
import adafruit_bme680
from bme680 import BME680

# Set up the I2C bus and the multiplexer
#i2c = busio.I2C(board.SCL, board.SDA)
i2c = board.I2C()
# Create a TCA9548A multiplexer instance
mux = adafruit_tca9548a.TCA9548A(i2c)

# Set up the BME688 sensors connected to channels 4 and 5 of the multiplexer
sensor1 = adafruit_bme680.Adafruit_BME680_I2C(mux[7])
#sensor2 = adafruit_bme680.Adafruit_BME680_I2C(mux[6])
#channel_number1  = int(mux[4].value)
#sensor1 = bme680.BME680(mux[4])
#sensor2 = bme680.BME680(mux[5])

# Read and print the data from both sensors
while True:
    # Read data from sensor 
    #temperature1, pressure1, humidity1, gas1 = sensor1.data
    print("Sensor 1:")
    print("Temperature: %.2f C" % sensor1.temperature)
    print("Pressure: %.2f hPa" % sensor1.pressure)
    print("Humidity: %.2f %%" % sensor1.humidity)
    print("Gas resistance: %d ohm" % sensor1.gas)
    print()
    time.sleep(5)
 
    # Read data from sensor 1
   # temperature2, pressure2, humidity2, gas2 = sensor2.data
   # print("Sensor 2:")
   # print("Temperature: %.2f C" % sensor2.temperature)
   # print("Pressure: %.2f hPa" % sensor2.pressure)
   # print("Humidity: %.2f %%" % sensor2.humidity)
   # print("Gas resistance: %d ohm" % sensor2.gas)
   # print()
   # time.sleep(5)
