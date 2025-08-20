from task_manager import add_task, view_tasks, update_task, delete_task, save_tasks, load_tasks

def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            add_task(tasks, title, description, due_date)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks)
            try:
                index = int(input("Enter task number to update: ")) - 1
                title = input("Enter new title (leave blank to skip): ")
                description = input("Enter new description (leave blank to skip): ")
                due_date = input("Enter new due date (leave blank to skip): ")
                status = input("Enter new status (leave blank to skip): ")
                update_task(tasks, index, title or None, description or None, due_date or None, status or None)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            view_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(tasks, index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
