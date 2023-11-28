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
import time
import threading 
import time 
import board
import adafruit_tca9548a
import adafruit_bme680
from bme680 import BME680


#while True:
#    os.system("sh pi_cam_uc444.sh")
 #   time.sleep(1200)

#import stepper motor 
#DECOMMISION MODE HAS STEPPERMOTORS ACTIVATED IN ANTICLOCKWISE


#task 1 for threads  
#def task1():
 #   while True:
  #      os.system("python STEPPERMOTOR_ANTICLOCK.py")
   ##     time.sleep(5)  #STEPPERMOTOR IS ACTIVATED ON REVERSE WITHIN 5 MINUTES OF STARTING THIS MODE
     #   break  

#imports for environmental sensors 


#import time
#import board
#import busio
#import adafruit_tca9548a
#import adafruit_bme680
#from bme680 import BME680

#imports for spectrometers

from adafruit_as7341 import AS7341
import adafruit_tca9548a


#improts for LEDs

import RPi.GPIO as GPIO
from time import sleep

def save_to_results_file(data):
    with open("decommission.csv",  "a") as f:
        f.write(data)
        f.write("\n")
        print (data)

def sensor_results_file(sensordata):
    with open("decomenvsens.csv", "a") as f:
        f.write(sensordata)
        f.write("\n")
        print (sensordata)


def spectro_results_file(spectrodata):
    with open("decomspectro.csv", "a") as f:
        f.write(spectrodata)
        f.write("\n")
    print (spectrodata)



def task1():
        os.system("python STEPPERMOTOR_ANTICLOCK.py")    #Steppermotor is activated on reverse within 5 minutes of starting this mode
        time.sleep(1)
        


#steppermotor anticlockwise in decommission mode


#while True:
    #os.system("python STEPPERMOTOR_ANTICLOCK.py")
    #time.sleep(300)   #STEPPERMOTOR IS ACTIVATED ON REVERSE WITHIN 5 MINUTES (300seconds)  OF STARTING THIS MODE. (TBC)
    
#camera active every 20 minutes
#task 2 for threads
def task2():
    while True:
        os.system("sh pi_cam_uc444.sh")
        time.sleep(1) #must be 1200
        break

#task 3 thread
def task3():
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

#task 4 for threads 
def task4():
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
    data_sensor1 = ( "Sensor 1:\n"+
    "Temperature: %.2f C\n" % sensor1.temperature +
    "Pressure: %.2f hPa\n" % sensor1.pressure +
    "Humidity: %.2f %%\n" % sensor1.humidity +
    "Gas resistance: %d ohm\n" % sensor1.gas)

    save_to_results_file(data_sensor1)
    sensor_results_file(data_sensor1)

    time.sleep(1)  #must be 60
 
 



    # Read data from sensor 1
   # temperature2, pressure2, humidity2, gas2 = sensor2.data
    data_sensor2 = ( "Sensor 2:\n"+
    "Temperature: %.2f C\n" % sensor2.temperature +
    "Pressure: %.2f hPa\n" % sensor2.pressure +
    "Humidity: %.2f %%\n" % sensor2.humidity +
    "Gas resistance: %d ohm\n" % sensor2.gas)

    save_to_results_file(data_sensor2)
    sensor_results_file(data_sensor2)

    time.sleep(1) #must be 60



#set the adress of TCA9548 I2C multiplexer 
#MUX adress =0x70
#task 5 for thread
def task5():
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
    spectro_results_file(data_spectro1)

#Read sensor data from channel 2
#Set the channel of the multiplexer to read data from spectro 2

 
#SPECTRO 2 
#Initialize the BME688 sensor on channel 1 
    spectro2= AS7341(mux[1])
    data_spectro2 =("SPECTRO 2 CHANNEL 415 nm/VIOLET DATA: %d\n" % spectro2.channel_415nm +
    "SPECTRO 2 CHANNEL 480 nm/BLUE DATA: %d\n" % spectro2.channel_480nm +
    "SPECTRO 2 CHANNEL 555 nm/GREEN DATA: %d\n" %  spectro2.channel_555nm)

    save_to_results_file(data_spectro2)
    spectro_results_file(data_spectro2)
    

#SPECTRO3
#Initialize the BME688 sensor on channel 2 
    spectro3= AS7341(mux[2])
    data_spectro3 =("SPECTRO 3 CHANNEL 415 nm/VIOLET DATA: %d\n" % spectro3.channel_415nm +
    "SPECTRO 3 CHANNEL 480 nm/BLUE DATA: %d\n" % spectro3.channel_480nm +
    "SPECTRO 3 CHANNEL 555 nm/GREEN DATA: %d\n" % spectro3.channel_555nm)
 
    save_to_results_file(data_spectro3)
    spectro_results_file(data_spectro3)

#SPECTRO4
#CHANNEL 3 
    spectro4= AS7341(mux[3])
    data_spectro4 =("SPECTRO 4 CHANNEL 415 nm/VIOLET DATA: %d\n" % spectro4.channel_415nm +
    "SPECTRO 4 CHANNEL 480 nm/BLUE DATA: %d\n" % spectro4.channel_480nm +
    "SPECTRO 4 CHANNEL 555 nm/GREEN DATA: %d\n" % spectro4.channel_555nm)

    save_to_results_file(data_spectro4)
    spectro_results_file(data_spectro4)

     

    time.sleep(1) #must be 300
    
   # print("THE CURRENT MODE IS DECOMMISION")

#threads are created to make each task a separate function
#create and start threads for each task
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)
thread3 = threading.Thread(target=task3)
thread4 = threading.Thread(target=task4)
thread5 = threading.Thread(target=task5)


thread1.start()
thread1.join()
thread2.start()
thread2.join()
thread3.start()
thread3.join()
thread4.start()
thread4.join()
thread5.start()
thread4.join()


#join() is used to wait for each thread to finish for main thread to continue

#thread1.join()
#thread2.join()
#thread3.join()
#thread4.join()
#thread5.join()



    

print("ALL TASKS IN DECOMMISSION MODE HAVE BEEN COMPLETED")

