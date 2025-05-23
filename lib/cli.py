# lib/cli.py

from helpers import (
    exit_program,
    list_teachers,
    add_teachers,
    add_students,
    update_teachers,
    delete_teachers,
    delete_students,
    list_teacher_students,
    fancy_menu,
)


def main_menu():
    choice = ""
    while choice.lower != "e":
        print("\nWelcome to the Wonder School!")
        fancy_menu()      
        print("\nPlease enter E to exit or")
        print("Please enter T to see a list of teachers")
        fancy_menu()      
        
        choice = input("> ")
        if choice.lower == "E" or choice == "e":
            exit_program()
        elif choice == "T" or choice == "t":
            teacher_details_sub()
    exit_program()


def teacher_details_sub():
    choice = ""
    while choice.lower != "e":
        list_teachers()
        fancy_menu()      
        print("\nEnter S to see a teacher's details")
        print("A to add a teacher")
        print("U to update a teacher")
        print("D to delete a teacher")
        print("B to go back to go back to the previous menu")
        print("Or E to exit")
        fancy_menu()      

        choice = input("> ")
        if choice.lower == "E" or choice == "e":
            exit_program()
        elif choice == "S" or choice == "s":
            teacher = list_teacher_students()
            student_details_sub(teacher)
        elif choice == "A" or choice == "a":
            add_teachers()
            teacher_details_sub()
        elif choice == "U" or choice == "u":
            update_teachers()
            teacher_details_sub()
        elif choice == "D" or choice == "d":
            delete_teachers()
            teacher_details_sub()
        elif choice == "B" or choice == "b":
            main_menu()
    exit_program()


def student_details_sub(teacher):
    fancy_menu()      

    choice = ""
    while choice.lower != "e":
        print("\nEnter A to add a student")
        print("D to delete a student")
        print("B to go back to the previous menu")
        print("Or E to exit")
        fancy_menu()      

        choice = input("> ")
        if choice.lower == "E" or choice == "e":
            exit_program()
        elif choice == "A" or choice == "a":
            add_students(teacher)
        elif choice == "D" or choice == "d":
            delete_students(teacher)
        elif choice == "B" or choice == "b":
            teacher_details_sub()
    exit_program()


def menu():
    print("E. Exit the program")


if __name__ == "__main__":
    main_menu()
