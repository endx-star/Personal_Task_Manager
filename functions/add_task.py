from db import get_connection

def add_task_to_db(title, description, due_date, status="Pending", category="General", priority="Normal"):
    """Add a new task to the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, description, due_date, status, category, priority)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (title, description, due_date, status, category, priority))
    conn.commit()
    conn.close()