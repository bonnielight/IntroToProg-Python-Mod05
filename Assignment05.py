# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script (starter script)
#   Bonnie Light, 11/11/2024, Modified starter script for Assignment05
# ------------------------------------------------------------------------------------------ #

import json
import sys

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data: str = ''  # ??
file = None  # Holds a reference to an opened file.
student_data: dict = {}  # dictionary with one row of student data
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

#csv_data: str = ''  # Holds combined string data separated by a comma. Needed??

# When the program starts, read the file data into a list of dictionary rows (table)
# Extract the data from the file with structured error handling
# Errors considered: file not found, other non-specific error
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    print(students)   # Not in criteria, just sanity check
    file.close()

except FileNotFoundError as e:
    print("Text file must exist before running this script!\n:")
    print("-- Technical Error Message--")
    print(e, e.__doc__, type(e), sep='\n')
    sys.exit()

except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')
    sys.exit()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do? ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Student's first name must contain only letters.")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Student's last name must contain only letters.")

            course_name = input("Please enter the name of the course: ")
            #if (not course_name.isalnum() and not " " in course_name):   #must not contain a symbol, except a ' ' is allowed
            if not course_name.replace(" ", "").isalnum():
                raise ValueError("Course name must contain only letters, numbers, or a space.")

            student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message --")
            print(e.__doc__)
            print(e.__str__)
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')

        continue

   # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student["FirstName"]} {student["LastName"]} is \
enrolled in {student["CourseName"]}\n")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            #students = 5
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("Data has been written to file.")
            continue
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4!")

print("Program Ended")

#Questions
#does json file all one line?
#how to test the file write (I don't know how to break it!)
#the try:except: for the file read kills the program
#course_name symbols