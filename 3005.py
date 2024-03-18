import psycopg2

# The code in 3005.py is a Python program that connects to a PostgreSQL database and retrieves all the students from the students table. The program uses the psycopg2 library to connect to the database and execute SQL queries. The getAllStudents function connects to the database, retrieves all the students from the students table, and prints the results. The main function calls the getAllStudents function to retrieve and print all the students from the database.

# This function connects to the database and retrieves all the students from the students table. It then prints the results.
def getAllStudents():
    with psycopg2.connect("dbname='3005 assignment 3' user=postgres password=postgres host=localhost") as database:
        with database.cursor() as cur:
            cur.execute("SELECT * FROM students")
            rows = cur.fetchall()  
            for row in rows:
                print(row)
                
# This function connects to the database and adds a new student to the students table.
def addStudent(first_name, last_name, email, enrollment_date):
    with psycopg2.connect("dbname='3005 assignment 3' user=postgres password=postgres host=localhost") as database:
        with database.cursor() as cur:
            cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
            database.commit()
            print("Student added")
            
# This function connects to the database and updates the email of a student in the students table.  
def updateStudentEmail(student_id, new_email):
    with psycopg2.connect("dbname='3005 assignment 3' user=postgres password=postgres host=localhost") as database:
        with database.cursor() as cur:
            cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
            database.commit()
            print("Email updated")
            
            
# This function connects to the database and deletes a student from the students table.
def deleteStudent(student_id):
    with psycopg2.connect("dbname='3005 assignment 3' user=postgres password=postgres host=localhost") as database:
        with database.cursor() as cur:
            cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
            database.commit()
            print("Student deleted")

            
# This function is the main function that allows the user to interact with the program. It presents a menu of options to the user and calls the appropriate functions based on the user's choice.   
def main():
    while True:
        print("1. Get all students")
        print("2. Add a student")
        print("3. Update student email")
        print("4. Delete student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            getAllStudents()
        elif choice == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date: ")
            addStudent(first_name, last_name, email, enrollment_date)
        elif choice == "3":
            student_id = input("Enter student id: ")
            new_email = input("Enter new email: ")
            updateStudentEmail(student_id, new_email)
        elif choice == "4":
            student_id = input("Enter student id: ")
            deleteStudent(student_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice")
            
            
main()


