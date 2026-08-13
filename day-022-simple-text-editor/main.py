import os
def main():
	file_path = input("Enter file path (e.g., newfile.txt): ")
	try:
		with open(file_path, 'a') as file:
			while True:
				line = input()
				if line == '':
					break
				file.write(line + '\n')
		print(f'File {file_path} saved successfully.')
	except IOError as e:
		print(f'Error: {e}')

if __name__ == '__main__':
	main()
