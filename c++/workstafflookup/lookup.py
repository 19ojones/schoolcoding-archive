# Welcome message to welcome the user
print("Welcome to the department lookup program.")

# Importing the necessary library
import csv

# Ask the user whom they would like to look up
userq = input("Who would you like to look up? (e.g. John Smith): ")

# Open the .csv file and read the contents
file_path = 'u:\Desktop\Department Lookup\example.csv'
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Check if the first column (assuming it contains names) matches the user's query
        if row[0].lower() == userq.lower():
            department = row[1]  # Assuming the department is in the second column
            print(f"The department for {userq} is {department}.")
            break  # Exit the loop if a match is found

    else:
        print(f"Sorry, the department information for {userq} could not be found.")
