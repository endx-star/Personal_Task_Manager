import tkinter as tk
from tkinter import messagebox, simpledialog
from task_manager import add_task, view_tasks, update_task, delete_task, save_tasks, load_tasks
from task import Task

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.tasks = load_tasks()

        # Main window widgets
        self.label = tk.Label(root, text="Task Manager", font=("Arial", 16))
        self.label.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task_window)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(root, text="View Tasks", command=self.view_tasks_window)
        self.view_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task_window)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task_window)
        self.delete_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save and Exit", command=self.save_and_exit)
        self.save_button.pack(pady=5)

    def add_task_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Task")

        tk.Label(add_window, text="Title:").pack()
        title_entry = tk.Entry(add_window)
        title_entry.pack()

        tk.Label(add_window, text="Description:").pack()
        desc_entry = tk.Entry(add_window)
        desc_entry.pack()

        tk.Label(add_window, text="Due Date:").pack()
        date_entry = tk.Entry(add_window)
        date_entry.pack()

        def submit():
            title = title_entry.get()
            description = desc_entry.get()
            due_date = date_entry.get()
            if title and description and due_date:
                add_task(self.tasks, title, description, due_date)
                messagebox.showinfo("Success", "Task added successfully!")
                add_window.destroy()
            else:
                messagebox.showerror("Error", "All fields are required!")

        submit_button = tk.Button(add_window, text="Submit", command=submit)
        submit_button.pack(pady=5)

    def view_tasks_window(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Tasks")

        if not self.tasks:
            tk.Label(view_window, text="No tasks found.").pack()
            return

        for i, task in enumerate(self.tasks, start=1):
            task_label = tk.Label(view_window, text=f"Task {i}: {task.title} - {task.status}")
            task_label.pack(anchor="w")

    def update_task_window(self):
        if not self.tasks:
            messagebox.showinfo("Info", "No tasks to update.")
            return

        update_window = tk.Toplevel(self.root)
        update_window.title("Update Task")

        tk.Label(update_window, text="Select Task:").pack()
        task_list = [f"{i+1}. {task.title}" for i, task in enumerate(self.tasks)]
        task_var = tk.StringVar(update_window)
        task_var.set(task_list[0])
        task_menu = tk.OptionMenu(update_window, task_var, *task_list)
        task_menu.pack()

        tk.Label(update_window, text="New Title:").pack()
        title_entry = tk.Entry(update_window)
        title_entry.pack()

        tk.Label(update_window, text="New Description:").pack()
        desc_entry = tk.Entry(update_window)
        desc_entry.pack()

        tk.Label(update_window, text="New Due Date:").pack()
        date_entry = tk.Entry(update_window)
        date_entry.pack()

        tk.Label(update_window, text="New Status:").pack()
        status_entry = tk.Entry(update_window)
        status_entry.pack()

        def submit():
            index = task_var.get().split(".")[0]
            index = int(index) - 1
            title = title_entry.get() or None
            description = desc_entry.get() or None
            due_date = date_entry.get() or None
            status = status_entry.get() or None
            update_task(self.tasks, index, title, description, due_date, status)
            messagebox.showinfo("Success", "Task updated successfully!")
            update_window.destroy()

        submit_button = tk.Button(update_window, text="Submit", command=submit)
        submit_button.pack(pady=5)

    def delete_task_window(self):
        if not self.tasks:
            messagebox.showinfo("Info", "No tasks to delete.")
            return

        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Task")

        tk.Label(delete_window, text="Select Task:").pack()
        task_list = [f"{i+1}. {task.title}" for i, task in enumerate(self.tasks)]
        task_var = tk.StringVar(delete_window)
        task_var.set(task_list[0])
        task_menu = tk.OptionMenu(delete_window, task_var, *task_list)
        task_menu.pack()

        def submit():
            index = task_var.get().split(".")[0]
            index = int(index) - 1
            delete_task(self.tasks, index)
            messagebox.showinfo("Success", "Task deleted successfully!")
            delete_window.destroy()

        submit_button = tk.Button(delete_window, text="Submit", command=submit)
        submit_button.pack(pady=5)

    def save_and_exit(self):
        save_tasks(self.tasks)
        self.root.destroy()
