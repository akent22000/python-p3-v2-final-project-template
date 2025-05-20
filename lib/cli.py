# lib/cli.py

from helpers import (
    exit_program,
    list_teachers,
    add_teachers,
    add_students,
    delete_teachers,
    list_teacher_students,
    fancy_menu,
)


def teacher():
    choice = ""
    while choice.lower != "e":
        print("\nWelcome to the Wonder School!")
        fancy_menu()      
        print("\nPlease enter E to exit or")
        print("Please enter T to see a list of teachers")
        
        choice = input("> ")
        if choice.lower == "E" or choice == "e":
            exit_program()
        elif choice == "T" or choice == "t":
            list_teachers()
            teacher_details_sub()
    exit_program()

def teacher_details_sub():
    choice = ""
    while choice.lower != "e":
        fancy_menu()      
        print("\nEnter S to see a teacher's details")
        print("A to add a teacher")
        print("D to delete a teacher")
        print("B to go back")
        print("\nOr E to exit")
        fancy_menu()      

        choice = input("> ")
        if choice.lower == "E" or choice == "e":
            exit_program()
        elif choice == "S" or choice == "s":
            list_teacher_students()
            student_details_sub()
        elif choice == "A" or choice == "a":
            add_teachers()
        elif choice == "D" or choice == "d":
            delete_teachers()
        elif choice == "B" or choice == "b":
            teacher()
    exit_program()

def student_details_sub():
    choice = ""
    while choice.lower != "e":
        print("\nEnter A to add a student")
        print("B to go back")
        print("\nOr E to exit")

        choice = input("> ")
        if choice.lower == "E" or choice == "e":
            exit_program()
        elif choice == "A" or choice == "a":
            add_students()
        elif choice == "B" or choice == "b":
            teacher()
    exit_program()


def menu():
    print("E. Exit the program")


if __name__ == "__main__":
    teacher()
