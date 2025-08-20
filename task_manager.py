from db import init_db, add_task_to_db, get_all_tasks, update_task_in_db, delete_task_from_db
from task import Task

def add_task(title, description, due_date, status="Pending"):
    add_task_to_db(title, description, due_date, status)

def view_tasks():
    return get_all_tasks()

def update_task(task_id, title=None, description=None, due_date=None, status=None):
    update_task_in_db(task_id, title, description, due_date, status)

def delete_task(task_id):
    delete_task_from_db(task_id)
