from db import get_connection

def update_task_in_db(task_id, title=None, description=None, due_date=None, status=None, category=None, priority=None):
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
    if category:
        updates.append("category = %s")
        params.append(category)
    if priority:
        updates.append("priority = %s")
        params.append(priority)
    if updates:
        set_clause = ", ".join(updates)
        params.append(task_id)
        cursor.execute(f"UPDATE tasks SET {set_clause} WHERE id = %s", params)
        conn.commit()
    conn.close()