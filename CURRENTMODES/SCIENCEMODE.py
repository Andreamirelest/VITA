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

# HOUSEKEEPING DATA
housekeeping_directory = "HOUSEKEEPINGFOLDER/"
results_directory = "RESULTSFOLDER/"

housekeepingLineCounter = 0
sciencemodeLineCounter = 0
sciencemodeenvsensLineCounter = 0
sciencemodespectroLineCounter = 0
sciencespectrodataLineCounter = 0
sciencestcsLineCounter = 0
sciencetcsdataLineCounter = 0



def save_to_housekeeping_file(data):
    os.makedirs(housekeeping_directory, exist_ok=True)
    file_path = os.path.join(housekeeping_directory, "housekeepingscience.csv")
    with open(file_path, "a") as f:
        housekeepingLineCounter = cyclicFileWriting(f, housekeepingLineCounter, data)

    print(data)

def housekeeping_data(component, data):
    save_to_housekeeping_file(f"{component} status: {data}")


def save_to_results_file(data):
    os.makedirs(results_directory, exist_ok=True)
    file_path = os.path.join(results_directory, "sciencemode.csv")
    with open(file_path, "a") as f:
        sciencemodeLineCounter = cyclicFileWriting(f, sciencemodeLineCounter, data)
    print(data)

def sensor_results_file(data):
    os.makedirs(results_directory, exist_ok=True)
    file_path = os.path.join(results_directory, "sciencemodeenvsens.csv")
    with open(file_path, "a") as f:
        sciencemodeenvsensLineCounter = cyclicFileWriting(f, sciencemodeenvsensLineCounter, data)
    print(data)

def spectro_results_file(data):
    os.makedirs(results_directory, exist_ok=True)
    file_path = os.path.join(results_directory, "sciencemodespectro.csv")
    with open(file_path, "a") as f:
        sciencemodespectroLineCounter = cyclicFileWriting(f, sciencemodespectroLineCounter, data)
    print(data)

def spectro_results(data):
    with open("sciencespectrodata.csv", "a") as f:
        sciencespectrodataLineCounter = cyclicFileWriting(f, sciencespectrodataLineCounter, data)
    print(data)



#tcs results to outside folder RESULTS FOLDER 


def tcs_results_file(data): 
    os.makedirs(results_directory, exist_ok=True)    # check if directory exists 
    file_path = os.path.join(results_directory, "sciencestcs.csv")
    with open(file_path, "a") as f: 
        sciencestcsLineCounter = cyclicFileWriting(f, sciencestcsLineCounter, data)

    print (data)

    with open(file_path, "a") as f:    
        sciencestcsLineCounter = cyclicFileWriting(f, sciencestcsLineCounter, data)      
    print (data)


# tcs results 

def tcs_results(data):
    with open("sciencetcsdata.csv", "a") as f: 
        sciencetcsdataLineCounter = cyclicFileWriting(f, sciencetcsdataLineCounter, data)


# Task 1: 

def task1():

        #importing external codes (steppermotor &  TCS) 


        # check this is correct 
        os.system("python V2FINALcsv.py") # make sure to have V2 CODE IN csv format here 
        data_tcs = os.system("python V2FINALcsv.py") # make sure to have V2 CODE IN csv format here # comment if code not working 

        tcs_results_file(data_tcs)

        tcs_results(data_tcs)

        save_to_results_file(data_tcs)

        housekeeping_data("TCS SCIENCE MODE", data_tcs)



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

#TBC include while loop here if necessary

def task4():


    # add while loop if necessary 

    i2c = board.I2C()
    mux = adafruit_tca9548a.TCA9548A(i2c)

    sensor1 = adafruit_bme680.Adafruit_BME680_I2C(mux[7])
    sensor2 = adafruit_bme680.Adafruit_BME680_I2C(mux[6])

    
    data_sensor1 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f},{:.2f}".format (time.time(), 1, sensor1.temperature, sensor1.pressure, sensor1.humidity, sensor1.gas)
    save_to_results_file(data_sensor1)
    sensor_results_file(data_sensor1)


    save_to_housekeeping_file(data_sensor1)

    time.sleep(60)  # Sleep for 60 seconds (1 minute)

    data_sensor2 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f},{:.2f}".format (time.time(), 2, sensor2.temperature, sensor2.pressure, sensor2.humidity, sensor2.gas)
    save_to_results_file(data_sensor2)
    sensor_results_file(data_sensor2)

    save_to_housekeeping_file(data_sensor2)

    time.sleep(60)  # Sleep for 60 seconds (1 minute)

# Task 5: Read data from spectrometers
def task5():
    i2c = board.I2C()
    mux = adafruit_tca9548a.TCA9548A(i2c)

    spectro1 = AS7341(mux[0])

    #while True:
    data_spectro1 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f}".format(
    time.time(), 1, spectro1.channel_415nm, spectro1.channel_480nm, spectro1.channel_555nm
        )
    save_to_results_file(data_spectro1)
    spectro_results_file(data_spectro1)


    save_to_housekeeping_file(data_spectro1)

        
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
