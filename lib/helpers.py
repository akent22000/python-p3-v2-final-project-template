# lib/helpers.py
from models.teacher import Teacher
# from models.student import Student

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_teachers():
    # teacher = Teacher.get_all(__name__)
    # for i in teacher:
    #     print(i)
    #     # print(teacher)


    message = Teacher.get_all(Teacher.name)
    print(message)  # Output: Hello, World!