

import os
import subprocess
from ALLMODES8 import main



try:
    main()
    #os.system("python 5MODES.py")

    # os.system("python 5MODES.py")
   # subprocess.run(["5MODES.py"], check = True, shell=True)
except:
    print("Error Caught !!!")
#except ArithmeticError:
#   
#    # Handle other arithmetic errors
#    print("An arithmetic error occurred.")
#except Exception as e:
#    
#    print(f"An exception of type {type(e).__name__} occurred.")
else:
    # Code to execute if no exceptions were raised
    print("No exceptions were raised.")
finally:
    # Cleanup code (always gets executed)
    print("Cleanup code.")

try:
    # Code that may raise other exceptions goes here
    value = int("abc")  # Example: ValueError
except ValueError as ve:
    # Handle ValueError
    print(f"ValueError: {ve}")

try:
    # Code that may raise IOError goes here
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except IOError as ioe:
    # Handle IOError
    print(f"IOError: {ioe}")

try:
    # Code that may raise a custom exception goes here
    raise RuntimeError("Custom error message")
except RuntimeError as re:
    # Handle custom exception
    print(f"RuntimeError: {re}")

try:
    # Code that may raise KeyboardInterrupt goes here
    input("Press Enter to simulate KeyboardInterrupt: ")
except KeyboardInterrupt:
    # Handle KeyboardInterrupt
    print("KeyboardInterrupt detected.")

try:
    # Code that may raise SystemExit goes here
    sys.exit("Exiting the program")
except SystemExit as se:
    # Handle SystemExit
    print("SystemExit detected:", se)


