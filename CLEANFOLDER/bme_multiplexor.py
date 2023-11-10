import smbus2
#import adafruit_bme680
#from library import bme680
from bme680 import BME680

# Set the address of the TCA9548 I2C multiplexer
MUX_ADDRESS = 0x70

# Set the addresses of the BME688 sensors
SENSOR_2_ADDRESS = 0x76
SENSOR_3_ADDRESS = 0x76

# Set the channel numbers of the BME688 sensors
SENSOR_2_CHANNEL = 2
SENSOR_3_CHANNEL = 3

# Initialize the I2C bus
bus = smbus2.SMBus(1)

# Set the channel of the multiplexer to read data from sensor 2
bus.write_byte(MUX_ADDRESS, 1 << SENSOR_2_CHANNEL)

# Initialize the BME688 sensor on channel 2
sensor2 = BME680(i2c_addr=SENSOR_2_ADDRESS, i2c_device=bus)
#sensor2 = adafruit_bme680.Adafruit_BME680_I2C(i2c_addr=SENSOR_2_ADDRESS, i2c_device =bus)

# Read sensor data from channel 2
data2 = sensor2.get_sensor_data()

# Print the sensor data from channel 2
print("Sensor 2:")
print("Temperature: {} C".format(sensor2.data.temperature))
print("Pressure: {} hPa".format(sensor2.data.pressure))
print("Humidity: {} %RH".format(sensor2.data.humidity))
print("Gas Resistance: {} Ohms".format(sensor2.data.gas_resistance))

# Set the channel of the multiplexer to read data from sensor 3
bus.write_byte(MUX_ADDRESS, 1 << SENSOR_3_CHANNEL)

# Initialize the BME688 sensor on channel 3
sensor3 = BME680(i2c_addr=SENSOR_3_ADDRESS, i2c_device=bus)
#sensor3 = adafruit_bme680.Adafruit_BME680_I2C(i2c_addr=SENSOR_3_ADDRESS, i2c_device=bus)

# Read sensor data from channel 3
data3 = sensor3.get_sensor_data()

# Print the sensor data from channel 3
print("Sensor 3:")
print("Temperature: {} C".format(sensor3.data.temperature))
print("Pressure: {} hPa".format(sensor3.data.pressure))
print("Humidity: {} %RH".format(sensor3.data.humidity))
print("Gas Resistance: {} Ohms".format(sensor3.data.gas_resistance))
