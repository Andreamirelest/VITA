import os

#Starts the watchdog timer
os.system("sudo systemctl start watchdog")

#run to check watchdog status
os.system("sudo systemctl status watchdog")

