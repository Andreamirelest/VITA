
# THE FOLLOWING CODE WILL SERVE THE PURPOSE TO TRANSFER RESULT FILES IN CSV FORMAT TO AN OUTSIDE FOLDER. 

import os 

# import 5 modes code 


# define the path to directory where files will be saved in this case outside folder RESULTScsv

results_csv = “/path/to/RESULTSFOLDER/“

def save_to_results_file(data):

#create folder in case it does not exist 

    os.makedirs(results_csv, exist_ok=True)

#MODES FILEPATHS 

    file_path = os.path.join(results_csv, "safemode.csv")

    file_path = os.path.join(results_csv, "standby.csv")

    file_path = os.path.join(results_csv, "rehydration.csv")

    file_path = os.path.join(results_csv, "science.csv")

    file_path = os.path.join(results_csv, "decommission.csv")


    with  open (file_path, "a") as f: 
        f.write(data)
        f.write("\n")

        print(data)

 ### DEFINE SENSORS DATA TO RESULTS FOLDER 

def sensor_results_file(sensordata) : 

    os.makedirs(resukts_directory, exist_ok=True)

    file_path = os.path.join(results_directory, "standbyenvsens.csv")

    file_path = os.path.join(results_directory, "rehydrationenvsens.csv")

    file_path = os.path.join(results_directory, "scienceenvsens.csv")

    file_path = os.path.join(results_directory, "decomenvsens.csv")

    with  open (file_path, "a") as f: 
        f.write(data)
        f.write("\n")

        print(sensordata)



 #### DEFINE SPECTROMETERS DATA TO RESULTS FOLDER


 def spectro_results_file(spectrodata): 
     os.makedirs(results_directory, exist_ok=True)


     file_path = os.path.join(results_directory, "rehydrationspectro.csv")
     file_path = os.path.join(results_directory, "sciencespectro.csv")
     file_path = os.path.join(results_directory, "decomspectro.csv")

     with  open (file_path, "a") as f: 
        f.write(spectrodata)
        f.write("\n")

        print(spectrodata) 



 #### DEFINE V2 DATA TO RESULTS FOLDER 


    




