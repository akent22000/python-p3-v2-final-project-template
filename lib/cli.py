# lib/cli.py

from helpers import (
    exit_program,
    list_teachers,
    list_students,
    add_teachers,
    add_students,
    update_teachers,
    delete_teachers,
    list_teacher_students
)


def teacher():
    choice = ""
    while choice.lower != "e":
        print("Welcome to the Wonder School!")
        print("**********")
        print("\nPlease enter E to exit or")
        print("Please enter T to see a list of teachers")
        print("\n**********")
        choice = input("> ")
        if choice.lower == "E" or choice == "e":
            exit_program()
        elif choice == "T" or choice == "t":
            list_teachers()
            details_sub()
        elif choice.lower != "E" or choice !="e":
            print("invaild")
    exit_program()

def details_sub():
        print("\nEnter E to exit or")
        print("\nS to see a teacher's details")
        print("A to add a teacher")
        print("U to update a teacher")
        print("D to delete a teacher")
        print("B to go back")
        choice = input("> ")
        if choice.lower == "E" or choice == "e":
            exit_program()
        elif choice == "S" or choice == "s":
            list_teacher_students()
            add_students()
        elif choice == "A" or choice == "a":
            add_teachers()
        elif choice == "U" or choice == "u":
            update_teachers()
        elif choice == "D" or choice == "d":
            delete_teachers()
        elif choice == "B" or choice == "b":
            teacher()
        elif choice.lower != "E" or choice !="e":
            exit_program()





def fancy_menu():
    print("**********")

def menu():
    print("E. Exit the program")


if __name__ == "__main__":
    teacher()
