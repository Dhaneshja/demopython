import sqlite3

DATABASE_NAME = 'students.db'

def create_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            class TEXT NOT NULL,
            subject1 INTEGER NOT NULL,
            subject2 INTEGER NOT NULL,
            subject3 INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def create_student(name, class_name, marks):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO students (name, class, subject1, subject2, subject3)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, class_name, marks['subject1'], marks['subject2'], marks['subject3']))

    student_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return student_id

def get_student(student_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    student = cursor.fetchone()

    conn.close()

    return student

def get_all_students():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()

    conn.close()

    return students

# Example usage:
# delete_student(1)  # Replace 1 with the actual ID of the student you want to delete


