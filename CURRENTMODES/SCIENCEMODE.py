# Title: cvssciencemodecorrected.py
# Configuration item identifier:
# Purpose:
# The following code is a merged code from previous NEWread_environ_mux_data.py / NEWread_spec_mux_data.py / newLEDs.py
# codes, the purpose of this code is for LEDs, environmental sensors, and spectrometers to work simultaneously.
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

#update previous file

with open("lastMode.txt", "r+") as f:
    f.seek(0)
    f.truncate(0)
    f.writelines("SCIENCEMODE.py")
    f.close()


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
                lineCounter += 1
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

environmentalLineCounter = 0
spectroLineCounter = 0
tcsLineCounter = 0

def saveEnvironmentalData(data):
    global environmentalLineCounter
    environment_directory = "CURRENTMODES\Environment"

    os.makedirs(environment_directory, exist_ok = True)
    file_path = os.path.join(environment_directory, "environmentalData.csv")
    with open(file_path, "a") as f:
        environmentalLineCounter = cyclicFileWriting(f, environmentalLineCounter, data)
    print(data)

def saveSpectrometerData(data, spectroNum):
    global environmentalLineCounter
    experiment_directory = "CURRENTMODES\Experiment"

    os.makedirs(experiment_directory, exist_ok = True)
    file_path = os.path.join(experiment_directory, "spectrometreData%s.csv" % str(spectroNum))
    with open(file_path, "a") as f:
        spectroLineCounter = cyclicFileWriting(f, spectroLineCounter, data)
    print(data)

def saveTcsData(data):
    global tcsLineCounter
    experiment_directory = "CURRENTMODES\Experiment"

    os.makedirs(experiment_directory, exist_ok = True)
    file_path = os.path.join(experiment_directory, "tcsData.csv")
    with open(file_path, "a") as f:
        tcsLineCounter = cyclicFileWriting(f, tcsLineCounter, data)
    print(data)


# Task 1: 

def task1():

        #importing external codes (steppermotor &  TCS) 


        # check this is correct 
        os.system("python V2FINALcsv.py") # make sure to have V2 CODE IN csv format here 
        data_tcs = os.system("python V2FINALcsv.py") # make sure to have V2 CODE IN csv format here # comment if code not working 

        saveTcsData(data_tcs)

        time.sleep(1)




# Task 2: Activate camera every 20 minutes
def task2():
    while True:
        os.system("sh pi_cam_uc444.sh")
        #time.sleep(1200)  # This should be 1200 (20 minutes)



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

#TBC include while loop here if necessary

def task4():


    # add while loop if necessary 

    i2c = board.I2C()
    mux = adafruit_tca9548a.TCA9548A(i2c)

    sensor1 = adafruit_bme680.Adafruit_BME680_I2C(mux[7])
    sensor2 = adafruit_bme680.Adafruit_BME680_I2C(mux[6])

    
    data_sensor1 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f},{:.2f}".format (time.time(), 1, sensor1.temperature, sensor1.pressure, sensor1.humidity, sensor1.gas)
    saveEnvironmentalData(data_sensor1)

    #time.sleep(60)  # Sleep for 60 seconds (1 minute)
    time.sleep(1)

    data_sensor2 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f},{:.2f}".format (time.time(), 2, sensor2.temperature, sensor2.pressure, sensor2.humidity, sensor2.gas)
    saveEnvironmentalData(data_sensor2)

    #time.sleep(60)  # Sleep for 60 seconds (1 minute)
    time.sleep(1)

# Task 5: Read data from spectrometers
def task5():
    i2c = board.I2C()
    mux = adafruit_tca9548a.TCA9548A(i2c)

    spectro1 = AS7341(mux[0])

    #while True:
    data_spectro1 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f}".format(
    time.time(), 1, spectro1.channel_415nm, spectro1.channel_480nm, spectro1.channel_555nm
        )
    saveSpectrometerData(data_spectro1, 1)

        
    spectro2= AS7341(mux[1])
    data_spectro2 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f}".format(time.time(),2,spectro2.channel_415nm,spectro2.channel_480nm,spectro2.channel_555nm)
 
    saveSpectrometerData(data_spectro2, 2)
    

#SPECTRO3
#Initialize the BME688 sensor on channel 2 
    spectro3= AS7341(mux[2])
    data_spectro3 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f}".format(time.time(),3,spectro3.channel_415nm,spectro3.channel_480nm,spectro3.channel_555nm)

 
    saveSpectrometerData(data_spectro3, 3)

#SPECTRO4
#CHANNEL 3 
    spectro4= AS7341(mux[3])
    data_spectro4 ="{:.2f},{:d},{:.2f}.{:.2f},{:.2f}".format(time.time(),4,spectro4.channel_415nm,spectro4.channel_480nm,spectro4.channel_555nm)

 
    saveSpectrometerData(data_spectro4, 4)

    time.sleep(1) #must be 300



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

print("ALL TASKS IN SCIENCE MODE HAVE BEEN COMPLETED")
