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


#the following code is for 
#import camera code 

import os
import time
import threading 


#for cyclic data storage
from cyclicDataTest import cyclicCheck
#print(cyclicCheck())

#import for steppermotor
#steppermnotor clockwise in rehydration mode
#while True:
 #   os.system("python STEPPERMOTOR_CLOCKWISE.py")
  #  time.sleep(5)
   # break

#while True:
 #   os.system("sh pi_cam_uc444.sh")
  #  time.sleep(300)




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
#import V2FINALPLAY.py 

#improts for LEDs

import RPi.GPIO as GPIO
from time import sleep

#IMPORT STEPPERMOTOR CLOCKWISE FOR REHYDRATION MODE

#def task1():
 #   while True:
  #      os.system("python STEPPERMOTOR_CLOCKWISE.py")
   #     time.sleep(5)
        

#IMPORT FOR CAMERA

#def task2():
#    os.system("sh pi_cam_uc444.sh")
 #   time.sleep(5)



def save_to_results_file(data):
    print ("Testing saving stuff")
    with open("rehydrate.txt",  "a") as f:
        if cyclicCheck():
            try:
                f.write(data)
                f.write("\n")
                print (data)
            except:
                print("write failed")

        else:
            print("SD Card Full!!")
            data = f.readlines()
            noLines = len(data)
            if lineCounter < noLines:
                try:
                    data[lineCounter] = data
                    print (data)
                except:
                    print("write failed")
            else:
                lineCounter = 0
                try:
                    data[lineCounter] = data
                    print (data)
                except:
                    print( "Write Failed")
    print ("End of saving stuff")


#Import steppermotor clockwise in rehydration mode

def task1():

        #importing external codes (steppermotor &  TCS)	
        
        os.system("python V2FINALPLAY.py")
        time.sleep(1)


#camera

def task2():
    while True:
	
        os.system("sh pi_cam_uc444.sh")
        time.sleep(1)
        break


    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)


#set up all 4 GPIOs 
#instead of using 24 GPIOS ,4 GPIOS are used to power all 24 LEDs

    GPIO.setup(14,GPIO.OUT)
    GPIO.setup(15,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(23,GPIO.OUT)


#While Loop
#while True:
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
#channel_number1  = int(mux[4].value)
#sensor1 = bme680.BME680(mux[4])
#sensor2 = bme680.BME680(mux[5])
    sleep(1)
# Read and print the data from both sensors
#while True:
    # Read data from sensor 
    #temperature1, pressure1, humidity1, gas1 = sensor1.data
    data_sensor1 =( "Sensor 1:\n"+
    "Temperature: %.2f C\n" % sensor1.temperature +
    "Pressure: %.2f hPa\n" % sensor1.pressure +
    "Humidity: %.2f %%\n" % sensor1.humidity +
    "Gas resistance: %d ohm\n" % sensor1.gas)

    save_to_results_file(data_sensor1)

    time.sleep(1)  #must be 60
 
 
    # Read data from sensor 1
   # temperature2, pressure2, humidity2, gas2 = sensor2.data
    data_sensor2 =( "Sensor 2:\n"+
   "Temperature: %.2f C\n" % sensor2.temperature +
   "Pressure: %.2f hPa\n" % sensor2.pressure +
   "Humidity: %.2f %%\n" % sensor2.humidity +
   "Gas resistance: %d ohm\n" % sensor2.gas)

    save_to_results_file(data_sensor2)
    time.sleep(1)   #must be 60

#set the adress of TCA9548 I2C multiplexer 
#MUX adress =0x70
    i2c = board.I2C()
    mux = adafruit_tca9548a.TCA9548A(i2c)

#Initialize the TCA4598A spectro on channel 0
#spectro 1 =AS7341 (i2c_addr=spec_1_address, i2c_device=bus)
#while True:
    spectro1 =AS7341(mux[0])
    data_spectro1 = ("SPECTRO 1 CHANNEL 415 nm/VIOLET DATA: %d\n" % spectro1.channel_415nm +
    "SPECTRO 1 CHANNEL 480 nm/BLUE DATA: %d\n" % spectro1.channel_480nm +
    "SPECTRO 1 CHANNEL 555 nm/GREEN DATA: %d\n" % spectro1.channel_555nm)

    save_to_results_file(data_spectro1)


#Read sensor data from channel 2
#Set the channel of the multiplexer to read data from spectro 2

 
#SPECTRO 2 
#Initialize the BME688 sensor on channel 1 
    spectro2= AS7341(mux[1])
    data_spectro2 =("SPECTRO 2 CHANNEL 415 nm/VIOLET DATA: %d\n" % spectro2.channel_415nm +
    "SPECTRO 2 CHANNEL 480 nm/BLUE DATA: %d\n" % spectro2.channel_480nm +
    "SPECTRO 2 CHANNEL 555 nm/GREEN DATA: %d\n" %  spectro2.channel_555nm)

    save_to_results_file(data_spectro2)

#SPECTRO3
#Initialize the BME688 sensor on channel 2 
    spectro3= AS7341(mux[2])
    data_spectro3 =("SPECTRO 3 CHANNEL 415 nm/VIOLET DATA: %d\n" % spectro3.channel_415nm +
    "SPECTRO 3 CHANNEL 480 nm/BLUE DATA: %d\n" % spectro3.channel_480nm +
    "SPECTRO 3 CHANNEL 555 nm/GREEN DATA: %d\n" % spectro3.channel_555nm)
 
    save_to_results_file(data_spectro3)

#SPECTRO4
#CHANNEL 3 
    spectro4= AS7341(mux[3])
    data_spectro4 =("SPECTRO 4 CHANNEL 415 nm/VIOLET DATA: %d\n" % spectro4.channel_415nm +
    "SPECTRO 4 CHANNEL 480 nm/BLUE DATA: %d\n" % spectro4.channel_480nm +
    "SPECTRO 4 CHANNEL 555 nm/GREEN DATA: %d\n" % spectro4.channel_555nm)

    save_to_results_file(data_spectro4)


    time.sleep(1)  #must be 60

    print ("THE CURRENT MODE IS SCIENCE MODE ")


#thread 

thread1 = threading.Thread(target = task1)
thread2 = threading.Thread(target = task2)
thread3 = threading.Thread(target = task3)


#start the threads in order

thread1.start()
thread1.join() #wait for task 1 to complete before starting task 2 
thread2.start()
thread2.join()
thread3.start()
thread3.join()

print ("ALL TASKS HAVE BEEN COMPLETED FOR SCIENCE MODE")
