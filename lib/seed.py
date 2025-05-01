from models.__init__ import CONN, CURSOR
from models.teacher import Teacher
# from models.student import Student

def seed_database():
    # Student.drop_table()
    Teacher.drop_table()
    Teacher.create_table()
    # Student.create_table()

    # Create seed data
    Teacher.create("Allen")
    Teacher.create("Anne")
    # Student.create("Amir", "Accountant", payroll.id)
    # Student.create("Bola", "Manager", payroll.id)
    # Student.create("Charlie", "Manager", human_resources.id)
    # Student.create("Dani", "Benefits Coordinator", human_resources.id)
    # Student.create("Hao", "New Hires Coordinator", human_resources.id)


seed_database()
print("Seeded database")
