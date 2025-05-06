# lib/models/student.py
from models.__init__ import CURSOR, CONN
from models.teacher import Teacher

class Student:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, teacher_id, id=None):
        self.id = id
        self.name = name
        self.teacher_id = teacher_id

    def __repr__(self):
        return (
            f"<Student {self.id}: {self.name} " +
            f"Teacher ID: {self.teacher_id}>"
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def teacher_id(self):
        return self._teacher_id

    @teacher_id.setter
    def teacher_id(self, teacher_id):
        if type(teacher_id) is int and Teacher.find_by_id(teacher_id):
            self._teacher_id = teacher_id
        else:
            raise ValueError(
                "teacher_id must reference a teacher in the database")


    @classmethod
    def get_all(cls):
        """Return a list containing one Student object per table row"""
        sql = """
            SELECT *
            FROM students
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Student instances """
        sql = """
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES teachers(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Student instances """
        sql = """
            DROP TABLE IF EXISTS students;
        """
        CURSOR.execute(sql)
        CONN.commit()



    def save(self):
        sql = """
                INSERT INTO students (name, teacher_id)
                VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.teacher_id,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Student instance."""
        sql = """
            UPDATE students
            SET name = ?, teacher_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.teacher_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Student instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM students
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, teacher_id):
        """ Initialize a new Student instance and save the object to the database """
        student = cls(name, teacher_id)
        student.save()
        return student

    @classmethod
    def instance_from_db(cls, row):
        """Return an Student object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        student = cls.all.get(row[0])
        if student:
            # ensure attributes match row values in case local instance was modified
            student.name = row[1]
            student.teacher_id = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            student = cls(row[1], row[2])
            student.id = row[0]
            cls.all[student.id] = student
        return student


    @classmethod
    def find_by_id(cls, id):
        """Return Student object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM students
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return Student object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM students
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None