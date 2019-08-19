stimport sqlite3
import os

DIRPATH = os.path.dirname(__file__)
DBFILENAME = "employees.db"
DBPATH = os.path.join(DIRPATH, DBFILENAME)


def schema(dbpath):
    with sqlite3.connect(DBPATH) as conn:
        cursor = conn.cursor()

        SQL = "DROP TABLE IF EXISTS employees;"
        cursor.execute(SQL)

        SQL = """CREATE TABLE employees(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            Last_name TEXT,
            First_name TEXT,
            employee_ID VARCHAR(10),
            salary FLOAT
            );"""
        cursor.execute(SQL)

        SQL = "DROP TABLE IF EXISTS branches;"
        cursor.execute(SQL)

        SQL = """CREATE TABLE branches(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            City TEXT,
            State TEXT,
            Zip VARCHAR(10)
        );"""
        cursor.execute(SQL)

        SQL = """DROP TABLE IF EXISTS employees_branches;"""
        cursor.execute(SQL)

        SQL = """CREATE TABLE employees_branches(
            employees_pk,
            branches_pk,
            FOREIGN KEY(employees_pk) REFERENCES employees(pk),
            FOREIGN KEY(branches_pk) REFERENCES branches(pk),
            UNIQUE(employees_pk, branches_pk)
        );"""
        cursor.execute(SQL)

if __name__ == "__main__":
    schema(DBPATH)