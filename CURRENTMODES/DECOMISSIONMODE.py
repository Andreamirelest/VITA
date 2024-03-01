
# Title: CSVDECOMMISSIONMODE.py
# Configuration item identifier:
# Purpose:
# CHANGES: THIS IS THE LAST UPDATE OF A CLEAN CODE 
# Date: 7th July 2023
# Modifier name: Andrea Mireles Tavarez
# Description:

# Import necessary libraries
import os
import time
import threading
import board
import adafruit_tca9548a
import adafruit_bme680
#from bme680 import BME680

# Import required modules for environmental sensors
from adafruit_as7341 import AS7341
import adafruit_tca9548a

# Import necessary modules for LEDs
import RPi.GPIO as GPIO
from time import sleep

#To check remaining SD card storage below threshold.
from cyclicDataTest import cyclicCheck

def cyclicFileWriting(f, lineCounter, data):
    if cyclicCheck():
        try:
            f.write(data)
            f.write("\n")
        except:
            print("WRITE FAILED!!!")
    else:
        print("Out of storage space")
        fileData = f.readLines()
        noLines = len(fileData)

        if lineCounter < noLines:
            try:
                fileData[lineCounter] = fileData
                lineCounter += lineCounter
                print (data)
            except:
                print ("Write Failed")
        else:
            lineCounter = 0
            try:
                fileData[lineCounter] = fileData

            except:
                print ("Write Failed")
    return lineCounter


# HOUSEKEEPING DATA
housekeeping_directory = "HOUSEKEEPINGFOLDER/"
results_directory = "RESULTSFOLDER/"

housekeepingdecommissionLineCounter = 0
decommissionLineCounter = 0
decommissionenvsensLineCounter = 0
decommissionspectroLineCounter = 0
decommissionspectrodataLineCounter = 0

def housekeeping_data(component, data):
    save_to_housekeeping_file(f"{component} status: {data}")


def save_to_housekeeping_file(data):
    os.makedirs(housekeeping_directory, exist_ok=True)
    file_path = os.path.join(housekeeping_directory, "housekeepingdecommission.csv")
    with open(file_path, "a") as f:
        housekeepingdecommissionLineCounter = cyclicFileWriting(f, housekeepingdecommissionLineCounter, data)
    print(data)

def save_to_results_file(data):
    os.makedirs(results_directory, exist_ok=True)
    file_path = os.path.join(results_directory, "decommission.csv")
    with open(file_path, "a") as f:
        decommissionLineCounter = cyclicFileWriting(f, decommissionLineCounter, data)
    print(data)

def sensor_results_file(data):
    os.makedirs(results_directory, exist_ok=True)
    file_path = os.path.join(results_directory, "decommissionenvsens.csv")
    with open(file_path, "a") as f:
        decommissionenvsensLineCounter = cyclicFileWriting(f, decommissionenvsensLineCounter, data)
    print(data)

def spectro_results_file(data):
    os.makedirs(results_directory, exist_ok=True)
    file_path = os.path.join(results_directory, "decommissionspectro.csv")
    with open(file_path, "a") as f:
        decommissionspectroLineCounter = cyclicFileWriting(f, decommissionspectroLineCounter, data)
    print(data)

def spectro_results(data):
    with open("decommissionspectrodata.csv", "a") as f:
        decommissionspectrodataLineCounter = cyclicFileWriting(f, decommissionspectrodataLineCounter, data)
    print(data)

# Task 1: Activate stepper motor anticlockwise in decommission mode
def task1():
    os.system("python STEPPERMOTOR_ANTICLOCK.py")  # Steppermotor is activated on reverse within 5 minutes of starting this mode
    time.sleep(1)

# Task 2: Activate camera every 20 minutes
def task2():
    while True:
        os.system("sh pi_cam_uc444.sh")
        time.sleep(1200)  # This should be 1200 (20 minutes)

# TBC still missing to send camera files to cvs format 


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

    sleep(1)

    while True:
        data_sensor1 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f},{:.2f}".format(
            time.time(), 1, sensor1.temperature, sensor1.pressure, sensor1.humidity, sensor1.gas
        )
        save_to_results_file(data_sensor1)
        sensor_results_file(data_sensor1)

       # time.sleep(60)  # Sleep for 60 seconds (1 minute)

        data_sensor2 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f},{:.2f}".format(
            time.time(), 2, sensor2.temperature, sensor2.pressure, sensor2.humidity, sensor2.gas
        )
        save_to_results_file(data_sensor2)
        sensor_results_file(data_sensor2)

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

print("ALL TASKS IN DECOMMISSION MODE HAVE BEEN COMPLETED")


