import os
import time
import threading

# Define the directory to store housekeeping data
housekeeping_directory = "/path/to/HOUSEKEEPINGFOLDER/"

def save_to_housekeeping_file(data):
    os.makedirs(housekeeping_directory, exist_ok=True)
    file_path = os.path.join(housekeeping_directory, "housekeeping.csv")
    with open(file_path, "a") as f:
        f.write(data)
        f.write("\n")
    print(data)

# Housekeeping data function
def housekeeping_data(data):
    save_to_housekeeping_file(data)

# Your existing functions for other data types (e.g., sensor data, spectro data)...

# Example usage of housekeeping data function
housekeeping_data("Housekeeping data entry 1")
housekeeping_data("Housekeeping data entry 2")

# The rest of your code...

# Thread creation and execution...