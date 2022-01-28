from config import *
import sqlite3

# Databse connection
conn = sqlite3.connect("students.db")

def main():

    # Number of students to add
    number = get_positive_int("How many students do you want to add? ")

    # Add new students
    students = add_students(number)
    print(students)

# Create students based on the given number
def add_students(n):

    # Added students list
    added = []

    # Connection cursor
    c = conn.cursor()

    # Count current number of students in database
    count = c.execute("SELECT COUNT(*) FROM students").fetchall()[0][0]
    for i in range(0, n):
        # Get student name
        name = input("Name: ")

        # Get first grade
        get_g1 = get_grade("First grade: ")

        # Get second grade
        get_g2 = get_grade("Second grade: ")

        # Create student object
        s = Student(f"{i + count + 1000}", name, get_g1, get_g2)

        # Insert student into database
        c.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?)", (i + count + 1, s.code, s.name, s.g1, s.g2, s.g, s.apprv))

        # Append student to list
        added.append({"code" : s.code, "name": s.name, "first grade": s.g1, "second grade" : s.g2, "final grade" : s.g, "approved" : s.apprv})

    # Commit database changes
    conn.commit()
    # Close database connection
    conn.close()

    return added

if __name__ == "__main__":
    main()