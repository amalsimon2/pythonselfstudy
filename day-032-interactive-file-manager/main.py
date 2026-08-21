import os


def list_files(directory):
    try:
        files = os.listdir(directory)
        print(f'Files in {directory}: {files}')
    except FileNotFoundError:
        print('Directory not found.')

def create_file(file_path):
    try:
        with open(file_path, 'w') as file:
            file.write('')
        print(f'File created: {file_path}')
    except Exception as e:
        print(f'Error creating file: {e}')

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f'File deleted: {file_path}')
    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print(f'Error deleting file: {e}')

def rename_file(old_path, new_path):
    try:
        os.rename(old_path, new_path)
        print(f'File renamed from {old_path} to {new_path}')
    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print(f'Error renaming file: {e}')

if __name__ == '__main__':
    directory = input('Enter directory path: ')
    list_files(directory)
    file_path = input('Enter file path to create: ')
    create_file(file_path)
    file_path = input('Enter file path to delete: ')
    delete_file(file_path)
    old_path = input('Enter old file path: ')
    new_path = input('Enter new file path: ')
    rename_file(old_path, new_path)
