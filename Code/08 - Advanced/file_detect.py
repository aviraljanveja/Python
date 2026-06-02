# File detection in Python


import os  # importing the os module to interact with the operating system


# Checking if the file exists
file_path = "C:/Users/HP PC/Desktop/pets.txt"  # specifying the path to the file

if os.path.exists(file_path):
    print("The file exists.")
else:
    print("The file does not exist.")
