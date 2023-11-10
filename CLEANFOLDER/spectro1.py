
"""
Title: read_spectro_data.py
Configuration item identifier: OBDH_spectro_data-v1.0


Purpose: to read spectro data
Original author: Rocio Valera Falla - eayrv@nottingham.ac.uk
Creation date: 23/02/2023

Before running the script, the Adafruit_Blinka library must be
installed. This may also require enabling I2C on the RPi
To do this:
sudo pip3 install adafruit-circuitpython-as7341

This program access data from the Adafruit AS7341 sensor
1. Import the necessary libraries. board from the adafruit_blinka
library (which provides low-level hardware access), adafruit_as7341
from the Adafruit_CircuitPython_AS7341 library (which provides a
high-level interface to the spectrometer) and time
2. Create an I2C object using the board pins for SCL and SDA
3. Create a AS7341 object using the I2C object we just created
4. Start an infinite loop that read and prints out the data
from the spectrometer with 1-second delay between readings.



CHANGES:

Date:
Modifier name:
Description:
"""

import board
import time
import adafruit_as7341

# create an I2C bus object
i2c = board.I2C()

# create a spectrometer object
spec = adafruit_as7341.AS7341(i2c)

while True:
    # read current reading for the 415, 445, 480, 515, 555, 590, 630 and 680 band
    channel_415nm = spec.channel_415nm
  #  channel_445nm = spec.channel_445nm
    channel_480nm = spec.channel_480nm
   # channel_515nm = spec.channel_515nm
    channel_555nm = spec.channel_555nm
   # channel_590nm = spec.channel_590nm
   # channel_630nm = spec.channel_630nm
   # channel_680nm = spec.channel_680nm

    # print the results
    print("Channel 415 nm/Violet data:",  channel_415nm)
   # print("Channel 445 nm/Indigo data:", channel_445nm)
    print("Channel 480 nm/Blue data:", channel_480nm)
  #  print("Channel 515 nm/Cyan data:", channel_515nm)
    print("Channel 555 nm/Green data:", channel_555nm)
   # print("Channel 590 nm/Yellow data:", channel_590nm)
   # print("Channel 630 nm/Orange data:", channel_630nm)
   # print("Channel 680 nm/Red data:", channel_680nm)
    time.sleep(5)
