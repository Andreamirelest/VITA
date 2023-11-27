

#THE FOLLOWING CODE WILL SERVE THE PURPOSE OF CHOOSING BETWEEN OPTIONS OF OPENING MERGED_CODE.py and Stepper motor code

import subprocess 


def main():
 print("WELCOME! SELECT AN OPTION:")
 print("1. Run MERGED_CODE.py")
 print("2. Run Stepper_motor_code.py")

 choice = input("Enter your choice (1/2):")
  

#options given here

 if choice == "1":
 run_file("MERGED_CODE.py")
 elif choice == "2":
 run_file("Stepper_motor_code.py") 
 else 
 print("THERE IS NO SUCH A FILE")

 

 #defining what run_file command will do
 
 def run_file(MERGED_CODE.py)
 try:
 subprocess.run(["python3",MERGED_CODE.py],check=True)
  

 def run_file(Stepper_motor_code.py)
 try:
 subprocess.run(["python3",Stepper_motor_code.py],check=True)

 if__name__ == "__main__":
 main()


