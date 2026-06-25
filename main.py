import sqlite3
from datetime import datetime

# ======================
# DATABASE
# ======================

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    status TEXT,
    priority TEXT,
    due_date TEXT
);
""")

# ======================
# HELPER LOGIC
# ======================


def is_overdue(due_date_str):
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")

    return due_date < datetime.now()


def format_task(row):

    if is_overdue(row[4]):
        status_extra = " | OVERDUE"
    else:
        status_extra = ""

    return f"ID: {row[0]} | Task: {row[1]} | Status: {row[2]} | Priority: {row[3]} | Due: {row[4]}{status_extra}"


def print_tasks(rows):
    if not rows:
        print("No tasks found")
        return
    
    for row in rows:
        print(format_task(row))


# ======================
# CRUD FUNCTIONS
# ======================


def show_tasks():
    cursor.execute("""SELECT * FROM tasks ORDER BY due_date""")
    rows = cursor.fetchall()

    print_tasks(rows)


def add_task():
    user_task = input("What task do you want to add? Write a new task: ")

    user_due_time = input("Enter due date (YYYY-MM-DD HH:MM): ")

    due_date = datetime.strptime(user_due_time, "%Y-%m-%d %H:%M")

    cursor.execute("""
    INSERT INTO tasks (title, status, priority, due_date)
    VALUES (?, 'open', 'low', ?);
    """, (user_task, due_date.strftime("%Y-%m-%d %H:%M"),))
    conn.commit()


def update_priority():
    task_id = int(input("Task ID: "))
    priority = input("low/medium/high: ")

    cursor.execute("""
    UPDATE tasks
    SET priority = ?
    WHERE id = ?
    """, (priority, task_id))

    conn.commit()


def update_task():
    try:
        user_id = int(input("Which task do you want to update? Choose the task ID: "))
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (user_id,))
        task = cursor.fetchone()
        
        if not task:
            print("Task not found")
            return

        elif task[2] == 'open':
            cursor.execute("""
            UPDATE tasks
            SET status = 'done'
            WHERE id = ?;
            """, (user_id,))
            conn.commit()
        
        elif task[2] == 'done':
            cursor.execute("""
            UPDATE tasks
            SET status = 'open'
            WHERE id = ?;
            """, (user_id,))
            conn.commit()

    except ValueError:
        print("Please enter a valid number (task ID)")


def delete_task():
    try:
        user_id = int(input("Which task do you want to delete? Choose the task ID: "))
        cursor.execute("SELECT * FROM tasks WHERE id = ?;", (user_id,))
        task = cursor.fetchone()

        if task:
            cursor.execute("""
            DELETE FROM tasks
            WHERE id = ?;
            """, (user_id,))
            conn.commit()
          
        else:
            print("Task not found")

    except ValueError:
        print("Please enter a valid number (task ID)")


def filter_tasks():
    status = input("Filter by status: (open / done): ").strip().lower()

    if status not in ["open", "done"]:
        print("Invalid status")
        return
    
    cursor.execute("""SELECT * FROM tasks WHERE status = ?""", (status,))
    rows = cursor.fetchall()

    print_tasks(rows)


def search_tasks():
    user_request = input("Enter search title/status/priority: ").strip().lower()
    search_pattern = f"%{user_request}%"
    cursor.execute("""
    SELECT * FROM tasks WHERE title LIKE ?
    OR status LIKE ? OR priority LIKE ?""", (search_pattern, search_pattern, search_pattern,))
    rows = cursor.fetchall()

    print_tasks(rows)


def filter_overdue_tasks():
    cursor.execute("""SELECT * FROM tasks ORDER BY due_date""")
    rows = cursor.fetchall()

    found = False

    for row in rows:
        if is_overdue(row[4]):
            print(format_task(row))
            found = True

    if not found:
        print("No tasks found")
        

# ======================
# UI
# ======================


def menu():
    menu_options = ["1. Add task", "2. Show tasks", "3. Update task", "4. Delete task", "5. Filter tasks", "6. Update priority", "7. Search tasks", "8. Show overdue tasks", "9. Exit"]
    for menu_option in menu_options:
        print(f"{menu_option}")


def main():
    while True:
        menu()
        choice = input("Choose the option: ")

        if choice == "1":
            add_task()
            print("Task added successfully.")
            
        elif choice == "2":
            show_tasks()
            input("Press Enter to continue...")

        elif choice == "3":
            update_task()
            print("Task updated successfully.")

        elif choice == "4":
            delete_task()
            print("Task deleted successfully.")

        elif choice == "5":
            filter_tasks()
            input("Press Enter to continue...")

        elif choice == "6":
            update_priority()
            print("Priority updated successfully.")

        elif choice == "7":
            search_tasks()
            input("Press Enter to continue...")

        elif choice == "8":
            filter_overdue_tasks()
            input("Press Enter to continue...")

        elif choice == "9":
            break    

        else:
            print("Invalid option") 


main()