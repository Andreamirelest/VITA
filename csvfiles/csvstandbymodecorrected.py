# Title: MERGED_CODE.py
# Configuration item identifier:
# Purpose:
# The following code is a merged code from previous NEWread_environ_mux_data.py / NEWread_spec_mux_data.py / newLEDs.py
# codes, the purpose of this code is for LEDs, environmental sensors, and spectrometers to work in a simultaneous way.

# CHANGES:

# Date: 7th July 2023
# Modifier name: Andrea Mireles Tavarez
# Description:

import os
import time
import threading
import board
import adafruit_tca9548a
import adafruit_bme680
from bme680 import BME680
from adafruit_as7341 import AS7341
import RPi.GPIO as GPIO
from time import sleep

# HOUSEKEEPING DATA
housekeeping_directory = "/path/to/HOUSEKEEPINGFOLDER/"

def save_to_housekeeping_file(data):
    os.makedirs(housekeeping_directory, exist_ok=True)
    file_path = os.path.join(housekeeping_directory, "housekeepingstandby.csv")
    with open(file_path, "a") as f:
        f.write(data)
        f.write("\n")
    print(data)

# Housekeeping data function for each component
def housekeeping_data(component, data):
    save_to_housekeeping_file(f"{component} status: {data}")

results_directory = "/path/to/RESULTSFOLDER/"

def save_to_results_file(data):
    os.makedirs(results_directory, exist_ok=True)
    file_path = os.path.join(results_directory, "standby.csv")
    with open(file_path, "a") as f:
        f.write(data)
        f.write("\n")
    print(data)

# Define functions for environmental sensor data
def sensor_results_file(data):
    os.makedirs(results_directory, exist_ok=True)
    file_path = os.path.join(results_directory, "standbyenvsens.csv")
    with open(file_path, "a") as f:
        f.write(data)
        f.write("\n")
    print(data)

def sensor_results(data):
    os.makedirs(results_directory, exist_ok=True)
    file_path = os.path.join(results_directory, "standbyenvsens.csv")
    with open(file_path, "a") as f:
        f.write(data)
        f.write("\n")
    print(data)

def task1():
    while True:
        os.system("sh pi_cam_uc444.sh")
        time.sleep(5)
        break

# Housekeeping For camera
    camera_data = "OK"
    housekeeping_data("Camera", camera_data)

def task2():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # set up all 4 GPIOs
    # instead of using 24 GPIOs, 4 GPIOs are used to power all 24 LEDs
    GPIO.setup(14, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)

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

def task3():

#add while loop if necessary


    i2c = board.I2C()
    mux = adafruit_tca9548a.TCA9548A(i2c)

    # Set up the BME688 sensors connected to channels 4 and 5 of the multiplexer
    sensor1 = adafruit_bme680.Adafruit_BME680_I2C(mux[7])
    sensor2 = adafruit_bme680.Adafruit_BME680_I2C(mux[6])
    #time.sleep(1)

    data_sensor1 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f},{:.2f}".format(
        time.time(), 1, sensor1.temperature, sensor1.pressure, sensor1.humidity, sensor1.gas)

    save_to_results_file(data_sensor1)
    sensor_results_file(data_sensor1)
    sensor_results(data_sensor1)
    housekeeping_data("Sensor1", data_sensor1)
   # time.sleep(1)



    data_sensor2 = "{:.2f},{:d},{:.2f},{:.2f},{:.2f},{:.2f}".format(
        time.time(), 1, sensor2.temperature, sensor2.pressure, sensor2.humidity, sensor2.gas)

    save_to_results_file(data_sensor2)
    sensor_results_file(data_sensor2)
    sensor_results(data_sensor2)
    housekeeping_data("Sensor2", data_sensor2)
    time.sleep(1)  #must be 60

# threading
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)
thread3 = threading.Thread(target=task3)

thread1.start()
thread1.join()
thread2.start()
thread2.join()
thread3.start()
thread3.join()

print("ALL TASKS IN STANDBY MODE HAVE BEEN COMPLETED")


 
