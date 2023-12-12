"""
Title:MERGED_CODE.py 
Configuration item identifer: 
Purpose: 
The following code is a merged code from previous NEWread_environ_mux_data.py / NEWread_spec_mux_data.py / newLEDs.py 
codes , thepurpose of this code is for LEDs,environmental sensors and spectrometers to work in a simultaneous way. 


CHANGES:

Date: 7th july 2023
Modifier name:Andrea Mireles Tavarez 
Description:
"""
#import camera code 
#for standby mode  only environmental data, temperature , pressure and humidity given.

import os
import time 
import threading 
import board 
import busio
import adafruit_tca9548a
import adafruit_bme680
from bme680 import BME680
from adafruit_as7341 import AS7341
import adafruit_tca9548a
#import raspistill 


#def task1():
   # while True:
       # os.system("sh pi_cam_uc444.sh")
       # time.sleep(5) #must be 43200

#imports for environmental sensors 


#import time
#import board
#import busio
#import adafruit_tca9548a
#import adafruit_bme680
#from bme680 import BME680

#imports for spectrometers

#from adafruit_as7341 import AS7341
#import adafruit_tca9548a


#imports for LEDs

import RPi.GPIO as GPIO
from time import sleep

#send results to outside folder 





def save_to_results_file(data):
    with open("standby.csv",  "a") as f: # Opening the file the data will be stored in
        f.write(data) # Writing data to the above file
        f.write("\n") # Makes a new line
        print (data) 


def sensor_results_file(envsensdata):
    with open("standbyenvsens.csv", "a") as f: 
        f.write(envsensdata)
        f.write("\n")
        print (envsensdata) 

# HOUSE KEEPING DATA 

def housekeeping_data_to_csv():
    while True:
    housekeeping_data = "Timestamp,Temp,Humidity,Pressure,Light"    
    save_to_results_file(housekeeping_data, "housekeepingscience.csv")  
    time.sleep(60) # house keeping data every minute





        ### housekeepingdata 


def task1():
#        raspistill -o image.jpg
    os.system("sh pi_cam_uc444.sh") # Executes commands directly from script
    time.sleep(5) 

 
def task2():
    GPIO.setmode(GPIO.BCM) # Setting numbering scheme
    GPIO.setwarnings(False) # Ignores warnings from compiler, though God knows why you've done that


#set up all 4 GPIOs 
#instead of using 24 GPIOS ,4 GPIOS are used to power all 24 LEDs

    GPIO.setup(14,GPIO.OUT)
    GPIO.setup(15,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(23,GPIO.OUT)


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
def task3():
    
    i2c = board.I2C()
# Create a TCA9548A multiplexer instance
    mux = adafruit_tca9548a.TCA9548A(i2c)



# Set up the BME688 sensors connected to channels 4 and 5 of the multiplexer
    sensor1 = adafruit_bme680.Adafruit_BME680_I2C(mux[7])
    sensor2 = adafruit_bme680.Adafruit_BME680_I2C(mux[6])
    time.sleep(1)
# Read and print the data from both sensors
    
    data_sensor1 = ( "Sensor 1:\n"+
    "Temperature: %.2f C\n" % sensor1.temperature +
    "Pressure: %.2f hPa\n" % sensor1.pressure +
    "Humidity: %.2f %%\n" % sensor1.humidity +
    "Gas resistance: %d ohm\n" % sensor1.gas)

    save_to_results_file(data_sensor1)
    sensor_results_file(envsensdata_sensor1)

    time.sleep(1) #must be 60
  
 
    # Read data from sensor 1
   # temperature2, pressure2, humidity2, gas2 = sensor2.data
    data_sensor2 = ( "Sensor 2:\n"+
    "Temperature: %.2f C\n" % sensor2.temperature +
    "Pressure: %.2f hPa\n" % sensor2.pressure +
    "Humidity: %.2f %%\n" % sensor2.humidity +
    "Gas resistance: %d ohm\n" % sensor2.gas)

    save_to_results_file(data_sensor2)
    sensor_results_file(envsensdata_sensor2)

    time.sleep(1)





#set the adress of TCA9548 I2C multiplexer 
#MUX adress =0x70
#i2c = board.I2C()
#mux = adafruit_tca9548a.TCA9548A (i2c)

#Initialize the TCA4598A spectro on channel 0
#spectro 1 =AS7341 (i2c_addr=spec_1_address, i2c_device=bus)
#while True:
#spectro1 =AS7341(mux[0])
#data_spectro1 = ("SPECTRO 1 CHANNEL 415 nm/VIOLET DATA: %d\n" % spectro1.channel_415nm +
# "SPECTRO 1 CHANNEL 480 nm/BLUE DATA: %d\n" % spectro1.channel_480nm +
# "SPECTRO 1 CHANNEL 555 nm/GREEN DATA: %d\n" % spectro1.channel_555nm)

#save_to_results_file(data_spectro1)


#Read sensor data from channel 2
#Set the channel of the multiplexer to read data from spectro 2
 
#SPECTRO 2 
#Initialize the BME688 sensor on channel 1 
#spectro2= AS7341(mux[1])
#data_spectro2 =("SPECTRO 2 CHANNEL 415 nm/VIOLET DATA: %d\n" % spectro2.channel_415nm +
# "SPECTRO 2 CHANNEL 480 nm/BLUE DATA: %d\n" % spectro2.channel_480nm +
# "SPECTRO 2 CHANNEL 555 nm/GREEN DATA: %d\n" %  spectro2.channel_555nm)

#save_to_results_file(data_spectro2)

#SPECTRO3
#Initialize the BME688 sensor on channel 2 
#spectro3= AS7341(mux[2])
#data_spectro3 =("SPECTRO 3 CHANNEL 415 nm/VIOLET DATA: %d\n" % spectro3.channel_415nm +
# "SPECTRO 3 CHANNEL 480 nm/BLUE DATA: %d\n" % spectro3.channel_480nm +
# "SPECTRO 3 CHANNEL 555 nm/GREEN DATA: %d\n" % spectro3.channel_555nm)
 
#save_to_results_file(data_spectro3)

#SPECTRO4
#CHANNEL 3 
#spectro4= AS7341(mux[3])
#data_spectro4 =("SPECTRO 4 CHANNEL 415 nm/VIOLET DATA: %d\n" % spectro4.channel_415nm +
# "SPECTRO 4 CHANNEL 480 nm/BLUE DATA: %d\n" % spectro4.channel_480nm +
# "SPECTRO 4 CHANNEL 555 nm/GREEN DATA: %d\n" % spectro4.channel_555nm)

#save_to_results_file(data_spectro4)


#time.sleep(1)





# threading 

thread1 = threading.Thread(target = task1)
thread2 = threading.Thread(target = task2)
thread3 = threading.Thread(target = task3)



thread1.start()
thread1.join()
thread2.start()
thread2.join()
thread3.start()
thread3.join()


print("ALL TASKS IN STANDBY MODE HAVE BEEN COMPLETED")












