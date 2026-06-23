import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Create Assignments DB if it doesn't already exist
cursor.execute('''CREATE TABLE IF NOT EXISTS assignments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name TEXT NOT NULL,
    assignment_name TEXT NOT NULL,
    due_date TEXT NOT NULL,
    completed INTEGER NOT NULL DEFAULT 0
)''')   

connection.commit()

# Add Assignment Function
def add_assignment(class_name, assignment_name, due_date):

    cursor.execute("""
    INSERT INTO assignments (class_name, assignment_name, due_date) VALUES (?, ?, ?)""",
    (class_name, assignment_name, due_date))
    
    connection.commit()

# Get Assignments Function
def get_assignments():
    cursor.execute("""
    SELECT * FROM assignments
    ORDER BY due_date
    """)


    return cursor.fetchall()

# Complete Assignment Function
def complete_assignment(id):
    cursor.execute("""
    UPDATE assignments
    SET completed = 1
    WHERE id = ?
    """, (id,))

    connection.commit()

print("Database loaded")

print("Functions available:")
print(add_assignment)
print(get_assignments)
print(complete_assignment)


# Create Schedule table
cursor.execute('''CREATE TABLE IF NOT EXISTS schedule (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    day TEXT NOT NULL,
    start_time TEXT NOT NULL,
    end_time TEXT NOT NULL
)
''')

connection.commit()

# Add class to scheule function
def add_class(course_name, day, start_time, end_time):
    cursor.execute("""
    INSERT INTO schedule
    (course_name, day, start_time, end_time) 
    VALUES (?, ?, ?, ?)
    """,
    (course_name, day, start_time, end_time))
    
    connection.commit()

# Get all classes in schedule function
def get_schedule():
    cursor.execute("""
    SELECT * FROM schedule
    ORDER BY day, start_time
    """)
    
    return cursor.fetchall()

print("add_class exists:", "add_class" in globals())
print("get_schedule exists:", "get_schedule" in globals())