import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set up all GPIOs
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)


#While loop 
while True:
 GPIO.output(14,GPIO.HIGH)
 sleep(5)
 GPIO.output(14,GPIO.LOW)
 sleep(1)
 GPIO.output(15,GPIO.HIGH)
 sleep(5)
 GPIO.output(15,GPIO.LOW)
 sleep(1)
 GPIO.output(18,GPIO.HIGH)
 sleep(5)
 GPIO.output(18,GPIO.LOW)
 sleep(1)
 GPIO.output(23,GPIO.HIGH)
 sleep(5)
 GPIO.output(23,GPIO.LOW)
 sleep(1)
