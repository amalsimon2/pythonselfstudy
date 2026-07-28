# Import necessary library
import sys
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = 'Done' if task['done'] else 'Pending'
        print(f"{i}. {task['description']} - {status}")
def add_task(tasks):
    description = input("Enter task description: ").strip()
    if not description:
        print("Task description cannot be empty.")
        return
    tasks.append({'description': description, 'done': False})
    print(f"Task '{description}' added successfully.")
def mark_task(tasks):
    try:
        task_number = int(input("Enter task number to mark as done: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['done'] = True
            print(f"Task '{tasks[task_number - 1]['description']}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def main():
    tasks = []
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            mark_task(tasks)
        elif choice == '4':
            print("Exiting To-Do List Manager.")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
if __name__ == '__main__':
    main()