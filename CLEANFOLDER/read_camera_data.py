"""
Title: read_camera_data.py
Configuration item identifier: OBDH_camera_data-v1.0


Purpose: To read camera data
Original author: Rocio Valera Falla - eayrv@nottingham.ac.uk
Creation date: 23/02/2023

Before starting the script, the camera might need to be enabled.
To do this:
sudo raspi-config
Interfacing options
P1 Camera
After camera has been enabled, RPi might need to be rebooted.

In this script, we first import the time and picamera libraries.
We then create an instance of the PiCamera class and set the
resolution and framerate using the resolution and framerate
attributes. We give the camera a couple of seconds to warm up
using the time.sleep() function.

We then capture an image using the capture() method and save it
to a file named image.jpg. Finally, we capture a 10-second video
using the start_recording() and stop_recording() methods and
save it to a file named video.h264.


CHANGES:

Date:
Modifier name:
Description:
"""

import picamera
import time

# create an instance of the PiCamera class
camera = picamera.PiCamera()

# set the camera resolution and framerate
camera.resolution = (640, 480)
camera.framerate = 30

# give the camera time to warm up
time.sleep(2)

# capture an image and save it to a file
camera.capture('image.jpg')

# capture a video for 10 seconds and save it to a file
camera.start_recording('video.h264')
time.sleep(10)
camera.stop_recording()
