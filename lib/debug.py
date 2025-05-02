#!/usr/bin/env python3
# lib/debug.py

from __init__ import CONN, CURSOR
from models.teacher import Teacher
from models.student import Student

def reset_database():
    # Student.drop_table()
    Teacher.drop_table()
    Teacher.create_table()
    # Student.create_table()

    # Create seed data
    Teacher.create("Anne")
    Teacher.create("Sam")
    Student.create("Amir", "Accountant")
    Student.create("Bola", "Manager")

breakpoint()