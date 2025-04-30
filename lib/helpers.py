# lib/helpers.py
from models.teacher import Teacher
# from models.student import Student

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_teachers():
    teacher = Teacher.get_all()
    for teacher in teacher:
        print(teacher)