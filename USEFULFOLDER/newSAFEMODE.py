# SAFE MODE CODE 
import time 
import _thread
import os
import sys

moveModes = ["newSCIENCEMODE.py", "newREHYDRATIONMODE.py"]
#Checks if was previously in science / rehydrate mode - will move into those
with open("lastMode.txt", "r+") as f:
    data = str(f.readlines()[0])
    print("last mode = %s" % str(data))
    if data in moveModes:
        os.system("python %s" % str(data))
    else:
        f.seek(0)
        f.truncate(0)
        data = "newSAFEMODE.py"
        f.writelines(data)


args = None
keepLooping = True

def inputChecking(threadname):
    global keepLooping
    global args

    print("\nonly input direct commandline prompts or will break - i.e. don't open new windows / files\n")
    print("reboot - emergency restart")
    print("watchdog - check watchdog status")
    print("update - update and reboot the pi")
    print("exit - completely exit program to commanline")
    print("done - next mode \n")

    args = input("input:   ")
    try:
        if args == "done":
            print("safe mode complete")
            keepLooping = False
        elif args == "exit":
            os.system("pkill python")
        elif args == "reboot":
            os.system("sudo reboot now")
        elif args == "watchdog":
            os.system("sudo systemctl status watchdog")
            args = None
        elif args == "update":
            os.system("sudo apt-get update")
            os.system("sudo apt-get upgrade")
            os.system("sudo reboot now")
        else:
            print("not planned command, so running")
            os.system(args)
            args = None
    except:
        print("Command failed")
        args = None




while keepLooping:
    print("SAFE MODE HAS BEEN ACTIVATED\n")
    try:
        _thread.start_new_thread( inputChecking, ("UI",) )
        while args==None:
            pass;
    except:
        print("Thread error")


#Previous Safe Mode
#while True:
#    print ("SAFE MODE HAS BEEN ACTIVATED")
#
#    time.sleep(5)
#    break
