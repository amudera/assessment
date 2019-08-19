import sqlite3
from orm import ORM

class Employee(ORM):
    dbpath = "employees.db"
    tablename = "employees"
    fields = ['Last_name','First_name','employee_id','salary']

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.last_name = kwargs.get("Last_name")
        self.first_name = kwargs.get('First_name')
        self.employee_id = kwargs.get('employee_id')
        self.salary = kwargs.get('salary')
    
    def branch(self):
        employee_id = input("ID: ")
        SQL = "SELECT * FROM employees JOIN employees_branches ON employees.pk = employees_branches.employees_pk JOIN branches ON branches.pk = employees_branches.branches_pk WHERE employee_id=?;".format(employee_id)
        with sqlite3.connect(dbpath) as conn:
                conn.row_factory = sqlite3.Row
                curs = conn.cursor()

                curs.execute(SQL)
                results = curs.fetchall()
                print(results)
    
    #unittest would create a new user for a new branch, save the user and then use the above to check if Equal the new branch that was added
    