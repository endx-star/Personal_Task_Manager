from task import Task
from db import get_connection, init_db

try:
    from psycopg2.errors import UndefinedTable
except Exception:
    UndefinedTable = None


def get_a_task(task_id):
    """Fetch a single task by ID. Returns a Task or None if not found.

    Parameters
    ----------
    task_id : Any
        Identifier of the task (string or integer). Passed directly to the query params.
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT id, title, description, due_date, status FROM tasks WHERE id = %s', (task_id,))
    except Exception as exc:
        if (UndefinedTable is not None and isinstance(exc, UndefinedTable)) or (
            getattr(exc, "__class__", None) and exc.__class__.__name__ == "UndefinedTable"
        ):
            conn.close()
            init_db()
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT id, title, description, due_date, status FROM tasks WHERE id = %s', (task_id,))
        else:
            conn.close()
            raise
    row = cursor.fetchone()
    if not row:
        conn.close()
        return None
    task = Task(row[1], row[2], row[3], row[4])
    task.id = row[0]
    conn.close()
    return task


