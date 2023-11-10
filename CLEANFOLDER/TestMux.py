import board
import adafruit_tca9548a
i2c = board.I2C()
tca = adafruit_tca9548a.TCA9548A(i2c)
for channel in range(8):
	if tca[channel].try_lock():
	 print("Channel{}:".format(channel), end="")
	addresses=tca[channel].scan()
	print([hex(address) for address in addresses if address !=0x70])
	tca[channel].unlock()
