
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

# HOUSEKEEPING DATA 



housekeeping_directory = "/path/to/HOUSEKEEPINGFOLDER/"

def save_to_housekeeping_file(data):
    os.makedirs(housekeeping_directory, exist_ok=True)
    file_path = os.path.join(housekeeping_directory, "rehydrationhousekeeping.csv")
    with open(file_path, "a") as f:
        f.write(data)
        f.write("\n")
    print(data)

# Housekeeping data function for each component
def housekeeping_data(data):
    save_to_housekeeping_file(data)




results_directory = “/path/to/RESULTSFOLDER/“

def save_to_results_file(data): #try replacing filename with  Rehydrationmode.csv if it does not work 

#create folder in case it does not exist 

    os.makedirs(results_directory, exist_ok=True)
  
    file_path = os.path.join(results_directory, "rehydration.csv")   # Rehydration results in outside folder 

    with  open (file_path, "a") as f: 
        f.write(data)
        f.write("\n")

        print(data)


def save_to_results_file(data):
    with open("rehydration.csv",  "a") as f:
        f.write(data)
        f.write("\n")
    print (data)
      

# evironmental sensors data to RESULTS FOLDER 

# comment what does not work 

def sensor_results_file(data): 

    os.makedirs(results_directory, exist_ok=True)

    file_path = os.path.join(results_directory, "rehydrationenvsens.csv")

    with  open (file_path, "a") as f: 
        f.write(data)
        f.write("\n")

        print(data)        



def sensor_results(data):
    os.makedirs(resukts_directory, exist_ok=True)

    file_path = os.path.join(results_directory, "rehydrationenvsens.csv")

    with open(file_path, "a") as f:      # comment it if not working 
    with open("rehydrationenvsens.csv", "a") as f:
        f.write(data)
        f.write("\n")
    print (data)



    # spectrometer results to outside folder RESULTSFOLDER 

 def spectro_results_file(data): 
     os.makedirs(results_directory, exist_ok=True)

    
    file_path = os.path.join(results_directory, "rehydrationspectro.csv")

     with  open (file_path, "a") as f: 
        f.write(data)
        f.write("\n")

        print(data)

# spectrometer results 

def spectro_results(data):
    with open("rehydrationspectrodata.csv", "a") as f:
        f.write(data)
        f.write("\n")
    print (data)




#tcs results to outside folder RESULTS FOLDER 


def tcs_results_file(tcsdata): 
     os.makedirs(results_directory, exist_ok=True)    # check if directory exists 

    # spectrometer results to outside folder RESULTSFOLDER 

    file_path = os.path.join(results_directory, "rehydrationtcs.csv")

     with  open (file_path, "a") as f: 
        f.write(tcsdata)
        f.write("\n")

        print(tcsdata)

# tcs results 

def tcs_results(tcsdata):
    with open("rehydrationtcsdata.csv", "a") as f: 
        f.write(tcsdata)
        f.write("\n")
    print (tcsdata)


      

 # camera picture files  to outside folder HERE (to be completed )






#Import steppermotor clockwise in rehydration mode

def task1():

        #importing external codes (steppermotor &  TCS)	
        os.system("python STEPPERMOTOR_CLOCKWISE.py")
        time.sleep(1)
        os.system("python V2FINALcsv.py") 
 

        os.system("python V2FINALcsv.py") # make sure to have V2 CODE IN csv format here 
        data_tcs = os.system("python V2FINALcsv.py") # make sure to have V2 CODE IN csv format here # comment if code not working 

        tcs_results_file(data_tcs)

        tcs_results(data_tcs)

        save_to_results_file(data_tcs)

        housekeeping_data("TCS REHYDRATION MODE ", data_tcsrehydration)





        tcs_results_file(tcsdata_tcs)

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
    
    data_sensor1 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f},{:.2f}".format(time.time(), 1, sensor1.temperature, sensor1.pressure, sensor1.humidity, sensor1.gas)

    save_to_results_file(data_sensor1)
    sensor_results_file(data_sensor1)
    sensor_results(data_sensor1)

    housekeeping_data("Sensor1", data_sensor1)


    save_to_housekeeping_file(data_sensor1)


    time.sleep(1)  #must be 60
 
 
    # Read data from sensor 1
   # temperature2, pressure2, humidity2, gas2 = sensor2.data
    
    data_sensor2 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f},{:.2f}".format(time.time(), 2, sensor2.temperature, sensor2.pressure, sensor2.humidity, sensor2.gas)



    save_to_results_file(data_sensor2)
    sensor_results_file(data_sensor2)
    sensor_results(data_sensor2)
    save_to_housekeeping_file(data_sensor2)
    housekeeping_data("Sensor2", data_sensor2)


    time.sleep(1)   #must be 60

#set the adress of TCA9548 I2C multiplexer 
#MUX adress =0x70
    i2c = board.I2C()
    mux = adafruit_tca9548a.TCA9548A(i2c)

#Initialize the TCA4598A spectro on channel 0
#spectro 1 =AS7341 (i2c_addr=spec_1_address, i2c_device=bus)
#while True:
    spectro1 =AS7341(mux[0])
    
    data_spectro1 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f}".format(time.time(),1,spectro1.channel_415nm,spectro1.channel_480nm,spectro1.channel_555nm)

    save_to_results_file(data_spectro1)
    spectro_results_file(data_spectro1)
    spectro_results(data_spectro1)

    housekeeping_data("Spectro1", data_spectro1)



    save_to_housekeeping_file(data_spectro1)

#Read sensor data from channel 2
#Set the channel of the multiplexer to read data from spectro 2

 
#SPECTRO 2 
#Initialize the BME688 sensor on channel 1 
    
    data_spectro2 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f}".format(time.time(),2,spectro2.channel_415nm,spectro2.channel_480nm,spectro2.channel_555nm)


    save_to_results_file(data_spectro2)
    spectro_results_file(data_spectro2)
    spectro_results(data_spectro2)


    housekeeping_data("Spectro2", data_spectro2)

    save_to_housekeeping_file(data_spectro1)

#SPECTRO3
#Initialize the BME688 sensor on channel 2 
    spectro3= AS7341(mux[2])
    
    data_spectro3 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f}".format(time.time(),3,spectro3.channel_415nm,spectro3.channel_480nm,spectro3.channel_555nm)
 
    save_to_results_file(data_spectro3)
    spectro_results_file(data_spectro3)
    spectro_results(data_spectro3)

    housekeeping_data("Spectro3", data_spectro3)




    save_to_housekeeping_file(data_spectro3)


#SPECTRO4
#CHANNEL 3 
    spectro4= AS7341(mux[3])
    
    data_spectro4 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f}".format(time.time(),4,spectro4.channel_415nm,spectro4.channel_480nm,spectro4.channel_555nm)





    save_to_results_file(data_spectro4)
    spectro_results_file(data_spectro4)
    spectro_results(data_spectro4)

    housekeeping_data("Spectro4", data_spectro4)




    save_to_housekeeping_file(data_spectro4)


    time.sleep(1)  #must be 60

    print ("THE CURRENT MODE IS REHYDRATE MODE ")


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

print ("ALL TASKS HAVE BEEN COMPLETED FOR REHYDRATE MODE")
