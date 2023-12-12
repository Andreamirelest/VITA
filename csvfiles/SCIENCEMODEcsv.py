"""
Title:SCIENCEMODE.py 
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
import time
import threading 

#while True:
#    os.system("sh pi_cam_uc444.sh")
 #   time.sleep(5) #MUST BE 300  
  #  break
#imports for environmental sensors 


import time
import board
import busio
import adafruit_tca9548a
import adafruit_bme680
from bme680 import BME680

import V2FINALPLAY.py 



#imports for spectrometers

from adafruit_as7341 import AS7341
import adafruit_tca9548a


#improts for LEDs

import RPi.GPIO as GPIO
from time import sleep

def save_to_results_file(data):
    with open("SPECTROMETER.csv",  "a") as f:
        f.write(data)
        f.write("\n")
    print (data)


#Set up the I2C bus and the multiplexer
#i2c = busio.I2C(board.SCL, board.SDA)
def task1():
 
#set the adress of TCA9548 I2C multiplexer 
#MUX adress =0x70
    i2c = board.I2C()
    mux = adafruit_tca9548a.TCA9548A(i2c)

#Initialize the TCA4598A spectro on channel 0
#spectro 1 =AS7341 (i2c_addr=spec_1_address, i2c_device=bus)
#while True:
    spectro1 = AS7341(mux[0])
    data_spectro1 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f}".format(time.time(),1,spectro1.channel_415nm,spectro1.channel_480nm,spectro1.channel_555nm)

    save_to_results_file(data_spectro1)


#Read sensor data from channel 2
#Set the channel of the multiplexer to read data from spectro 2

 
#SPECTRO 2 
#Initialize the BME688 sensor on channel 1 
    spectro2 = AS7341(mux[1])
    
    data_spectro2 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f}".format(time.time(),2,spectro2.channel_415nm,spectro2.channel_480nm,spectro2.channel_555nm)

    save_to_results_file(data_spectro2)

#SPECTRO3
#Initialize the BME688 sensor on channel 2 
    spectro3 = AS7341(mux[2])
                  
    data_spectro3 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f}".format(time.time(),3,spectro3.channel_415nm,spectro3.channel_480nm,spectro3.channel_555nm)
 
    save_to_results_file(data_spectro3)

#SPECTRO4
#CHANNEL 3 
    spectro4 = AS7341(mux[3])
    data_spectro4 ="{:.2f},{:d},{:.2f}.{:.2f},{:.2f}".format(time.time(),4,spectro4.channel_415nm,spectro4.channel_480nm,spectro4.channel_555nm)

    save_to_results_file(data_spectro4)

 
    time.sleep(1) #must be 60

    print ("THE CURRENT MODE IS SCIENCE MODE ")



#thread  to be continued tomorrow 

thread1 = threading.Thread(target=task1)



#start threads in order

thread1.start()
thread1.join()   #waits for task1 to be done before task 2



print("ALL TASKS HAVE BEEN COMPLETED IN SCIENCE MODE")


 
