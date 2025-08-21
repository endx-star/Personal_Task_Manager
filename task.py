class Task:
    def __init__(self, title, description, due_date, status="Pending", category="General", priority="Normal"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.category = category
        self.priority = priority

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Due Date: {self.due_date}\n"
            f"Status: {self.status}\n"
            f"Category: {self.category}\n"
            f"Priority: {self.priority}\n"
        )
