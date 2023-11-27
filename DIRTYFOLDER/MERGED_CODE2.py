"""
Title:MERGED_CODE.py 
Configuration item identifier: 
Purpose: 
The following code is a merged code from previous NEWread_environ_mux_data.py / NEWread_spec_mux_data.py / newLEDs.py 
codes , thepurpose of this code is for LEDs,environmental sensors and spectrometers to work in a simultaneous way. 


CHANGES:

Date: 7th july 2023
Modifier name:Andrea Mireles Tavarez 
Description:

"""
#import camera code 

import os
os.system("sh pi_cam_uc444.sh")


#imports for environmental sensors 


import time
import board
import busio
import adafruit_tca9548a
import adafruit_bme680
from bme680 import BME680

#imports for spectrometers

from adafruit_as7341 import AS7341
import adafruit_tca9548a


#improts for LEDs

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#set up all 4 GPIOs 
#instead of using 24 GPIOS ,4 GPIOS are used to power all 24 LEDs

GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)


#While Loop
while True:
 GPIO.output(14,GPIO.HIGH)
 sleep(2)
 GPIO.output(14,GPIO.LOW)
 sleep(1)
 GPIO.output(15,GPIO.HIGH)
 sleep(2)
 GPIO.output(15,GPIO.LOW)
 sleep(1)
 GPIO.output(18,GPIO.HIGH)
 sleep(2)
 GPIO.output(18,GPIO.LOW)
 sleep(1)
 GPIO.output(23,GPIO.HIGH)
 sleep(2)
 GPIO.output(23,GPIO.LOW)
 sleep(1) 


# Set up the I2C bus and the multiplexer
#i2c = busio.I2C(board.SCL, board.SDA)
 i2c = board.I2C()
# Create a TCA9548A multiplexer instance
 mux = adafruit_tca9548a.TCA9548A(i2c)

# Set up the BME688 sensors connected to channels 4 and 5 of the multiplexer
 sensor1 = adafruit_bme680.Adafruit_BME680_I2C(mux[7])
 sensor2 = adafruit_bme680.Adafruit_BME680_I2C(mux[6])
#channel_number1  = int(mux[4].value)
#sensor1 = bme680.BME680(mux[4])
#sensor2 = bme680.BME680(mux[5])
 sleep(1)
# Read and print the data from both sensors
#while True:
    # Read data from sensor 
    #temperature1, pressure1, humidity1, gas1 = sensor1.data
 print("Sensor 1:")
 print("Temperature: %.2f C" % sensor1.temperature)
 print("Pressure: %.2f hPa" % sensor1.pressure)
 print("Humidity: %.2f %%" % sensor1.humidity)
 print("Gas resistance: %d ohm" % sensor1.gas)
 print()
 time.sleep(5)

#send data from sensor 1 to text file 

# def save_to_file(sensor1, DATARESULTS.txt):
# with open(DATARESULTS.txt, 'a') as file:
# file.write(sensor1 = '/n') 

# def obtain_sensor1_data(sensor1):
# data = f"{sensor1}data"
# return data 



 
    # Read data from sensor 1
   # temperature2, pressure2, humidity2, gas2 = sensor2.data
 print("Sensor 2:")
 print("Temperature: %.2f C" % sensor2.temperature)
 print("Pressure: %.2f hPa" % sensor2.pressure)
 print("Humidity: %.2f %%" % sensor2.humidity)
 print("Gas resistance: %d ohm" % sensor2.gas)
 print()
 time.sleep(5)


# def save_to_file(sensor2, DATARESULTS.txt):
# with open(DATARESULTS.txt, 'a') as file:
# file.write(sensor2 = '/n')

# def obtain_sensor2_data(sensor2):
# data= f"{sensor2}data"
# return data 

#set the adress of TCA9548 I2C multiplexer 
#MUX adress =0x70
 i2c = board.I2C()
 mux = adafruit_tca9548a.TCA9548A (i2c)

#Initialize the TCA4598A spectro on channel 0
#spectro 1 =AS7341 (i2c_addr=spec_1_address, i2c_device=bus)
#while True:
 spectro1 =AS7341(mux[0])
 print("SPECTRO 1 CHANNEL 415 nm/VIOLET DATA:", spectro1.channel_415nm) 
 print("SPECTRO 1 CHANNEL 480 nm/BLUE DATA:", spectro1.channel_480nm)
 print("SPECTRO 1 CHANNEL 555 nm/GREEN DATA:", spectro1.channel_555nm)

#send spectrometer data to file SPECTRORESULTS.txt 

while True:
for spectro1_data in ["spectro1"]:
obtain_spectro1_data(spectro1)
save_to_file(spectro1_data, "SPECTRORESULTS.txt")



#Read sensor data from channel 2
#Set the channel of the multiplexer to read data from spectro 2

 
#SPECTRO 2 
#Initialize the BME688 sensor on channel 1 
 spectro2= AS7341(mux[1])
 print("SPECTRO 2 CHANNEL 415 nm/VIOLET DATA:", spectro2.channel_415nm)
 print("SPECTRO 2 CHANNEL 480 nm/BLUE DATA:", spectro2.channel_480nm)
 print("SPECTRO 2 CHANNEL 555 nm/GREEN DATA:", spectro2.channel_555nm)

for spectro2_data in ["spectro2"]:
obatin_spectro2_data(spectro2)
save_to_file(spectro2_data, "SPECTRORESULTS.txt")


#SPECTRO3
#Initialize the BME688 sensor on channel 2 
 spectro3= AS7341(mux[2])
 print("SPECTRO 3 CHANNEL 415 nm/VIOLET DATA:", spectro3.channel_415nm)
 print("SPECTRO 3 CHANNEL 480 nm/BLUE DATA:", spectro3.channel_480nm)
 print("SPECTRO 3 CHANNEL 555 nm/GREEN DATA:", spectro3.channel_555nm)


#SPECTRO4
#CHANNEL 3 
 spectro4= AS7341(mux[3])
 print("SPECTRO 4 CHANNEL 415 nm/VIOLET DATA:", spectro4.channel_415nm)
 print("SPECTRO 4 CHANNEL 480 nm/BLUE DATA:", spectro4.channel_480nm)
 print("SPECTRO 4 CHANNEL 555 nm/GREEN DATA:", spectro4.channel_555nm)
 time.sleep(1)





