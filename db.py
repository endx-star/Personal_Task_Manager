import os
from pathlib import Path

import psycopg2
from psycopg2 import sql
try:
    from psycopg2.errors import UndefinedTable
except Exception:
    UndefinedTable = None
from task import Task

# Load environment variables from a local .env file in this directory
try:
    from dotenv import load_dotenv
    _ENV_PATH = Path(__file__).resolve().parent / ".env"
    # load_dotenv is safe to call even if the file does not exist
    load_dotenv(_ENV_PATH)
except Exception:
    # If python-dotenv is not installed, environment variables can still be
    # provided via the OS environment. We fail gracefully here.
    pass

# Read database settings from environment variables
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")




def get_connection():
    """Create and return a PostgreSQL connection."""
    if not DB_NAME or not DB_USER or not DB_PASSWORD:
        raise RuntimeError(
            "Missing required database environment variables. Ensure DB_NAME, "
            "DB_USER, and DB_PASSWORD are set (e.g., in Personal_Task_Manager/.env)."
        )
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

def init_db():
    """Initialize the database and create the tasks table if it doesn't exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            due_date TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_task_to_db(title, description, due_date, status="Pending"):
    """Add a new task to the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, description, due_date, status)
        VALUES (%s, %s, %s, %s)
    ''', (title, description, due_date, status))
    conn.commit()
    conn.close()

def get_all_tasks():
    """Fetch all tasks from the database and return as Task objects."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT id, title, description, due_date, status FROM tasks')
    except Exception as exc:
        # If table doesn't exist yet, create it and retry once
        if (UndefinedTable is not None and isinstance(exc, UndefinedTable)) or (
            getattr(exc, "__class__", None) and exc.__class__.__name__ == "UndefinedTable"
        ):
            conn.close()
            init_db()
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT id, title, description, due_date, status FROM tasks')
        else:
            conn.close()
            raise
    tasks = []
    for row in cursor.fetchall():
        task = Task(row[1], row[2], row[3], row[4])
        task.id = row[0]  # Set the task ID
        tasks.append(task)
    conn.close()
    return tasks

def update_task_in_db(task_id, title=None, description=None, due_date=None, status=None):
    """Update a task in the database by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    updates = []
    params = []
    if title:
        updates.append("title = %s")
        params.append(title)
    if description:
        updates.append("description = %s")
        params.append(description)
    if due_date:
        updates.append("due_date = %s")
        params.append(due_date)
    if status:
        updates.append("status = %s")
        params.append(status)
    if updates:
        set_clause = ", ".join(updates)
        params.append(task_id)
        cursor.execute(f"UPDATE tasks SET {set_clause} WHERE id = %s", params)
        conn.commit()
    conn.close()

def delete_task_from_db(task_id):
    """Delete a task from the database by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    conn.commit()
    conn.close()
