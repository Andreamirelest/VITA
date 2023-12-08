new code for camera in python version 

import subprocess
import time
import shutil



# this part of the code might need to be pasted in mode code when importing camera code to send file to results folder 

# Function to capture and save an image and send to outside results folder 
def capture_and_save_image(RESULTSFOLDER, cameraresults):
    output_file = f"{RESULTSFOLDER}/{cameraresults}.jpg"

# error handling within camera 

    try: 
        subprocess.run(["raspistill", "-o", output_file], check=True)
        print(f"Captured and saved image to {output_file}")
    except subprocess.CalledProcessError as e:
        # Handle the error 
        print(f"Error capturing image: {e}")
        #handle error (send a notification or retry) 


        # send notification 

        # This part TBC by adding server to send notification to 


        #send_notification(f"Error capturing image: {e}")


        # retry capturing image after 1 minute 


        time.sleep(60)
        capture_and_save_image(RESULTSFOLDER, cameraresults)
    

    #"subprocess.run(["raspistill", "-o", output_file]) # uncomment if necessary

# Folder where the images will be saved
output_folder = "/path/to/RESULTSFOLDER/"

# Loop to capture and save images every 5 minutes
while True:
    timestamp = time.strftime("%Y%m%d%H%M%S") 
    capture_and_save_image(output_folder, f"image_{timestamp}")
    print(f"Captured and saved image to {output_folder}")
    
#time.strftime("%Y%m%d%H%M%S"):uses the strftime function from the time module to format the current date and time into a string with a specific format. The format string "%Y%m%d%H%M%S" represents the year, month, day, hour, minute, and second. 
    time.sleep(300)  # 300 seconds = 5 minutes



# Set GPIO pins as outputs
subprocess.run(["raspi-gpio", "set", "4", "op"])
subprocess.run(["raspi-gpio", "set", "17", "op"])

# Set I2C settings
subprocess.run(["i2cset", "-y", "1", "0x70", "0x00", "0x01"])

# Set GPIO pins low
subprocess.run(["raspi-gpio", "set", "17", "dl"])
subprocess.run(["raspi-gpio", "set", "4", "dl"])

print("Choose camera A")
subprocess.run(["raspistill", "-o", "camera1.jpg"])

# Set I2C settings
subprocess.run(["i2cset", "-y", "1", "0x70", "0x00", "0x02"])

# Set GPIO pin 4 high
subprocess.run(["raspi-gpio", "set", "4", "dh"])

print("Choose Camera B")
subprocess.run(["raspistill", "-o", "camera2.jpg"])

print("Test OK")
