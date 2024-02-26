import sys
import os
import time  
import signal


modeIndex = 0

#for dealing with post rehydration mode timeout
#automatically starts science mode
def interupted(signum, frame):
    modeIndex += 1
    
signal.signal(signal.SIGALRM, interupted)

#define the list of codes 

code_files = ["STANDBYMODE.py","REHYDRATIONMODE.py","SCIENCEMODE.py","DECOMMISSIONMODE.py"]


def run_code(filename):
    global modeIndex

    try:
        os.system(f"python {filename}")
        return True 
    except Exception as e:
        print(f"An error has occured in {filename}: {e}")
        return False 


def main():
    global modeIndex
    
    rehydrateTimeout = 5 #Seconds allowed after rehydration mode finnishing before automatically moving to science mode.    
    
    programs = ["SAFEMODE.py", "STANDBYMODE.py", "REHYDRATIONMODE.py", "SCIENCEMODE.py", "DECOMMISSIONMODE.py"]

    if run_code("BOOTLOADER.py"):
        print("Bootloader process successful")
    input("Press enter to start\n")
    print("Safe mode will start as default")
    
    while True:
        if run_code(str(programs[modeIndex])):
            if modeIndex == 2:
                signal.alarm(rehydrateTimeout)
                try:
                    choice = input ("REHYDRATION HAS BEEN SUCCESFUL!  WOULD YOU LIKE TO CONTINUE TO SCIENCE MODE? (yes/no):").lower()
                    if choice == "yes":
                        modeIndex += 1
                    else:
                        while True:
                            code_choice = input("Which mode would you like to continue to ? (SAFE/STANDBY/REHYDRATION/SCIENCE/DECOMMISION):").upper()
                            if code_choice in ["SAFE","STANDBY","REHYDRATION","SCIENCE","DECOMMISSION" ]:
                                modeIndex  = ["SAFE","STANDBY","REHYDRATION","SCIENCE","DECOMMISSION" ].index(code_choice)

                                break

                except:
                    print("in except")
                    choice = "yes"

                #turn off alarm timer
                signal.alarm(0)

                if choice == "yes":
                    modeIndex += 1
                else:
                    while True:
                        code_choice = input("Which mode would you like to continue to ? (SAFE/STANDBY/REHYDRATION/SCIENCE/DECOMMISION):").upper()
                        if code_choice in ["SAFE","STANDBY","REHYDRATION","SCIENCE","DECOMMISSION" ]:
                            modeIndex  = ["SAFE","STANDBY","REHYDRATION","SCIENCE","DECOMMISSION" ].index(code_choice)

                            break



            else:
                choice = input ("%s HAS BEEN SUCCESFUL!  WOULD YOU LIKE TO CONTINUE TO %s? (yes/no):" % (str(programs[modeIndex]), str(programs[modeIndex + 1]))).lower()

                if choice == "yes":
                    modeIndex += 1
                else:
                    while True:
                        code_choice = input("Which mode would you like to continue to ? (SAFE/STANDBY/REHYDRATION/SCIENCE/DECOMMISION):").upper()
                        if code_choice in ["SAFE","STANDBY","REHYDRATION","SCIENCE","DECOMMISSION" ]:
                            modeIndex  = ["SAFE","STANDBY","REHYDRATION","SCIENCE","DECOMMISSION" ].index(code_choice)
                            #run_code(f"{code_choice.upper()}MODE.py")
                            break



def main1():
    while True:
        if run_code("BOOTLOADER.py"):
            print("bootloader successful")
        input("Press enter to start\n")
        print("Safe Mode will start as default mode")

        if run_code("SAFEMODE.py"):
            choice = input("SAFE MODE HAS BEEN COMPLETED! WOULD YOU LIKE TO CONTINUE TO STANDBY MODE? (yes/no):").lower()


        if choice == "yes":
          # for code_file in code_files:
            if not run_code("STANDBYMODE.py"):
                print ("Error occurred in STANDBYMODE.py  . SAFE MODE WILL START AS DEFAULT MODE.") 
                run_code ("SAFEMODE.py")

            choice = input ("STANDBYMODE HAS BEEN SUCCESFUL! WOULD YOU LIKE TO CONTINUE TO REHYDRATION MODE? (yes/no):").lower()

        if choice == "yes":
           run_code("REHYDRATIONMODE.py")
       # elif choice == "sos"
           #run_code("SAFEMODE.py")
           signal.alarm(rehydrateTimeout)
           try:
               choice = input ("REHYDRATION HAS BEEN SUCCESFUL! WOULD YOU LIKE TO CONTINUE TO SCIENCE MODE? (yes/no):").lower()
           except:
               print("in except")
               choice = "yes"
           print("out of except")
           signal.alarm(0)
           print ("alarm off")
        if choice == "yes":
           print("starting mode")
           run_code("SCIENCEMODE.py")
           choice = input ("SCIENCE MODE HAS BEEN COMPLETED SUCCESFULLY! WOULD YOU LIKE TO CONTINUE TO DECOMMISSION MODE? (yes/no):").lower()
        if choice == "yes":
           run_code("DECOMMISSIONMODE.py")

           print ("ALL MODES HAVE BEEN SUCCESFUL!")

        elif choice =="no":
            while True:
                code_choice = input("Which mode would you like to continue to ? (SAFE/STANDBY/REHYDRATION/SCIENCE/DECOMMISION):").upper()
               # if code_choice in [f"{mode}MODE" for mode in ["STANDBY" , "REHYDRATION", "SCIENCE", "DECOMMISSION"]]:
               #     run_code(f"{code_choice.upper()}.py")

                if code_choice in ["SAFE","STANDBY","REHYDRATION","SCIENCE","DECOMMISSION" ]:
                    run_code(f"{code_choice.upper()}MODE.py")
            break


if __name__ == "__main__":
    main()


