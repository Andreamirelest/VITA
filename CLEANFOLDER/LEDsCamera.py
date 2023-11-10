#THE FOLLOWING CODE WILL TURN ON ALL 24 LEDS USING PINS 14,15,18,23 AND CAMERA SIMULTANEOUSLY /
#!/bin/sh

import RPi.GPIO as GPIO
from time 
import sleep

raspi-gpio set 4 op 
raspi-pgio set 17 op 
I2cset -y 1 0x70 0x00 0x01

#raspi-pgio set 17 dl #set the gpio17 low
#raspi-gpio set 4 dl  #set the gpio 14 low

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
 sleep(4)
 GPIO.output(14,GPIO.LOW)
 sleep(1)
 GPIO.output(15,GPIO.HIGH)
 sleep(4)
 GPIO.output(15,GPIO.LOW)
 sleep(1)
 GPIO.output(18,GPIO.HIGH)
 sleep(4)
 GPIO.output(18,GPIO.LOW)
 sleep(1)
GPIO.output(23,GPIO.HIGH)
sleep(4)
GPIO.output(23,GPIO.LOW)
sleep(4)


i2cset -y 1 0x70 0x00 0x01
raspi-pgio set 17 dl
raspi-pgio set 4 dl 
echo "Choose camera A"
raspistill -o camera1.jpg 

i2cset -y 1 0x70 0x00 0x02 
raspi-pgio set 17 dl
raspi-gpio set 4 dh

echo "Choose Camera B"
raspistill -o camera2.jpg 
echo "TEST OK" 



