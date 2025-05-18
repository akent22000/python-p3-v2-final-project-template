from models.teacher import Teacher
from models.student import Student


def exit_program():
    print("Goodbye!")
    exit()

def list_teachers():
    teachers = Teacher.get_all()
    for i, teacher in enumerate(teachers, start=1):
    		print(f"{i}. {teacher.name}")
              

def list_students():
    students = Student.get_all()
    for i, student in enumerate(students, start=1):
    		print(f"{i}. {student.name}")              


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
    name = input("Enter the teacher's name:")
    try:
        teacher = Teacher.create(name)
        print(f"Yay! You created {teacher}!")

    except Exception as exc:
        print("Error created teacher", exc)


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



##loop through index and subtract -1
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



# def update_employee():
#     id_ = input("Enter the employee's id: ")
#     if employee := Employee.find_by_id(id_):
#         try:
#             name = input("Enter the employee's new name: ")
#             employee.name = name
#             department_id = input("Enter the employee's new department id: ")

#             if not Department.find_by_id(department_id):
#                 print(f"Department {department_id} does not exist")
#                 return

#             employee.department_id = department_id
#             title = input("Enter the employee's new job title: ")
#             employee.title = title
#             salary = input("Enter the employee's new salary: ")
#             employee.salary = salary

#             employee.update()
#             print(f'Success: {employee}')
#         except Exception as exc:
#             print("Error updating employee: ", exc)
#     else:
#         print(f'Employee {id_} not found')
