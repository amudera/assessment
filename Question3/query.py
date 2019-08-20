import sqlite3
from pprint import pprint

connection = sqlite3.connect("employees.db")
cursor = connection.cursor()

def update():
    SQL = "UPDATE employees SET salary=73000 WHERE employee_id ='S0007';"
    cursor.execute(SQL)

def query():

    SQL = "SELECT Last_name,First_name FROM employees JOIN employees_branches ON employees.pk = employees_branches.employees_pk JOIN branches ON branches.pk = employees_branches.branches_pk WHERE employees.salary> 70000 AND branches.state='NY';"
    cursor.execute(SQL)
    results = cursor.fetchall()
    pprint(results)
    quit()

if __name__ == "__main__":
    update()
    query()
