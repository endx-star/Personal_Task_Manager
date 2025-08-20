import tkinter as tk
from tkinter import messagebox, simpledialog
from task_manager import add_task, view_tasks, update_task, delete_task
from task import Task

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.tasks = view_tasks()  # Load tasks from database

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

        self.save_button = tk.Button(root, text="Exit", command=self.exit_app)
        self.save_button.pack(pady=5)

    def add_task_window(self):
        """Open a window to add a new task."""
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
            """Add the task to the database and refresh the task list."""
            title = title_entry.get()
            description = desc_entry.get()
            due_date = date_entry.get()
            if title and description and due_date:
                add_task(title, description, due_date)
                messagebox.showinfo("Success", "Task added successfully!")
                add_window.destroy()
                self.tasks = view_tasks()  # Refresh task list
            else:
                messagebox.showerror("Error", "All fields are required!")

        submit_button = tk.Button(add_window, text="Submit", command=submit)
        submit_button.pack(pady=5)

    def view_tasks_window(self):
        """Open a window to view all tasks."""
        view_window = tk.Toplevel(self.root)
        view_window.title("View Tasks")

        if not self.tasks:
            tk.Label(view_window, text="No tasks found.").pack()
            return

        for task in self.tasks:
            task_label = tk.Label(view_window, text=f"ID: {task.id} - {task.title} ({task.status})")
            task_label.pack(anchor="w")

    def update_task_window(self):
        """Open a window to update a task."""
        if not self.tasks:
            messagebox.showinfo("Info", "No tasks to update.")
            return

        update_window = tk.Toplevel(self.root)
        update_window.title("Update Task")

        tk.Label(update_window, text="Select Task:").pack()
        task_list = [f"{task.id}. {task.title}" for task in self.tasks]
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
            """Update the selected task in the database."""
            task_id = task_var.get().split(".")[0]
            title = title_entry.get() or None
            description = desc_entry.get() or None
            due_date = date_entry.get() or None
            status = status_entry.get() or None
            update_task(task_id, title, description, due_date, status)
            messagebox.showinfo("Success", "Task updated successfully!")
            update_window.destroy()
            self.tasks = view_tasks()  # Refresh task list

        submit_button = tk.Button(update_window, text="Submit", command=submit)
        submit_button.pack(pady=5)

    def delete_task_window(self):
        """Open a window to delete a task."""
        if not self.tasks:
            messagebox.showinfo("Info", "No tasks to delete.")
            return

        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Task")

        tk.Label(delete_window, text="Select Task:").pack()
        task_list = [f"{task.id}. {task.title}" for task in self.tasks]
        task_var = tk.StringVar(delete_window)
        task_var.set(task_list[0])
        task_menu = tk.OptionMenu(delete_window, task_var, *task_list)
        task_menu.pack()

        def submit():
            """Delete the selected task from the database."""
            task_id = task_var.get().split(".")[0]
            delete_task(task_id)
            messagebox.showinfo("Success", "Task deleted successfully!")
            delete_window.destroy()
            self.tasks = view_tasks()  # Refresh task list

        submit_button = tk.Button(delete_window, text="Submit", command=submit)
        submit_button.pack(pady=5)

    def exit_app(self):
        """Close the application."""
        self.root.destroy()
