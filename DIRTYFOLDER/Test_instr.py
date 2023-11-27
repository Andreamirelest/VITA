import RPi.GPIO as GPIO
import time
from time import sleep
import board
from adafruit_as7341 import AS7341

#Set the Spectrometer
i2c = board.I2C()
sensor = AS7341(i2c)
GPIO.setmode(GPIO.BCM)
#Set the pin for LEDs
GPIO.setup(17,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
#Tghe main code
def save_to_results_file(results):
 with open("Test_instr_results.txt", "a") as f:
  f.write(results)
  f.write("\n")
  print(results)
mode =int(input("To carry out the test witouth LEDs press 1:"))
if mode == 1:
 while True:
  GPIO.output(4,GPIO.LOW)
  GPIO.output(17,GPIO.LOW)
  time.sleep(3)
  results = ("\n Time: %d \n" % time.time() + "sfGFP -515 nm: %s \n" % sensor.channel_515nm + "F5  -555nm: %s" % sensor.channel_555nm)
  save_to_results_file(results)
  time.sleep(1)
else: 
 while True:
  GPIO.output(4,GPIO.HIGH)
  GPIO.output(17,GPIO.HIGH)
  time.sleep(3)
  results = ("\nTime: %d \n" % time.time() + "sfGFP -515 nm: %s \n" % sensor.channel_515nm + "F5 -555nm: %s" % sensor.channel_555nm)
  save_to_results_file(results)
 # time.sleep(1)
 # GPIO.output(0,GPIO.LOW)
 # time.sleep(1)
