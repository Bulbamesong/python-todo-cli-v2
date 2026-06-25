# 📝 Task Manager (Python + SQLite)

A simple console-based Task Manager application built with Python and SQLite.  
The project demonstrates a basic CRUD system with persistent data storage.

---

## 🚀 Features

- Add new tasks
- Show all tasks
- Update task status (open → done)
- Delete tasks
- Persistent storage using SQLite
- Input validation and error handling
- Simple CLI menu system

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

---

## ⚙️ How It Works

The application runs in a loop and displays a menu:

1. Add task
2. Show tasks
3. Update task
4. Delete task
5. Exit

Each option calls a corresponding function:

- Add task → inserts a new task into the database
- Show tasks → displays all tasks
- Update task → changes task status to "done"
- Delete task → removes a task by ID

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

1. Add task
2. Show tasks
3. Update task
4. Delete task
5. Exit

Choose option: 1  
What task do you want to add? Learn Python  
Task added successfully

## 🔧 Future Improvements

- Add task priorities (Done)
- Filter tasks (open / done) (Done)
- Add deadlines (Done)
- Add search functionality
- Improve UI formatting
- Convert to GUI application
- Build web version with Flask or Django

## 👨‍💻 Author

Created as a learning project to practice Python, SQL, and software development fundamentals.

## 📈 Project Goal

The goal of this project is to understand how real applications:

- Store data in a database
- Modify and retrieve data
- Implement CRUD logic
- Structure backend applications properly
