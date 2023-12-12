
# Title: CSVREHYDRATIONMODE.py
# Configuration item identifier:
# Purpose:
# The following code is a merged code from previous NEWread_environ_mux_data.py / NEWread_spec_mux_data.py / newLEDs.py
# codes, the purpose of this code is for LEDs, environmental sensors, and spectrometers to work simultaneously.
# CHANGES: THIS IS THE LAST UPDATE OF A CLEAN CODE 
# Date: 7th July 2023
# Modifier name: Andrea Mireles Tavarez
# Description: latest version of rehydration mode csv fomrta done on the 12/DEC/2023

# Import necessary libraries
import os
import time
import threading
import board
import adafruit_tca9548a
import adafruit_bme680
from bme680 import BME680

# Import required modules for environmental sensors
from adafruit_as7341 import AS7341
import adafruit_tca9548a

# Import necessary modules for LEDs
import RPi.GPIO as GPIO
from time import sleep

# HOUSEKEEPING DATA
housekeeping_directory = "/path/to/HOUSEKEEPINGFOLDER/"
results_directory = "/path/to/RESULTSFOLDER/"

def save_to_housekeeping_file(data):
    os.makedirs(housekeeping_directory, exist_ok=True)
    file_path = os.path.join(housekeeping_directory, "housekeepingrehydration.csv")
    with open(file_path, "a") as f:
        f.write(data + "\n")
    print(data)

def save_to_results_file(data):
    os.makedirs(results_directory, exist_ok=True)
    file_path = os.path.join(results_directory, "rehydration.csv")
    with open(file_path, "a") as f:
        f.write(data + "\n")
    print(data)

def sensor_results_file(data):
    os.makedirs(results_directory, exist_ok=True)
    file_path = os.path.join(results_directory, "rehydrationenvsens.csv")
    with open(file_path, "a") as f:
        f.write(data + "\n")
    print(data)

def spectro_results_file(data):
    os.makedirs(results_directory, exist_ok=True)
    file_path = os.path.join(results_directory, "rehydrationspectro.csv")
    with open(file_path, "a") as f:
        f.write(data + "\n")
    print(data)

def spectro_results(data):
    with open("rehydrationspectrodata.csv", "a") as f:
        f.write(data + "\n")
    print(data)



def tcs_results_file(data): 
    os.makedirs(results_directory, exist_ok=True)    # check if directory exists 
    file_path = os.path.join(results_directory, "rehydrationtcs.csv")
    with open(file_path, "a") as f: 
        f.write(data + "\n")
    print (data)

# tcs results 

def tcs_results(data):
    with open("rehydrationtcsdata.csv", "a") as f: 
        f.write(data)
        f.write("\n")
    print (data)






# Task 1: Activate stepper motor clockwise in rehydration mode
def task1():


        # importing external codes (steppermotor & TCS) 
        os.system("python STEPPERMOTOR_CLOCKWISE.py") 
        time.sleep(1)


        os.system("python V2FINALcsv.py") 
 

        # make sure to have V2 CODE IN csv format 
        data_tcs = os.system("python V2FINALcsv.py") 

        tcs_results_file(data_tcs)

        tcs_results(data_tcs)

        save_to_results_file(data_tcs)

        housekeeping_data("TCS REHYDRATION MODE", data_tcsrehydration)

        tcs_results_file(tcsdata_tcs)

        time.sleep(1)    

# Task 2: Activate camera every 20 minutes
def task2():
    while True:
        os.system("sh pi_cam_uc444.sh")
        time.sleep(1200)  # This should be 1200 (20 minutes)

# Task 3: Control LEDs
def task3():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Set up GPIO pins for LEDs
    GPIO.setup(14, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)

    while True:
        # Control the LEDs here as needed
        GPIO.output(14, GPIO.HIGH)
        sleep(2)
        GPIO.output(14, GPIO.LOW)
        sleep(1)
        GPIO.output(15, GPIO.HIGH)
        sleep(2)
        GPIO.output(15, GPIO.LOW)
        sleep(1)
        GPIO.output(18, GPIO.HIGH)
        sleep(2)
        GPIO.output(18, GPIO.LOW)
        sleep(1)
        GPIO.output(23, GPIO.HIGH)
        sleep(2)
        GPIO.output(23, GPIO.LOW)
        sleep(1)

# Task 4: Read data from environmental sensors
def task4():
    i2c = board.I2C()
    mux = adafruit_tca9548a.TCA9548A(i2c)

    sensor1 = adafruit_bme680.Adafruit_BME680_I2C(mux[7])
    sensor2 = adafruit_bme680.Adafruit_BME680_I2C(mux[6])

   # sleep(1)

    while True:
        data_sensor1 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f},{:.2f}".format(
            time.time(), 1, sensor1.temperature, sensor1.pressure, sensor1.humidity, sensor1.gas
        )
        save_to_results_file(data_sensor1)
        sensor_results_file(data_sensor1)

        housekeeping_data("Sensor 1 ", data_sensor1)

        #time.sleep(60)  # Sleep for 60 seconds (1 minute)

        data_sensor2 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f},{:.2f}".format(
            time.time(), 2, sensor2.temperature, sensor2.pressure, sensor2.humidity, sensor2.gas
        )
        save_to_results_file(data_sensor2)
        sensor_results_file(data_sensor2)

        housekeeping_data("Sensor2", data_sensor2)

        time.sleep(60)  # Sleep for 60 seconds (1 minute)

# Task 5: Read data from spectrometers


def task5():
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



    housekeeping_data("Spectrometer1", data_spectro1)


#Read sensor data from channel 2
#Set the channel of the multiplexer to read data from spectro 2

 
#SPECTRO 2 
#Initialize the BME688 sensor on channel 1 
    spectro2= AS7341(mux[1])
    data_spectro2 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f}".format(time.time(),2,spectro2.channel_415nm,spectro2.channel_480nm,spectro2.channel_555nm)
 
    save_to_results_file(data_spectro2)
    spectro_results_file(data_spectro2)
    spectro_results(data_spectro2)

    housekeeping_data("Spectrometer2", data_spectro2)
    

#SPECTRO3
#Initialize the BME688 sensor on channel 2 
    spectro3= AS7341(mux[2])
    data_spectro3 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f}".format(time.time(),3,spectro3.channel_415nm,spectro3.channel_480nm,spectro3.channel_555nm)

 
    save_to_results_file(data_spectro3)
    spectro_results_file(data_spectro3)

    spectro_results(data_spectro3)

    housekeeping_data("Spectrometer3", data_spectro3)

#SPECTRO4
#CHANNEL 3 
    spectro4= AS7341(mux[3])
    data_spectro4 ="{:.2f},{:d},{:.2f}.{:.2f},{:.2f}".format(time.time(),4,spectro4.channel_415nm,spectro4.channel_480nm,spectro4.channel_555nm)

 
    save_to_results_file(data_spectro4)
    spectro_results_file(data_spectro4)

    spectro_results(data_spectro4)

    housekeeping_data("Spectrometer4", data_spectro4)

     

 


    time.sleep(300)  # Sleep for 300 seconds (5 minutes)

# Create and start threads for each task
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)
thread3 = threading.Thread(target=task3)
thread4 = threading.Thread(target=task4)
thread5 = threading.Thread(target=task5)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

# Wait for all threads to finish
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()

print("ALL TASKS IN REHYDRATION MODE HAVE BEEN COMPLETED")

