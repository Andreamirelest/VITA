#THIS CODE WILL SERVE TO TEST STEPPER MOTOR
#!/usr/bin/env python3

"""
test example file for module:rpiMotorlib.py

file: RpiMotorLib.py class BYJMotor
"""
import time
import RPi.GPIO as GPIO

#INSTALLED LIBRARY IMPORT

from RpiMotorLib import RpiMotorLib
"""
For testing motor step
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
"""
#Declare name 
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne" , "28BYJ")

def main():
 """ main function loop"""

 #test for motor 28BYJ48
 #Connect GPIO to [IN1 , IN2 , IN3 , IN4] on Motor PCN 
 GpioPins= [24, 25, 8, 1]   #pins can be changed here 

 #Arguments for motor run function

# time.sleep(0.1)
 #input("Press <Enter> to continue Test1")
#mymotortest.motor_run(GpioPins,.05,128, True, True,"full", .05)
 #time.sleep(1)
 #input("Press <Enter> to continue Test2")
 #mymotortest.motor_run(GpioPins,.0001,256, False, True,"half", .05)
 time.sleep(1)
 input("Press <Enter> to continue Testcounterclockwise")
 mymotortest.motor_run(GpioPins,.000000000000000000000001,25600000,False,True,"full", .5)  #second false stands for no data being shown
 time.sleep(1)
 input("Press <Enter> to continue Testclockwise")
 mymotortest.motor_run(GpioPins, .0000000000000000000000000001, 25600000, True, True, "full", .5)
 time.sleep(1)
 input("Press <Enter> to continue Test5")
 mymotortest.motor_run(GpioPins,.01,512,False,False,"half", .05)

"""
#need for testing motor stop
def button_callback(channel)
print("Test file: Stopping motor")
mymotortest.motor_stop()
"""
 #MAIN 

if __name__ == '__main__':

 print("START") 
 main()
 GPIO.cleanup()
 exit()


  #END 



