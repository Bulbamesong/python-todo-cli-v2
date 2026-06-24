import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    status TEXT
);
""")


def show_tasks():
    cursor.execute("""SELECT * FROM tasks""")
    rows = cursor.fetchall()
    
    if not rows:
        print("No tasks found")
        return
    
    for row in rows:
        print(f"ID: {row[0]} | Task: {row[1]} | Status: {row[2]}")


def add_task():
    user_task = input("What task do you want to add? Write a new task: ")
    cursor.execute("""
    INSERT INTO tasks (title, status)
    VALUES (?, 'open');
    """, (user_task,))
    conn.commit()


def update_task():
    try:
        user_id = int(input("Which task do you want to update? Choose the task ID: "))
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (user_id,))
        task = cursor.fetchone()

        if task:
            cursor.execute("""
            UPDATE tasks
            SET status = 'done'
            WHERE id = ?;
            """, (user_id,))
            conn.commit()

        else:
            print("Task not found")

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


def menu():
    menu_options = ["1. Add task", "2. Show tasks", "3. Update task", "4. Delete task", "5. Exit"]
    for menu_option in menu_options:
        print(f"{menu_option}")

def main():
    while True:
        menu()
        choice = input("Choose the option: ")

        if choice == "1":
            add_task()
            print("Task added successfully")
            
        elif choice == "2":
            show_tasks()
            input("Press Enter to continue...")

        elif choice == "3":
            update_task()
            print("Task updated successfully")

        elif choice == "4":
            delete_task()
            print("Task deleted successfully")

        elif choice == "5":
            break

        else:
            print("Invalid option") 

main()