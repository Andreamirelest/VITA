
#THE FOLLOWING CODE SERVES THE PURPOSE OF CONTROLLING THERMAL SENSORS
#THIS CODE WAS ORIGINALLY WRITTEN BY  THOMAS COMBE AND COPIED BY ANDREA MIRELES TAVAREZ

import threading 
import numpy as np 
import smbus
 
#TARGET TEMPERATURES
SetPoint = [25.0]

#Gains for PID loops
Kp = [1]  #Proportional gains
Ki = [1]  #Integral gains 
Kd = [1]  #Derivative gains

#Temporary variables 

deriv = 0                           #Change since last measurement (derivative) error = 0                           #Difference between the target temperature (proportional)
prev  = [0]                #Previous value for each PID loop
integral = [0]             #integral for each PID loop                 
intMin = 0                          #minimum integral value (set to zero to avoid windup)
intMax = 20                         #maximum integral value
Temp = [5]                 #current temperature for each PID loop
Duty = np.array([0], dtype=np.uint8)     #Dutycycle values (0-255)
Time = 0                            #elapse time in seconds 
LoopUpdate = [0]           #set to 1 when a target temperature has been updated 
                
               
HeaterAdresses= [0x01]
TempSensorAdresses= [0x18]
 
bus =smbus.SMBus(1)
 
#only let one thread edit the shared variables at any given time. The rest wait 
shared_lock = threading.Lock()
 
def pid_thread_function(shared_data, event):
    while not event.wait(1): #run code once a second 
        with shared_data['lock']:    #get access to the shared variables 
 
#read temperatures from sensors 
           for i in range(1) :
               tempRawHigh=bus.read_byte_data(TempSensorAdresses[i],0x05)
               tempRawLow=bus.read_byte_data(TempSensorAdresses[i],0x06)
   

               tempRawHigh=tempRawHigh  &  0x1F
          
               if (tempRawHigh  &  0x10)  == 0x10:
                   tempRawHigh   &=  0x0F
                   tempC  =  65536  -  ((tempRawHigh<<6) | (tempRawLow>>2)) 
               else:
                   tempC = (( tempRawHigh<<6) | (tempRawLow>>2))/4

               Temp[i]=tempC

           for i in range(1):
 
               if SetPoint[i] ==0:   #if set point is zero then switch the heater off and skip to the end
                   Duty[i]=0          #set the duty cycle to zero for that loop


               else:
                   error = SetPoint[i] - Temp[i]   #calculate the error 
                   integralTest = integral[i] + error #calculate the integral

                   if integralTest > intMax: #apply upper limit to inetgral
                       integral[i] = intMax 
 

                   elif integralTest < intMin:  #apply lower limit to integral 
                       integral[i] = intMin

                   else:
                       integral[i]  += error      #add the error to the integral

                   deriv = error - prev[i]        #calculate the derivative 
                   prev[i] = error                #copy the current error into prev (ready for next iteration)
             
                   duty_value = Kp[i] * error + Ki[i] * integral[i] + Kd[i]  * deriv #apply gains and sum up PID terms
  
                   clamped_duty  = max(0,min(255,  int(duty_value)))     #limit the duty cycle value to 8-bit
                   Duty[i] = np.uint8(clamped_duty)


         #write duty cycle bytes to each of the heater controllers 
           for i in range(1):
               bus.write_byte(HeaterAdresses[i],Duty[i])

           with open("Temp log", 'a') as file:                            #open text file named "temp log" 
             #write the temperatures and the time variables to the text file 
               file.write("Time:" f"{shared_data['Time']}\n")
              # file.write(f"3={Temp[3]:05.2f}\n")
              # file.write(f"2={Temp[2]:05.2f}\n")
              # file.write(f"1={Temp[1]:05.2f}\n")
               file.write(f"0={Temp[0]:05.2f}\n")

         #check if any loop has been updated 
               for i in range(1):
                   if shared_data['LoopUpdate'][i] == 1:      #if it has, then note it in the text file
                       file.write(f"Loop number{i} has been updated\n")
                       shared_data['LoopUpdate'][i] = 0 #reset the 'LoopUpdate' bit 


           shared_data['Time']  += 1 #increment the time (seconds) counter

 #these are the variables shared between the PID thread and the user input thread
shared_data = {
    'lock': shared_lock,
    'SetPoint': SetPoint,
    'Kp': Kp,
    'Ki': Ki,
    'Kd': Kd,
    'Time': Time,
    'LoopUpdate': LoopUpdate
}

#Create an event to signal the PID thread
pid_event = threading.Event()

#create PID thread
pid_thread = threading.Thread(target=pid_thread_function, args=(shared_data, pid_event))
#set it to the end when the main (user input) thread ends 
pid_thread.daemon = True 
#start the thread
pid_thread.start()

 #this thread prompts the user to enter gain values. The values are limited from 0 to 1000
def get_gain_values(shared_data, gain_type):
    print("Enter values for:")
    for i in range(1): 
        while True:
            try:
                gainInput = float(input(f"{gain_type}[{i}]: "))
                if 0 <= gainInput <= 1000:
                    shared_data[gain_type][i] =gainInput
                    break  #Exit the loop if input is valid 
                else:
                    print("Input out of range. Please enter a value between 0 and 100.")
            except ValueError:
                 print ("Invalid input. Please enter a valid number.")
          #return when valid values have been entered 

 #this thread interacts with the user, allowing them to edit the temperatures and the gains (on startup)
try:
    with  shared_data['lock']:        #lock the variables so the PID loop does not start yet

        #on boot, print the gain values, which will be set to default 
        print("Kp:", shared_data['Kp'])
        print("Ki:", shared_data['Ki'])
        print("Kd:", shared_data['Kd'])

        #ask the user if they want to edit this values
        user_input = input("Do you want to input gain values: Enter 'Y' for 'yes':")

        #if user enters 'y' then prompt then make them enter values for all the gains 
        if(user_input.lower()=="y"):

            get_gain_values(shared_data,  'Kp')  #enter proportional gain

            get_gain_values(shared_data,  'Ki')  #enter integral gain

            get_gain_values(shared_data,  'Kd')  #enter derivative gain


            #print the new gain values
            print("Kp:", shared_data['Kp'])
            print("Ki:", shared_data['Ki'])
            print("Kd:", shared_data['Kd'])



        #open the 'temp log'and note that a new session has started,then close it
        with open ("Temp log", 'a') as file:
            file.write("New session started\n")

        #this section loops constantly so that the user can change the target temperatures at the console 
    while True:
           
        print ("Current Time:", shared_data['Time'])   #print the time in seconds
        print ("setPoint:", shared_data['SetPoint'])  #print the current target temperatures


     #prompt the user to enter what loop they want to edit 
        while True:
            try:
                i = int(input("Enter loop number (0-3): "))         #input must be 0-3 three, to select one of the four loops 
                if 0  <=  i  <=  3:
                    break
                else:
                    print("Loop number must be between 0 and 3.")
            except ValueError:
                print("Invalid input.Please enter a valid loop number.")

           #prompt user to edit the new target temperature for that loop
        while True:
            try:
                setPoint_input =  float(input("Enter value for SetPoint (0-100): "))              #target temperature must be within 0-100 degrees C

                if 0<= setPoint_input  <= 100:
                    break
                else:
                    print("SetPoint value must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid SetPoint value.")



             #overwrite the old target temperature and set a bit in 'loopUpdate' to show which loop was updated 
        with  shared_data['lock']:
            shared_data['LoopUpdate'][i] = 1 
            shared_data['SetPoint'][i] = setPoint_input


except KeyboardInterrupt:
    print("Console error")
    pid_event.set()        #Signal the PID threat to exit 







