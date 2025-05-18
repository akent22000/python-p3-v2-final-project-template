# lib/cli.py

from helpers import (
    exit_program,
    list_teachers,
    list_students,
    add_teachers,
    # add_students,
    update_teachers,
    delete_teachers,
    list_teacher_students
)



def teacher():
    choice = ""
    while choice.lower != "e":
        print("Welcome to the Wonder School!")
        print("**********")
        print("\nPlease enter E to exit")
        print("or")
        print("Please enter T to see a list of teachers")
        print("Please enter A to add a teacher")
        print("Please enter U to update a teacher")
        print("Please enter D to delete a teacher")
        print("\n**********")
        choice = input("> ")
        if choice.lower == "E" or choice == "e":
            exit_program()
        # elif choice == "A" or choice == "a":
        #     add_teachers()
        # elif choice == "U" or choice == "u":
        #     update_teachers()
        elif choice == "T" or choice == "t":
            # list_teachers()
            list_teacher_students
        elif choice.lower != "E" or choice !="e":
            print("invaild")

    exit_program()

# def teacher_sub():
#         print("Enter E to exit")
#         print("A to add a teacher")
#         print("U to update a teacher")
#         print("D to delete a teacher")
#         list_teachers()

#         choice = input("> ")
#         if choice.lower == "E" or choice == "e":
#             exit_program()
#         elif choice == "A" or choice == "a":
#             add_teachers()
#         elif choice == "U" or choice == "u":
#             update_teachers()
#         elif choice == "D" or choice == "d":
#             delete_teachers()
#         elif choice.lower != "E" or choice !="e":
#             exit_program()



# def student_sub():
#         print("Enter E to exit")
#         print("A to add a student")
#         print("D to delete a student")
#         choice = input("> ")
#         if choice.lower == "E" or choice == "e":
#             exit_program()
#         # elif choice == "A" or choice == "a":
#         #     add_students()
#         # elif choice == "D" or choice == "d":
#         #     delete_students()
#         elif choice.lower != "E" or choice !="e":
#             exit_program()


def fancy_menu():
    print("**********")

def menu():
    print("E. Exit the program")


if __name__ == "__main__":
    teacher()
