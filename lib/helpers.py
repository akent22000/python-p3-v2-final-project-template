from models.teacher import Teacher
from models.student import Student


def exit_program():
    print("Goodbye!")
    exit()

def list_teachers():
    teachers = Teacher.get_all()
    for teacher in teachers:
        print(teacher)


def find_teacher_by_name():
    name = input("Enter the teacher's name: ")
    teacher = Teacher.find_by_name(name)
    print(teacher) if teacher else print(
        f'Teacher {name} not found')


def find_teacher_by_id():
    #use a trailing underscore not to override the built-in id function
    id_ = input("Enter the teacher's id: ")
    teacher = Teacher.find_by_id(id_)
    print(teacher) if teacher else print(f'Teacher {id_} not found')


def create_teacher():
    name = input("Enter the teacher's name: ")
    try:
        teacher = Teacher.create(name)
        print(f'Success: {teacher}')
    except Exception as exc:
        print("Error creating teacher: ", exc)


def update_teacher():
    id_ = input("Enter the teacher's id: ")
    if teacher := Teacher.find_by_id(id_):
        try:
            name = input("Enter the teacher's new name: ")
            teacher.name = name


            teacher.update()
            print(f'Success: {teacher}')
        except Exception as exc:
            print("Error updating teacher: ", exc)
    else:
        print(f'Teacher {id_} not found')


def delete_teacher():
    id_ = input("Enter the teacher's id: ")
    if teacher := Teacher.find_by_id(id_):
        teacher.delete()
        print(f'Teacher {id_} deleted')
    else:
        print(f'Teacher {id_} not found')


# You'll implement the student functions in the lab

def list_students():
    student = Student.get_all()
    for student in student:
        print(student)


def find_student_by_name():
    name = input("Enter the teacher's name: ")
    student = Student.find_by_name(name)
    print(student) if student else print(
        f'Student {name} not found')


def find_student_by_id():
    #use a trailing underscore not to override the built-in id function
    id_ = input("Enter the student's id: ")
    student = Student.find_by_id(id_)
    print(student) if student else print(f'Student {id_} not found')


def create_student():
    name = input("Enter the student's name: ")
    try:
        student = Student.create(name)
        print(f'Success: {student}')
    except Exception as exc:
        print("Error creating student: ", exc)


def update_student():
    id_ = input("Enter the student's id: ")
    if student := Student.find_by_id(id_):
        try:
            name = input("Enter the student's new name: ")
            student.name = name

            student.update()
            print(f'Success: {student}')
        except Exception as exc:
            print("Error updating student: ", exc)
    else:
        print(f'Dmployee {id_} not found')


def delete_student():
    id_ = input("Enter the teacher's id: ")
    if student := Student.find_by_id(id_):
        student.delete()
        print(f'Student {id_} deleted')
    else:
        print(f'Student {id_} not found')


def list_teacher_students():
    pass

