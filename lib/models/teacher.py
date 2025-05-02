# lib/models/teacher.py
from __init__ import CURSOR, CONN


class Teacher:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Teacher {self.id}: {self.name}>"

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

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Teacher instances """
        sql = """
            CREATE TABLE IF NOT EXISTS teacher (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Teacher instances """
        sql = """
            DROP TABLE IF EXISTS teacher;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and location values of the current Teacher instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO teacher (name, location)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        """ Initialize a new Teacher instance and save the object to the database """
        teacher = cls(name)
        teacher.save()
        return teacher

    def update(self):
        """Update the table row corresponding to the current Teacher instance."""
        sql = """
            UPDATE teacher
            SET name = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Teacher instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM teacher
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Teacher object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        teacher = cls.all.get(row[0])
        if teacher:
            # ensure attributes match row values in case local instance was modified
            teacher.name = row[1]
        else:
            # not in dictionary, create new instance and add to dictionary
            teacher = cls(row[1], row[2])
            teacher.id = row[0]
            cls.all[teacher.id] = teacher
        return teacher

    @classmethod
    def get_all(cls):
        """Return a list containing a Teacher object per row in the table"""
        sql = """
            SELECT *
            FROM teacher
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Teacher object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM teacher
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Teacher object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM teacher
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def students(self):
        """Return list of students associated with current teacher"""
        from student import Student
        sql = """
            SELECT * FROM students
            WHERE teacher_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Student.instance_from_db(row) for row in rows
        ]