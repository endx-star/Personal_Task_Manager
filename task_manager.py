import pickle
from task import Task

def add_task(tasks, title, description, due_date):
    new_task = Task(title, description, due_date)
    tasks.append(new_task)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"Task {i}:")
            print(task)

def update_task(tasks, index, title=None, description=None, due_date=None, status=None):
    if 0 <= index < len(tasks):
        task = tasks[index]
        if title:
            task.title = title
        if description:
            task.description = description
        if due_date:
            task.due_date = due_date
        if status:
            task.status = status
        print("Task updated successfully!")
    else:
        print("Invalid task index.")

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        del tasks[index]
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")

def save_tasks(tasks, filename="tasks.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(tasks, file)
    print("Tasks saved successfully!")

def load_tasks(filename="tasks.pkl"):
    try:
        with open(filename, "rb") as file:
            tasks = pickle.load(file)
        print("Tasks loaded successfully!")
        return tasks
    except FileNotFoundError:
        print("No saved tasks found.")
        return []
