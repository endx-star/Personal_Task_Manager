from task import Task
from db import get_connection, init_db

from psycopg2 import sql
try:
    from psycopg2.errors import UndefinedTable
except Exception:
    UndefinedTable = None


def get_all_tasks():
    """Fetch all tasks from the database and return as Task objects."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT id, title, description, due_date, status, category, priority FROM tasks')
    except Exception as exc:
        # If table doesn't exist yet, create it and retry once
        if (UndefinedTable is not None and isinstance(exc, UndefinedTable)) or (
            getattr(exc, "__class__", None) and exc.__class__.__name__ == "UndefinedTable"
        ):
            conn.close()
            init_db()
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT id, title, description, due_date, status, category, priority FROM tasks')
        else:
            conn.close()
            raise
    tasks = []
    for row in cursor.fetchall():
        task = Task(row[1], row[2], row[3], row[4], row[5], row[6])
        task.id = row[0]  # Set the task ID
        tasks.append(task)
    conn.close()
    return tasks