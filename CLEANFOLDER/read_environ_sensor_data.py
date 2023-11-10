"""
Title: read_environ_sensor_data.py
Configuration item identifier: OBDH_environmental_sensor-v1.0

Purpose: to read data from environmental sensor
Original author: Rocio Valera Falla - eayrv@nottingham.ac.uk
Creation date: 23/02/2023

This program access data from the Pimoroni BME688 sensor
1. Import the necessary libraries, time, board and bme680
sudo pip install bme680
2. Create an I2C object
I2C will have to be enabled on the Raspberry Pi
3. Create a BME680 object using the I2C object we just created
4. Set up the oversampling and filter configuration for temperature,
pressure and humidity. Also set up the gas sensor and heater
configuration
5. Start an infinite loop that prints out the current temperature,
pressure, humidity and gas resistance with 1-second delay between readings

CHANGES:

Date:
Modifier name:
Description:
"""

import bme680
import time
import smbus

# Create the smbus object
bus = smbus.SMBus(1) #Use bus 1 on RPi

# Create the BME680 sensor object
environ_sensor = bme680.BME680(i2c_addr=bme680.I2C_ADDR_PRIMARY, i2c_device=bus)

# Set up oversampling and filter configuration
environ_sensor.oversample_temperature = 2
environ_sensor.oversample_pressure = 2
environ_sensor.oversample_humidity = 2
environ_sensor.filter_size = 2

# Set up gas sensor configuration
environ_sensor.gas_stored_ohms = 100000

# Set up the heater configuration
environ_sensor.heater_temp = 320
environ_sensor.heater_time = 150

# Loop forever reading data
while True:
    print("Temperature: %0.1f C" % environ_sensor.data.temperature)
    print("Pressure: %0.1f hPa" % environ_sensor.data.pressure)
    print("Humidity: %0.1f %%" % environ_sensor.data.humidity)
    print("Gas: %d ohm" % environ_sensor.data.gas_resistance)
    time.sleep(5)
