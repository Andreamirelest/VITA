#THE FOLLOWING  IS A CODE THAT COMBINES ALL CODES

import sys
import os
import time  
#import raspistill 


#def main():
 #   while True:
  #      try:
        #if code has an error automatically go to safemode
           # pass
      #  except Exception as e 
       #     print(f"Error: {e}")
        #    print("Restarting code SAFEMODE WILL BE ACTIVATED....")
         #   time.sleep(5)   #wait for 5 seconds 
          #  continue  # restart the loop and run the code 

 


#define the list of codes 

code_files = ["STANDBYMODE.py","REHYDRATIONMODE.py","SCIENCEMODE.py","DECOMMISSIONMODE.py"]


#def main():
   # while True:
    #    try:

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
           # while True:
            
           # for code_file in code_files:
            run_code("STANDBYMODE.py")

            choice = input("STANDBYMODE HAS BEEN SUCCESFUL! WOULD YOU LIKE TO CONTINUE TO REHYDRATION MODE? (yes/no):").lower()
           #if an error occurs run code SAFEMODE
        

 
        if choice == "yes":
           run_code("REHYDRATIONMODE.py")
 #IF AN ERROR OCCURS RUN SAFEMODE 

        

            choice = input("REHYDRATION HAS BEEN SUCCESFUL! WOULD YOU LIKE TO CONTINUE TO SCIENCE MODE? (yes/no):").lower()
        if choice == "yes":
            run_code("SCIENCEMODE.py")
            choice = input("SCIENCE MODE HAS BEEN COMPLETED SUCCESFULLY! WOULD YOU LIKE TO CONTINUE TO DECOMMISSION MODE? (yes/no):").lower()
        if choice == "yes":
            run_code("DECOMMISSIONMODE.py")

            print ("ALL MODES HAVE BEEN SUCCESFUL!")
                
        elif choice =="no":
            while True:
                code_choice = input("Which mode would you like to continue to ? (STANDBY/REHYDRATION/SCIENCE/DECOMMISION):").upper()
               # if code_choice in [f"{mode}MODE" for mode in ["STANDBY" , "REHYDRATION", "SCIENCE", "DECOMMISSION"]]:
               #     run_code(f"{code_choice.upper()}.py")
                    
                   
                if code_choice in ["STANDBY","REHYDRATION","SCIENCE","DECOMMISSION" ]:
                    run_code(f"{code_choice.upper()}MODE.py")


        elif 
            run_code("SAFEMODE.py")

            break    
#def main()                 
   # while True:
      # try:
                
      #this allows to link the choices to the code_files document
                  
            
 #          pass
  #     except Exception as e:
   #       print(f"Error: {e}")
    #      print("RESTARTING CODE ... SAFEMODE WILL BE ACTIVATED AUTOMATICALLY")
     #     time.sleep(5)
      #    continue 


           # while True:
            #    code_choice = input("CODE CHOSEN HAS BEEN SUCCESFUL! TO WHICH MODE WOULD YOU LIKE TO CONTINUE TO ? (REHYDRATION/SCIENCE/DECOMMISSION):").upper()
             #   if code_choice in ["REHYDRATION","SCIENCE","DECOMMISSION"]:
                  #  run_code(f"{code_choice.upper()}MODE.py")
                  # try to find a more effective solution to run code automatically after code has been run.
                  # LAST EDIT FROM HERE   
              #      run_code (f"{code_choice.upper()}MODE.py")
           # break 

            #while True:
             #   code_choice = input("CODE CHOSEN HAS BEEN SUCCESFUL! TO WHICH MODE WOULD YOU LIKE TO CONTINUE  TO? (SCIENCE/DECOMMISSION):").upper() 
              #  if code_choice in ["REHYDRATION","SCIENCE","DECOMMISSION"]: 
               #     run_code(f"{code_choice.upper()}MODE.py")

           # while True:
           #     code_choice = input("THE REMAINING MODE IS DECOMMISSION MODE WOULD YOU LIKE TO PROCEED? (YES/NO):").upper()
            #    if code_choice == "YES":
             #        run_code("DECOMMISSIONMODE.py")

              #  if code_choice == "NO":
               #     print ("SAFEMODE WILL START AS DEFAULT MODE")
                #    run_code("SAFEMODE.py")
                #else:
                 #   print("INVALID CHOICE")
                    #break

#make a loop that until invalid input ask question again 


             #run_code() 

        #for code_file in code_file[index:]:
                    #    if not run_code(code_file):
                  #          break 
               # break


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
