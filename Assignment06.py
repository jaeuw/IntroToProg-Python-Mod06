# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   JBarnett,03/05/2025,Modified Script
# ------------------------------------------------------------------------------------------ #
import json
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

FILE_NAME: str = "Enrollments.json"

# Define variables
#students: list = []  # a table of student data
#menu_choice: str = "" # Hold the choice made by the user.
#student_first_name: str = ''  # Holds the first name of a student entered by the user.
#student_last_name: str = ''  # Holds the last name of a student entered by the user.
#course_name: str = ''  # Holds the name of a course entered by the user.
#student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
#csv_data: str = ''
#json_data: str = ''
#file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# Processing ---------------------------------------
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    JBarnett,03/05/2025,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads data from file and converts into json
        ChangeLog: (Who, When, What)
        JBarnett,03/05/2025,Created Class
        :param student_data: list of dictionary rows
        :return: student data
        """

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", error=e)
        finally:
            if file.closed == False:
                file.close()
        return student_data


    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function writes data to Json file
        ChangeLog: (Who, When, What)
        JBarnett,03/05/2025,Created Class
        :param file_name: Json file that is written to
        :param student_data: dictionary rows
        :return: None
        """

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("the student has been registered!")
            IO.output_student_courses(student_data=student_data)
        except TypeError as e:
            IO.output_error_messages("Please check that the data is in valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()



    # Present and Process the data

class IO:
    """
    A collection of presentation layer functions that manage user input and output
    ChangeLog: (Who, When, What)
    JBarnett,03/05/2025,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays a custom error message to the user
        ChangeLog: (Who, When, What)
        JBarnett,03/05/2025,Created Class
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message --")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the menu of choices
        ChangeLog: (Who, When, What)
        JBarnett,03/05/2025,Created Class
        :return: None
        """
        print() #Adding extra space to make it look nicer
        print(menu)
        print() #Adding extra space to make it look nicer

    @staticmethod
    def input_menu_choice():
        """
        This function gets a menu choice from the user
        ChangeLog: (Who, When, What)
        JBarnett,03/05/2025,Created Class
        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):
                raise Exception("Please, choose only 1,2,3,4")
        except Exception as e:
            IO_output_error_messages(e.__str__())
        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function displays current student data
        ChangeLog: (Who, When, What)
        JBarnett,03/05/2025,Created Class
        :return: registration list
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function requests the students first name, last name and registered course
        ChangeLog: (Who, When, What)
        JBarnett,03/05/2025,Created Class
        :return: student_data
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the incorrect type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# End of Class Function Definitions

students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while (True):

    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
