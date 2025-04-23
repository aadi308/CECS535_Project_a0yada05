import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='aadi98114',  # Change this to your_password
        database='535Projecta0yada05'
    )
    cursor = connection.cursor()
except Error as e:
    print("Connection Error:", e)
    exit()


def create_user(user_id, firstname, lastname, email):
    try:
        cursor.execute('INSERT INTO Users VALUES (%s, %s, %s, %s)', 
                       (user_id, firstname, lastname, email))
        connection.commit()
        print("User created.")
    except Error as e:
        print("Error in create_user:", e)


def create_task(task_id, name, due_date, user_id):
    try:
        cursor.execute('INSERT INTO Tasks (taskId, Name, DueDate, UserId) VALUES (%s, %s, %s, %s)',
                       (task_id, name, due_date, user_id))
        connection.commit()
        print("Task created.")
    except Error as e:
        print("Error in create_task:", e)


def read_users():
    try:
        cursor.execute('SELECT * FROM Users')
        for row in cursor.fetchall():
            print(row)
    except Error as e:
        print("Error in read_users:", e)


def delete_user(user_id):
    try:
        cursor.execute('DELETE FROM Users WHERE userId = %s', (user_id,))
        connection.commit()
        print("User deleted.")
    except Error as e:
        print("Error in delete_user:", e)


def show_overdue_tasks():
    try:
        cursor.callproc('cleaning')
        connection.commit()
        cursor.execute('SELECT * FROM ALERT')
        print("Overdue Tasks in ALERT table:")
        for row in cursor.fetchall():
            print(row)
    except Error as e:
        print("Error in show_overdue_tasks:", e)

def check_pending():
    try:
        user_id = int(input("Enter user ID: "))
        days = int(input("Enter number of days: "))
        if days <= 0:
            print("Number of days must be positive.")
            return
        
        cursor.execute('SELECT COUNT(*) FROM Users WHERE userId = %s', (user_id,))
        if cursor.fetchone()[0] == 0:
            print("User ID not found.")
            return

        cursor.execute('SELECT Pending(%s, %s)', (user_id, days))
        result = cursor.fetchone()
        print(f"Pending tasks due in next {days} days: {result[0]}")
    except Error as e:
        print("Error in check_pending:", e)
    except ValueError:
        print("Invalid input.")



# Sample test run please uncomment for testing
# create_user(10, "Aadi", "Yadav", "a0yada05@louisville.com")
# create_task(110, "Prepare Report", "2025-04-25", 1)
read_users()
show_overdue_tasks()
check_pending()


cursor.close()
connection.close()

