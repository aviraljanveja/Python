# Writing to Files in Python (text, JSON, CSV)


import os  # importing the os module to interact with the operating system
import json  # importing the json module to work with JSON data
import csv  # importing the csv module to work with CSV files


# Writing to a text file
text_file_path = "C:/Users/HP PC/Desktop/pets.txt"  # specifying the path to the file
pets = ["misty", "leo", "junior", "brownie"]  # creating a list of pets to write to the text file

# The with statement is a convenient way to handle file operations. 
# It ensures that the file is properly closed after operation, even if an exception is raised at some point.
# This means that you don't have to worry about closing the file manually, which can help prevent bugs and resource leaks.
with open(file = text_file_path, mode = 'w') as file:
    # The open() function is used to open a file. It takes two arguments: the file path and the mode in which to open the file.
    # It returns a file object, which is used to perform operations on the file.
    # The mode 'w' stands for write mode, which means that the file will be created if it does not exist, and if it does exist, it will be overwritten.
    # The 'as' keyword is used to assign the file object to the variable 'file', which can be used to perform operations on the file within the block of code.
    
    for pet in pets:
        file.write(pet + "\n")  # writing each pet's name to the file
    print("Data written to the text file successfully.")
# There is also a mode 'a' for append mode, which allows you to add content to the end of the file without overwriting it.
# There is also a mode 'x' for creating a new file, it will create a new file but will raise an error if the file already exists.


# Writing to a JSON file
# JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate.
# It is basically a way to represent data in a structured format using key-value pairs, similar to a Python dictionary.
json_file_path = "C:/Users/HP PC/Desktop/pets.json"  # specifying the path to the JSON file
pets_json = {  # creating a dictionary to represent the pets data in JSON format
    "pet1": "misty",
    "pet2": "leo",
    "pet3": "junior",
    "pet4": "brownie"
}

with open(file = json_file_path, mode = 'w') as json_file:
    json.dump(pets_json, json_file, indent=4)  # writing the dictionary to the JSON file
    print("Data written to the JSON file successfully.")


# Writing to a CSV file
# CSV (Comma-Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database.
csv_file_path = "C:/Users/HP PC/Desktop/pets.csv"  # specifying the path to the CSV file
pets_csv = [  # creating a list of lists to represent the pets data in CSV format
    ["pet1 ", " misty"],
    ["pet2 ", " leo"],
    ["pet3 ", " junior"],
    ["pet4 ", " brownie"]
]

with open(file = csv_file_path, mode = 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for row in pets_csv:
        writer.writerow(row)
    print("Data written to the CSV file successfully.")
