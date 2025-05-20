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
    else:
        print(f"Teacher not found!")




def add_teachers():
    name = input("Enter the teacher's name: ")
    try:
        teacher = Teacher.create(name)
        print(f"Yay! You created {teacher}!")

    except Exception as exc:
        print("Error created teacher", exc)


def add_students(teacher):
    name = input("Enter the student's name: ")

## Error creating student:  teacher_id must reference a teacher in the database
# def add_students(teacher.id=None):
#     name = input("Enter the student's name: ")
#     student = Student.create(name, (teacher.id))
#     print(f'Success: {student}')



# # WORKING!!!!!!!!!!!!!!!!!!!!!!!!!!
# def add_students():
#     choice = input("Enter the number of the teacher: ")

#     teachers = Teacher.get_all()
#     teacher = teachers[int(choice)-1]
#     name = input("\nPlease enter student name: ")
#     try:
#         Student.create(name, teacher.id)
#         print("\Student succesfully added")
#     except Exception as exc:
#         print("\nError creating new student", exc)
         


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


# working
def delete_teachers():
    choice = input("Enter the number of the teacher you want to delete: ")
    teachers = Teacher.get_all()
    if teacher := teachers[int(choice) - 1]:
        try:
            teacher.delete()
            print(f"Teacher {int(choice)} successfully deleted.")
        except Exception as exc:
                print(f"Error finding teacher:", exc)
    else:
        print(f"Teacher {int(choice)} not found.")




