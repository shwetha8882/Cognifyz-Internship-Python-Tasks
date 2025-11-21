import os

FILE_NAME = "tasks.txt"

class Task:
    def __init__(self, task_id, name, description, status="Pending"):
        self.task_id = task_id
        self.name = name
        self.description = description
        self.status = status

def load_tasks():
    tasks = []
    if not os.path.exists(FILE_NAME):
        return tasks
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, name, description, status = line.strip().split("|")
                tasks.append(Task(task_id, name, description, status))
    except:
        print("Error loading tasks.")
    return tasks

def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            for t in tasks:
                file.write(f"{t.task_id}|{t.name}|{t.description}|{t.status}\n")
    except:
        print("Error saving tasks.")

tasks = load_tasks()

def create_task():
    task_id = input("Enter Task ID: ")
    name = input("Enter Task Name: ")
    description = input("Enter Task Description: ")
    new_task = Task(task_id, name, description)
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!\n")

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return
    print("\n--- TASK LIST ---")
    for task in tasks:
        print(f"ID: {task.task_id}, Name: {task.name}, Description: {task.description}, Status: {task.status}")
    print()

def update_task():
    task_id = input("Enter Task ID to update: ")
    for task in tasks:
        if task.task_id == task_id:
            task.name = input("Enter new name: ")
            task.description = input("Enter new description: ")
            task.status = input("Enter new status (Pending/Completed): ")
            save_tasks(tasks)
            print("Task updated successfully!\n")
            return
    print("Task not found!\n")

def delete_task():
    task_id = input("Enter Task ID to delete: ")
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!\n")
            return
    print("Task not found!\n")

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")
