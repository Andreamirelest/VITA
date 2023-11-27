import RPi.GPIO as GPIO
import board
GPIO.setmode(GPIO.BCM)
GPIO.setup(0,GPIO.OUT)
GPIO.output(0,GPIO.HIGH)
