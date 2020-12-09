import sqlite3
print("-------- START OF ETL --------")

# Initiate a New SQLite DB

# To Create an Empty SQLlite DB:
# Simply sqlite3.connect() to Whatever you 
# want your new DB to be called.

# sqlite3.connect('Type your New DataBase name here.db')

db_path = 'study_part1.sqlite3'

# Establish Connection
conn = sqlite3.connect(db_path)
print("SQLite Connection Established")
# Intantiate Cursor
curs = conn.cursor()
print("Cursor Instantiated")


Q_CREATE_TABLE_STUDENTS = """ 
    CREATE TABLE IF NOT EXISTS students (
        student VARCHAR(50),
        studied TEXT,
        grade INT,
        age INT,
        sex VARCHAR(10)
    );
    """

# Excecute CREATE TABLE Query
curs.execute(Q_CREATE_TABLE_STUDENTS)

# Commit New Table on the Connection
conn.commit()
print("Table Successfully Created")

# Get Data
student_data = (('Lion-O', 'True', 85, 24, 'Male'), 
                ('Cheetara', 'True', 95, 22, 'Female'),
                ('Mumm-Ra', 'False', 65, 153, 'Male'),
                ('Snarf', 'False', 70, 15, 'Male'), 
                ('Panthro', 'True', 80, 30, 'Male'))

# ? is the placeholder value for SQLite
Q_INSERT_ROWS_INTO_STUDENTS = """
INSERT INTO students(student, studied, grade, age, sex)
VALUES (?, ?, ?, ?, ?);
    """

# In the Excecute method, you can pass values as a second argument
# AFTER passing a Query String that Contains Placeholder Values 
# which for SQLite are '?'. 
# ---> For PostgreSQL the placeholder value works the same way but it
#      is '%s'. <-- Just FYI
for row in student_data:
    curs.execute(Q_INSERT_ROWS_INTO_STUDENTS, row)

# Commit Inserted Rows on the Connection
conn.commit()
print("Rows Successfully Inserted")

# --- Check on the Success of the Insertion ---

# Get 5 Rows from New Table, Students
Q_GET_ALL_FROM_NEW_TABLE = """
SELECT * FROM students LIMIT 5;
    """

# Excecute Query
response = curs.execute(Q_GET_ALL_FROM_NEW_TABLE).fetchall()

# Print Response
print("--- SELECT * RESPONSE ---")
print(response)
print("--- RESPONSE END ---")

# Close Up Shop -> Close Cursor and Connection
curs.close()
print("Cursor Closed")
conn.close()
print("Connection Closed")
print("-------- END OF ETL --------")