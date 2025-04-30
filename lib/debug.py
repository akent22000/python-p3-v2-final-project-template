#!/usr/bin/env python3
# lib/debug.py

from __init__ import CONN, CURSOR
from models.teacher import Teacher
from models.student import Student
import ipdb

def reset_database():
    Student.drop_table()
    Teacher.drop_table()
    Teacher.create_table()
    Student.create_table()

    # Create seed data
    payroll = Teacher.create("Payroll", "Building A, 5th Floor")
    human_resources = Teacher.create(
        "Human Resources", "Building C, East Wing")
    Student.create("Amir", "Accountant", payroll.id)
    Student.create("Bola", "Manager", payroll.id)
    Student.create("Charlie", "Manager", human_resources.id)
    Student.create("Dani", "Benefits Coordinator", human_resources.id)
    Student.create("Hao", "New Hires Coordinator", human_resources.id)


reset_database()
ipdb.set_trace()
