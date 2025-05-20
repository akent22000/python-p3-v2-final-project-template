# School CLI


## Introduction

This project assists schools in managing the databases of teachers and students. Functionality within the Command-Line Interface menu includes:
-listing all teachers,
-listing all students within a teacher's classroom,
-adding and removing teachers
-adding, removing students

---

## Installation and Usage

1. After you've forked and cloned this repo to your local environment, 
open the project and run to install the required dependencies

    pipenv install then
    pipenv shell


2.  run the application

    python cli.py


3.  Choose from the main menu
    When the application starts, you’ll see the main menu:

    Welcome to the Wonder School!

        1. Please enter T to see a list of teachers
        2. Exit

    1. Please enter T to see a list of teachers - select this to display a list of teachers.
    2. Exit - select this to exit the program.

    If you selected T the following menu is displayed:

        1. Enter S to see a teacher's details
        2. A to add a teacher
        3. U to update a teacher
        4. D to delete a teacher
        5. B to go back to the previous menu
        6. E to exit the program

    1. S - select this to see a list of the teacher's students.
    2. A - select to add a new teacher, you will be prompted to enter the teacher's name.
    3. U - select this to update a teacher, you will be prompted to enter the number of the teacher you want to update from the list, then you will be prompted to enter a new teacher name.
    3. D - select this to delete a teacher, you will be prompted to enter the number of the teacher you want to remove from the list.
    5. B - select this to return to the previous menu.
    6. E - select this to exit the program.

    If you selected S the following menu is displayed:

        1. A to add a student
        2. B to go back to the previous menu
        3. E to exit the program

    1. A - select to add a new student, you will be prompted to enter the student's name.
    3. D - select this to delete a student, you will be prompted to enter the number of the student you want to remove from the list.
    5. B - select this to return to the previous menu.
    6. E - select this to exit the program.






---

