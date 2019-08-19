import sqlite3
from orm import ORM

class Branch(ORM):
    dbpath = "employees.db"
    tablename = "branches"
    fields = ['City','State','Zip']

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.city = kwargs.get("City")
        self.state = kwargs.get('State')
        self.zip = kwargs.get('zip')