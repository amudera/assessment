import sqlite3
import os

DIRPATH = os.path.dirname(__file__)
DBFILENAME = "employees.db"
DBPATH = os.path.join(DIRPATH, DBFILENAME)

def seed(dbpath):

    employees = [
        ("Lockett", "Walker", "S0001", 45000,),
        ("Coleman", "Casey", "S0002", 70000,),
        ("Kilome", "Franklyn", "S0003", 67000,),
        ("Santiago", "Hecton", "S0004", 100000,),
        ("Valdez", "Framber", "S0005", 39000,),
        ("Peacock", "Brad", "S0006", 51000,),
        ("Guduan", "Reymin", "S0007", 67000,),
        ("Cole", "Gerrit", "S0008", 55000,)]
  

    branches = [
        ("Flushing","NY","11368",),
        ("Houston","TX","77002",)]
           

    employees_branches = [
            (1,1),
            (2,1),
            (3,1),
            (4,1),
            (5,2),
            (6,2),
            (7,2),
            (8,2)]
            
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()
        
        SQL = """INSERT INTO employees(First_name,Last_name,employee_id,salary) VALUES(?,?,?,?);"""
        for employee in employees:
            cursor.execute(SQL, employee)

        SQL = """INSERT INTO branches(City,State,Zip) VALUES(?,?,?);"""
        for branch in branches:
            cursor.execute(SQL, branch)

        SQL = """INSERT INTO employees_branches VALUES(?,?);"""
        for employee_branch in employees_branches:
            cursor.execute(SQL, employee_branch)

if __name__ == "__main__":
    seed(DBPATH)