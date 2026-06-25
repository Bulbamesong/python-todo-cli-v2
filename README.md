# 📝 Task Manager (Python + SQLite)

A simple console-based Task Manager application built with Python and SQLite.  
The project demonstrates a basic CRUD system with persistent data storage.

---

## 🚀 Features

- Add tasks with priority and due date
- View all tasks with OVERDUE detection
- Update task status (open ↔ done)
- Update task priority (low / medium / high)
- Delete tasks
- Filter tasks by status
- Persistent SQLite storage
- Input validation and error handling
- Simple CLI menu system
- Search tasks by title
- CLI-based interface

---

## 🧱 Tech Stack

- Python 3
- SQLite3 (built-in Python library)

---

## 📂 Database Structure

Table: `tasks`

- `id` INTEGER PRIMARY KEY AUTOINCREMENT — unique task ID
- `title` TEXT — task description
- `status` TEXT — task status (open / done)
- `due_date` TEXT — task due date

---

## ⚙️ How It Works

The program runs in a loop and displays a menu.
Each option triggers a specific function:

- Create → INSERT task into database
- Read → SELECT tasks from database
- Update → change status or priority
- Delete → remove task by ID
- Search / Filter → SQL queries with conditions

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/Bulbamesong/python-todo-cli-v2.git
```

Run the program:

```bash
python main.py
```

---

## 🧠 Key Concepts Used

- CRUD operations (Create, Read, Update, Delete)
- SQLite database integration
- Python functions
- Loops and user input handling
- Error handling with try/except
- CLI application structure

---

## 📌 Example Usage

📋 Menu

1. Add task
2. Show tasks
3. Update task
4. Delete task
5. Filter tasks
6. Update priority
7. Search tasks
8. Exit

➕ Add task
Choose option: 1

What task do you want to add? Learn Python
Enter due date (YYYY-MM-DD HH:MM): 2026-06-26 18:00
Task added successfully

📋 Show tasks
Choose option: 2

ID: 1 | Task: Learn Python | Status: open | Priority: low | Due: 2026-06-26 18:00
ID: 2 | Task: Finish project | Status: open | Priority: high | Due: 2026-06-24 12:00 | OVERDUE

🔁 Update task (toggle open ↔ done)
Choose option: 3

Which task do you want to update? Choose the task ID: 1
Task updated successfully

❌ Delete task
Choose option: 4

Which task do you want to delete? Choose the task ID: 2
Task deleted successfully

🔎 Filter tasks
Choose option: 5

Filter by status: open
ID: 1 | Task: Learn Python | Status: open | Priority: high | Due: 2026-06-26 18:00

⭐ Update priority
Choose option: 6

Task ID: 1
Priority: high
Priority updated successfully

🔍 Search tasks
Choose option: 7

Enter search text: python
ID: 1 | Task: Learn Python | Status: open | Priority: high | Due: 2026-06-26 18:00

📋 Filter overdue tasks
Choose option: 8

ID: 1 | Task: Learn Python | Status: open | Priority: low | Due: 2026-06-26 18:00 | OVERDUE

🚪 Exit
Choose option: 9

---

## 🔧 Update summary

- Added task priority (low / medium / high)
- Added due date support
- Added OVERDUE indicator (calculated in runtime)
- Extended CLI menu (filter + priority update)
- Search tasks by title
- Added overdue task filter

---

## 🔧 Future Improvements

- Improve UI formatting
- Convert to GUI application
- Build web version with Flask or Django

---

## 👨‍💻 Author

Created as a learning project to practice Python, SQL, and software development fundamentals.

---

## 📈 Project Goal

The goal of this project is to understand how real applications:

- Store data in a database
- Modify and retrieve data
- Implement CRUD logic
- Structure backend applications properly
