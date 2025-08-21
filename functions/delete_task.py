from db import get_connection

def delete_task_from_db(task_id):
    """Delete a task from the database by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    conn.commit()
    conn.close()
