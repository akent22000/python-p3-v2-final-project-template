# lib/cli.py

from helpers import (
    exit_program,
    list_teachers,
    list_students,
    create_teacher,
    create_student,
    find_teacher_by_id,
    list_teacher_students,
    update_teacher
)


list_teachers()
find_teacher_by_id()

def find_teacher_by_id():
    while True:
        menu()

        choice = input("> ")
        if choice == "E":
            exit_program()
        elif choice == "U":
            update_teacher()
        else:
            print("Invalid choice")



def menu():
    print("Please select an option:")
    print("E. Exit the program")
    print("U. Update teacher")
#     print("2. Add student")



if __name__ == "__main__":
    find_teacher_by_id()
