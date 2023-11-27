# SINGLE ENVIRONMENT SENSOR  DATA 


 #imports 
import time 
import board
import adafruit_bme680
  

#sensor object , communicating over boards default I2C()

i2c = board.I2C()

sensor1 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

 #while loop 

while True:
    print("Sensor1 :\n" + "Temperature: %.2f C" % sensor1.temperature +
    "Pressure: %.2f hPa\n" % sensor1.pressure + 
    "Humidity: %.2f %%\n" % sensor1.humidity +  
    "Gas resistance: %d ohm\n" % sensor1.gas) 
     

    time.sleep(1)
 
#    print("\nTemperature: %0.1f C" % sensor1.temperature)
 #   print("Gas resisance: %d ohm" % sensor1.gas)
  #  print("Humidity: %.2f %%\n" % sensor1.humidity)
   # print("Pressure: %.2f hPa\n" % sensor1.pressure) 

#    time.sleep(1)
