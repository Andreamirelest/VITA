import picamera
import time

#initialize camera
camera = picamera.PiCamera()

#set camera resolution and framerate
camera.resolution = (640, 480)
camera.framerate = 38

# initialize the doubleplexer
camera.sensor_mode = 2
#camera.set_clock(0, 24000000)
#camera.set_clock(1, 24000000)
#camera.set_fps(30)

# give the cameras time to warm up
time.sleep(2)

# capture an image from camera 1 and save it to a file
camera.shutter_speed = 5000
camera.iso = 800
camera.exposure_mode = 'night'
camera.capture('camera1.jpg')

#switch to camera 2
camera.switch_sensor(1)

# capture an image from camera 2 and save it to a file
camera.shutter_speed = 5000
camera.iso = 800
camera.exposure_mode = 'night'
camera.capture('camera2.jpg')

# release the resources used by the camera
camera.close()
