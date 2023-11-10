








import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set up all GPIOs
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(1,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(0,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
#While loop 
while True:
 GPIO.output(12,GPIO.HIGH)
 GPIO.output(14,GPIO.HIGH)
 GPIO.output(15,GPIO.HIGH)
 GPIO.output(18,GPIO.HIGH)
 GPIO.output(23,GPIO.HIGH)
 GPIO.output(24,GPIO.HIGH)
 GPIO.output(25,GPIO.HIGH)
 GPIO.output(8,GPIO.HIGH)
 GPIO.output(7,GPIO.HIGH)
 GPIO.output(1,GPIO.HIGH)
 GPIO.output(19,GPIO.HIGH)
 GPIO.output(16,GPIO.HIGH)
 GPIO.output(4,GPIO.HIGH)
 GPIO.output(17,GPIO.HIGH)
 GPIO.output(27,GPIO.HIGH)
 GPIO.output(13,GPIO.HIGH)
 GPIO.output(10,GPIO.HIGH)
 GPIO.output(9,GPIO.HIGH)
 GPIO.output(11,GPIO.HIGH)
 GPIO.output(5,GPIO.HIGH)
 GPIO.output(0,GPIO.HIGH)
