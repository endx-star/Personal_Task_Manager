from db import get_connection

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