# Reading files in Python (text, JSON, CSV)


import json  # importing the json module to work with JSON data
import csv  # importing the csv module to work with CSV files


# Reading from a text file
text_file_path = "C:/Users/HP PC/Desktop/pets.txt"  # specifying the path to the file

with open(file = text_file_path, mode = 'r') as text_file:
    content = text_file.read()  # reading the entire content of the file
    print(content)


# Reading from a JSON file
json_file_path = "C:/Users/HP PC/Desktop/pets.json"  # specifying the path to the JSON file

with open(file = json_file_path, mode = 'r') as json_file:
    content = json.load(json_file)  # loading the JSON data from the file into a Python dictionary
    print(content) 


print()  # adding a blank line for better readability of the output


# Reading from a CSV file
csv_file_path = "C:/Users/HP PC/Desktop/pets.csv"  # specifying the path to the CSV file

with open(file = csv_file_path, mode = 'r') as csv_file:
    content = csv.reader(csv_file)  # creating a CSV reader object to read the CSV file
    for row in content:
        print(row)  # printing each row of the CSV file as a list
