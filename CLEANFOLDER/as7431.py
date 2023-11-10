from adafruit_as7341 import AS7341
import board

i2c = board.I2C()

sensor = AS7341(i2c)

print("F1 - 415nm/Violet  %s" % sensor.channel_415nm)
print("F2 - 445nm//Indigo %s" % sensor.channel_445nm)
print("F3 - 480nm//Blue   %s" % sensor.channel_480nm)
print("F4 - 515nm//Cyan   %s" % sensor.channel_515nm)
print("F5 - 555nm/Green   %s" % sensor.channel_555nm)
print("F6 - 590nm/Yellow  %s" % sensor.channel_590nm)
print("F7 - 630nm/Orange  %s" % sensor.channel_630nm)
print("F8 - 680nm/Red     %s" % sensor.channel_680nm)




