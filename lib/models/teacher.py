# lib/models/department.py
from __init__ import CURSOR, CONN





class Teacher:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name):
        self.name = name

    # def __repr__(self):
    #     return f"<Hi,{self.name}>"

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
    name = "Allen"

    def get_all(name):
            return f"Hello, {name}!"



    # @classmethod
    # def create_table(cls):
    #     """ Create a new table to persist the attributes of Department instances """
    #     sql = """
    #         CREATE TABLE IF NOT EXISTS departments (
    #         id INTEGER PRIMARY KEY,
    #         name TEXT,
    #         location TEXT)
    #     """
    #     CURSOR.execute(sql)
    #     CONN.commit()

    # @classmethod
    # def drop_table(cls):
    #     """ Drop the table that persists Department instances """
    #     sql = """
    #         DROP TABLE IF EXISTS departments;
    #     """
    #     CURSOR.execute(sql)
    #     CONN.commit()