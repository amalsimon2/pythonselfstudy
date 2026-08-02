import json

todo_list = []
file_path = 'todo.json'

try:
    with open(file_path, 'r') as file:
        todo_list = json.load(file)
except FileNotFoundError:
    pass

while True:
    print('\n1. Add task\n2. View tasks\n3. Remove task\n4. Exit\n')
    choice = input('Enter your choice: ')

    if choice == '1':
        task = input('Enter the task: ')
        todo_list.append(task)
        print('Task added!\n')
    elif choice == '2':
        if not todo_list:
            print('No tasks to display.\n')
        else:
            for index, task in enumerate(todo_list, 1):
                print(f'{index}. {task}')
    elif choice == '3':
        try:
            index = int(input('Enter the task number to remove: '))
            if 1 <= index <= len(todo_list):
                removed_task = todo_list.pop(index - 1)
                print(f'Task {removed_task} removed!\n')
            else:
                print('Invalid task number.\n')
        except ValueError:
            print('Please enter a valid number.\n')
    elif choice == '4':
        with open(file_path, 'w') as file:
            json.dump(todo_list, file)
        break
    else:
        print('Invalid choice. Please try again.\n')
