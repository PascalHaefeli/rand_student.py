import random
import sys

def is_input_valid(input_str):
    if not input_str.isnumeric():
        print("Your input needs to be a positive integer!")
        return False
    else:
        input_int = int(input_str)
    if input_int < 0:
        print("Your input needs to be a positive integer!")
        return False
    elif input_int != float(input_str):
        print("Your input needs to be a positive integer!")
        return False
    else:
        return True

#call the script with the '-h' flag or without any additional arguments
def manual():
    print_separator()
    print("Welcome to rand_student.py!")
    print("This script relies on a file named 'students.txt' as a pool from which to pick a random student.")
    print("You can later remove students you already picked to prevent them from being picked again until you reset the pool.")
    print("This accelerates the process of picking students during your seminars.")
    print("You can select which function to execute by passing the following flags and arguments when calling this script:")
    print_separator()
    print("'-cr' and a positive integer to generate a new list of students with the specified amount of students in your class unless")
    print("a file named 'students.txt' already exists.")
    print("e.g: python3 rand_student.py -cr 20")
    print_separator()
    print("'-rs' and a positive integer to generate a new list of students with the specified amount of students in your class;")
    print("overwrites existing files named 'students.txt' in this directory, if present.")
    print("e.g: python3 rand_student.py -rs 20")
    print_separator()
    print("'-g' to get a random student's number from students.txt")
    print("e.g: python3 rand_student.py -g")
    print_separator()
    print("'-rm' and the number(s) of one or more students to remove from the pool (their numbers must be separated by spaces)")
    print("e.g: python3 rand_student.py -rm 4, 5, 6")
    print_separator()
    print("'-a' and the number(s) of one or more students to add to the pool (their numbers must be separated by spaces)")
    print("e.g: python3 rand_student.py -a 21, 22, 23")
    print_separator()
    print("To open this manual again, just call this script without providing any additional arguments or with the '-h' flag.")
    print("If this is the first time you execute this script, you should create a pool with -cr to get started.")
    print_separator()

#call the script with the '-cr' flag and an int as your last argument
def create_pool(n_students):
    if is_input_valid(n_students):
        with open("students.txt", "x", encoding = "utf-8") as file:
            for index in range (1, int(n_students) + 1):
                file.write(f"{index}\n")
        print(f"File for {n_students} students successfully created!")
    else:
        create_pool(input("Please input the amount of students in your class: "))
        return

#call the script with the '-rs' flag and an int as your last argument
def reset_pool(n_students):
    if is_input_valid(n_students):
        print("Are you sure you want to reset students.txt?")
        answer = input("y/n    ")
        if answer == "y":
            with open("students.txt", "w", encoding = "utf-8") as file:
                for index in range (1, int(n_students) + 1):
                    file.write(f"{index}\n")
            print(f"File was reset and now contains {n_students} students.")
        elif answer == "n":
            print("Aborting reset...")
        else:
            print("Invalid input! Please enter 'y' for 'yes' or 'n' for 'no'!")
            reset_pool(n_students)
        quit()
    else:
        reset_pool(input("Please input the amount of students in your class: "))
        return

#call the script with the '-g' flag
def get_student():
    with open("students.txt", "r") as file:
        if not file.read(1):
            print("Your pool is empty! Do you want to reset students.txt?")
            answer = input("y/n    ")
            if answer == "y":
                reset_pool(input("Please specify the amount of students in your class: "))
            elif answer == "n":
                print("If your pool is empty, no students can be found. Aborting process...")
                quit()
            else:
                print("Invalid input! Please enter 'y' for 'yes' or 'n' for 'no'!")
                get_student()
                return
        students = file.read()
        students = students.split()
        chosen_student = random.choice(students)
    return print(f"chosen_student: {chosen_student}")

#call the script with the '-rm' flag and an int as your last argument
def rm_student(*args):
    for arg in args:
        if not is_input_valid(arg):
            rm_student(input("Please specify the student(s) to be removed from your pool: "))
            return
    try:
        with open("students.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            #this gets all the lines in students.txt so they can be used for the next step
    except:
        print("No file named students.txt exists in this directory. Would you like to create a new file?")
        answer = input("y/n    ")
        if answer == "y":
            create_pool(input("Please specify the amount of students in your class: "))
        elif answer == "n":
            print("This script relies on students.txt to fetch random students you have not yet picked. Without the file, it won't run.")
            print("For questions about this script's functionalities, please refer to the manual with the '-h' flag or review the source code.")
        else:
            print("Invalid input! Please input 'y' for 'yes' or 'n' for 'no'!")
            rm_student(args)
    student_removed = False
    with open("students.txt", "w+", encoding="utf-8") as file:
        if not file.read(1):
            print("Your pool is empty! Do you want to reset students.txt?")
            answer = input("y/n    ")
            if answer == "y":
                reset_pool(input("Please specify the amount of students in your class: "))
            elif answer == "n":
                print("If your pool is empty, no students can be found. Aborting process...")
                quit()
            else:
                print("Invalid input! Please enter 'y' for 'yes' or 'n' for 'no'!")
                get_student()
                return
        for line in lines:
            #filters out all students entered as arguments and writes those who are not meant to be removed, 
            #returning a file containing all students except the ones specified for removal
            if line.strip() not in args:
                file.write(line)
            else:
                student_removed = True
    if student_removed:
        print("Student(s) removed successfully!")
    else:
        print("The specified student was not part of your pool!")
    return

#call the script with the '-a' flag and an int as your last argument
def append_student(*args):
    for arg in args:
        if not is_input_valid(arg):
            append_student(input("Please specify the students to be removed from your pool: "))
            return
    try:
        with open("students.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            #this gets all the lines in students.txt so they can be used for the next step
    except:
        print("No file named students.txt exists in this directory. Would you like to create a new file?")
        answer = input("y/n    ")
        if answer == "y":
            create_pool(input("Please specify the amount of students in your class: "))
        elif answer == "n":
            print("This script relies on students.txt to fetch random students you have not yet picked. Without the file, it won't run.")
            print("For questions about this script's functionalities, please refer to the manual with the '-h' flag or review the source code.")
            return
        else:
            print("Invalid input! Please input 'y' for 'yes' or 'n' for 'no'!")
            append_student(args)
    with open("students.txt", "a", encoding="utf-8") as file:
        for arg in args:
            if arg not in lines:
                file.write(arg + "\n")
    print("Student(s) appended successfully!")

#calls a function by your specified flag when you execute this script from the terminal
def call_function_by_argument():
    if len(sys.argv) < 2:
        manual()
        return
    elif sys.argv[1] == "-h":
        manual()
        return
    elif sys.argv[1] == "-cr":
        create_pool(sys.argv[2])
        return
    elif sys.argv[1] == "-rs":
        reset_pool(sys.argv[2])
        return
    elif sys.argv[1] == "-rm":
        rm_student(*sys.argv[2:])
        return
    elif sys.argv[1] == "-g":
        get_student()
        return
    elif sys.argv[1] == "-a":
        append_student(*sys.argv[2:])
    else:
        print("Your argument was not recognized. Execute this script either without arguments or with the '-h' flag to review the manual.")
        return

#just for formatting the manual; self-explanatory
def print_separator():
    print("")
    print("===========================================================================================================================")
    print("")
    return

call_function_by_argument()