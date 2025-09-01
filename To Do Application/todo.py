# Store tasks in a Python list
tasks = []

def show_menu():
    """Display the main menu options."""
    print("\n==== To-Do List Menu ====")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Delete a Task")
    print("4. Quit")


def add_task():
    """Add a task to the task list."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task added: {task}")
    else:
        print("Task cannot be empty!")


def view_tasks():
    """Display all tasks in the list."""
    if not tasks:
        print("No tasks to display.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")


def delete_task():
    """Delete a task by index."""
    if not tasks:
        print("No tasks to delete.")
        return

    try:
        view_tasks()
        choice = int(input("Enter the task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"Task deleted: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    """Main program loop."""
    print("Welcome to the To-Do List App!")
    
    while True:
        show_menu()
        try:
            choice = input("Select an option (1-4): ").strip()
            
            if choice == "1":
                add_task()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                delete_task()
            elif choice == "4":
                print("Goodbye! Thanks for using the To-Do List App.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        finally:
            print("\n--- Returning to menu ---")


if __name__ == "__main__":
    main() 