"""
Title: read_spec_mux_data.py
Configuration item identifier: OBDH_spectro_multiplexer_data-v2.0


Purpose: To read multiple sensors data via the multiplexer
cOriginal author: Rocio Valera Falla - eayrv@nottingham.ac.uk
Creation date: 23/02/2023

Before running the script, the Adafruit_Blinka library must be
installed. This may also require enabling I2C on the RPi
To do this:
sudo pip3 install adafruit-circuitpython-tca9548a
sudo pip3 install adafruit-circuitpython-as7341

This program access data from the Adafruit TCA8548A multiplexer
1. Import the necessary libraries. board and busio from the adafruit_blinka
library (which provides low-level hardware access), adafruit_tca9548a
from the Adafruit_CircuitPython_TCA9548A library (which provides a
high-level interface to the multiplexer), adafruit_as7341
from the Adafruit_CircuitPython_AS7341 library (which provides a
high-level interface to the spectrometer)
2. Create an I2C object using the board pins for SCL and SDA
3. Create a TCA9548A object using the I2C object we just created
4. Create four instances of the AS7441 spectrometer, one for each channel of the
multiplexer.
5. Read and print the wavelength and calibration data of each spectrometer.


CHANGES:

Date: 27/04/2023
Modifier name: Rocio
Description: Use smbus instead of adafruit_tcs9548a for reading data
through the multiplexer.
"""
# import smbus2
import time
import board
from adafruit_as7341 import AS7341
import adafruit_tca9548a

# Set the address of the TCA9548 I2C multiplexer
# MUX_ADDRESS = 0x70
i2c = board.I2C()
mux = adafruit_tca9548a.TCA9548A(i2c)
# Set the address of the AS7341 spectrometers
# spec_1_address = 0x39
# spec_2_address = 0x39

# Set the channel numbers of the AS7341 spectrometers
# spec_0_channel = 0
# spec_1_channel = 1

# Initialize the I2B bus
# bus = smbus2.SMBus(1)
# Set the channel of the multiplexer to read data form sensor 1
# bus.write_byte(MUX_ADDRESS, 1 << spec_0_channel)

# Initialize the TCA4598A spectro on channel 0
# spectro1 = AS7341(i2c_addr=spec_1_address, i2c_device=bus)
while True: 
 spectro1 = AS7341(mux[0])
 print("Spectro 1 channel 415 nm/Violet data:", spectro1.channel_415nm)
 print("Spectro 1 channel 480 nm/Blue data:", spectro1.channel_480nm)
 print("Spectro 1 channel 555 nm/Green data:", spectro1.channel_555nm) 
# Read sensor data from channel 2
#data1 = spectro1.get_sensor_data()

# Print the sensor data from channel 2

#print("Spec 1:")
#print("Calibration data:", spectro1.read_calibration())
#print("Wavelength (nm):", spectro1.wavelength)


# Set the channel of the multiplexer to read data from spectro 2
#bus.write_byte(MUX_ADDRESS, 1 << spec_1_channel)

# Initialize the BME688 sensor on channel 1
# spectro2 = AS7341(mux[1])
# print("Spectro 2 channel 415 nm/Violet data:", spectro2.channel_415nm)
# print("Spectro 2 channel 480 nm/Blue data:", spectro2.channel_480nm)
# print("Spectro 2 channel 555 nm/Green data:", spectro2.channel_555nm)

#Initialize the BME688 sensor on channel 2
 #spectro3 = AS7341(mux[2])
 #print("Spectro 3 channel 415 nm/Violet data:", spectro3.channel_415nm)
 #print("Spectro 3 channel 480 nm/Blue data:", spectro3.channel_480nm)
 #print("Spectro 3 channel 555 nm/Green data:", spectro3.channel_555nm)

# channel 3
# spectro4=AS7341(mux[3])
# print("Spectro 4 channel 415 nm/Violet data:", spectro4.channel_415nm)
# print("Spectro 4 channel 480 nm/Blue data:", spectro4.channel_480nm)
# print("Spectro 4 channel 555 nm/Green data:", spectro4.channel_555nm)
# time.sleep(1)
# Read sensor data from channel 3
#data2 = spectro2.get_sensor_data()

# Print the sensor data from channel 2
#print("Spec 2:")
#print("Calibration data:", spectro2.read_calibration())
#print("Wavelength (nm):", spectro2.wavelength)

