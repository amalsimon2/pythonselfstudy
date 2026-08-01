import sys

tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task added: {task}')

def view_tasks():
    if not tasks:
        print('No tasks to display.')
    else:
        for index, task in enumerate(tasks, start=1):
            print(f'{index}. {task}')

def remove_task(index):
    try:
        removed_task = tasks.pop(index-1)
        print(f'Task removed: {removed_task}')
    except IndexError:
        print('Invalid task index.')

while True:
    print('\nTo-Do List Manager\n')
    print('1. Add Task')
    print('2. View Tasks')
    print('3. Remove Task')
    print('4. Exit')
    choice = input('Choose an option (1/2/3/4): ')

    if choice == '1':
        task = input('Enter the task: ')
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        index = int(input('Enter the task number to remove: '))
        remove_task(index)
    elif choice == '4':
        print('Exiting...')
        sys.exit()
    else:
        print('Invalid option. Please choose 1, 2, 3, or 4.')
