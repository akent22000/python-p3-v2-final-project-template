from models.teacher import Teacher
from models.student import Student


def exit_program():
    print("Goodbye!")
    exit()

def fancy_menu():
     print("*********************************")


# working
def list_teachers():
    teachers = Teacher.get_all()
    for i, teacher in enumerate(teachers, start=1):
    		print(f"{i}. {teacher.name}")
              

# working
def list_students():
    students = Student.get_all()
    for i, student in enumerate(students, start=1):
    		print(f"{i}. {student.name}")              


# working
def list_teacher_students():
    choice = input("Enter the number of the teacher to see their students: ")
    teachers = Teacher.get_all()
    if teacher := teachers[int(choice) - 1]:

        students = teacher.students()

        if students:
            print(f"Students in {teacher.name} class :")
            for i, student in enumerate(students, start=1):
                print(f"{i}. {student.name}")
        else:
            print(f"No students found in {teacher.name}'s class.")
    
        return teacher
    else:
        print(f"Teacher not found!")


# working
def add_teachers():
    name = input("Enter the teacher's name: ")
    try:
        teacher = Teacher.create(name)
        print(f"Yay! You created {teacher}!")

    except Exception as exc:
        print("Error created teacher", exc)

# working
def add_students(teacher):
    name = input("Enter the student's name: ")
    try:
        student = Student.create(name, teacher.id)
        print(f"Yay! You created {student}!")

    except Exception as exc:
        print("Error created student", exc)



# working
def delete_teachers():
    choice = input("Enter the number of the teacher delete: ")
    teachers = Teacher.get_all()
    if teacher := teachers[int(choice) - 1]:
        students = teacher.students()
        if students:
            for student in students:
              student.delete()
              teacher.delete()
        else:
            print(f"No students found in {teacher.name}'s class.")
    else:
        print(f"Teacher not found!")


def delete_students():
    choice = input("Enter the number of the student you want to delete: ")
    students = Student.get_all()
    if student := students[int(choice) - 1]:
        try:
            student.delete()
            print(f"Student {int(choice)} successfully deleted.")
        except Exception as exc:
                print(f"Error finding student:", exc)
    else:
        print(f"Student {int(choice)} not found.")


# working
def update_teachers():
    choice = input("Enter the number of the teacher you want to update: ")
    teachers = Teacher.get_all()
    if teacher := teachers[int(choice) - 1]:
        try:
            name = input("Enter teacher's new name: ")
            teacher.name = name
            teacher.update()
            print(f"Teacher {int(choice)} successfully updated.")
        except Exception as exc:
                print(f"Error finding teacher:", exc)
    else:
        print(f"Teacher {int(choice)} not found.")
