#THE FOLLOWING  IS A CODE THAT COMBINES ALL CODES

import sys
import os

#import raspistill 
 


#define the list of codes 

code_files = ["STANDBYMODE.py","REHYDRATIONMODE.py","SCIENCEMODE.py","DECOMMISSIONMODE.py"]


def run_code(filename):
    try:
        os.system(f"python {filename}")
        return True 
    except Exception as e:
        print(f"Error running {filename}: {e}")
        return False 


def main():
    while True:
        input("Press enter to start\n")
        print("Safe Mode will start as default mode")

        if run_code("SAFEMODE.py"):
            choice = input("SAFE MODE HAS BEEN COMPLETED! WOULD YOU LIKE TO CONTINUE TO STANDBY MODE? (yes/no):").lower()
        
        


        if choice == "yes":
            for code_file in code_files:
                    run_code(code_file)



        elif choice =="no":
            while True:
                code_choice = input("Which mode would you like to continue to ? (STANDBY/REHYDRATION/SCIENCE/DECOMMISION):").upper()
                if code_choice in [ "STANDBY","REHYDRATION","SCIENCE","DECOMMISSION" ]:
                    run_code(f"{code_choice.upper()}MODE.py")      #this allows to link the choices to the code_files document 
                else:
                    print("INVALID CHOICE")

        #for code_file in code_file[index:]:
                    #    if not run_code(code_file):
                  #          break 
                break


if __name__ == "__main__":
    main()



#here how do I run codes besides safe mode 



#past code starts here 

#default code to run in safemode 

#current_code="SAFEMODE.py"

#while True:
 #   try:
#
 #       input("PRESS ENTER TO START:")
  #      os.system(f"python{current_code}")    # f" is used to create an f string which allows to create strings with dynamic (changing) content such as the changing codesfor each mode.
   #     print(f"{current_code} EXECUTED SUCCESFULLY.")
   # except Exception as e:                  #e allows to assign the exception/error to a variable 
    #    print(f" An error ocurred: {e}")
   # finally:
    #    continue_running =  input("Do you wan to continue?" (yes/no): ").lower()    #lower() allows to convert all characters in answer to lower case for the sake of simplicity and a friendly interaction
        
     #   if continue_running == "yes":
        #code will run to next code in order.
      #  index = code_files.index(current_code)
       # if index < len(code_files) -1:  #used to check if current code running is not last code of list
        #   current_code = code_files[index + 1]   #if it is true that substracting 1 there are more codes in list then more code files can run after current one.

      #  else:
       #     print("All modes have been run")       #this part will be taken away it is for the purpose of knowing when all modes have been run 
        #    break 



    #    else:
     #   user_choice =input("SELECT THE MODE YOU WOULD LIKE TO RUN  (a= SAFEMODE/ b=STANDBYMODE / c=SCIENCEMODE /d=REHYDRATIONMODE / e=DECOMMISSIONMODE):".lower())
             

        #user choice to corresponding file, linking each letter to its correspondant file
       #      if user_choice in ["a", "b", "c","d","e"]:     #check whether this is written correctly this might present an error 
       #          current_code = f"Code{user_choice.upper()}.py"}
       #      else:
        #         print("Invalid choice. Continuing with the current code.")
