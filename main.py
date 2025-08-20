import tkinter as tk
from ui import TaskManagerApp
from db import init_db

def main():
    # Ensure database and tables exist before launching the UI
    init_db()
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
