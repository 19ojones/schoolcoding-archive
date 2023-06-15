import csv

print("Welcome to the lookup program.")

# Login System
username = str(input("Username: "))
password = str(input("Password: "))

file_path = r'u:\Desktop\Person Lookup\databases\login.csv'
with open(file_path, 'r', encoding='latin-1') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[0].lower() == username.lower() and row[1] == password:
            print("You are now logged in")
            break
    else:
        print("Invalid username or password")
        exit()
        
# Ask the user whom they would like to look up
userq = input("Who would you like to look up? (e.g. John Smith): ")

# Open the .csv file and read the contents
file_path = r'u:\Desktop\Person Lookup\databases\example.csv'
with open(file_path, 'r', encoding='latin-1') as file:
    csv_reader = csv.reader(file)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Check if the first column (assuming it contains names) matches the user's query
        if row[0].lower() == userq.lower():
            department = row[1]  # Assuming the department is in the second column
            ID = row[2]  # Assuming the ID is in the third column
            print(f"Department: {department}")
            print(f"ID: {ID}")
            print(f"This is all the known information on {userq}.")
            break
    else:
        print(f"Sorry, information for {userq} could not be found.")
