#THE FOLLOWING CODE WILL TURN ON LEDS AND CAMERA

#4 pins will be used to control  ALL 24 leds 

#!/bin/sh




import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
raspi-gpio set 14 op 




#set up all GPIOs
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

#While loop 
while True:
 
 GPIO.output(14,GPIO.HIGH)
 GPIO.output(15,GPIO.HIGH)
 GPIO.output(18,GPIO.HIGH)
 GPIO.output(23,GPIO.HIGH)
 
