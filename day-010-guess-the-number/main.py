import random
def main():
	secret_number = random.randint(1, 100)
	attempts = 0
	while True:
		try:
			guess = int(input('Guess the number between 1 and 100: '))
			attempts += 1
			if guess < secret_number:
				print('Too low!')
			elif guess > secret_number:
				print('Too high!')
			else:
				print(f'Congratulations! You guessed the number in {attempts} attempts.')
				break
		except ValueError:
			print('Please enter a valid number.')
if __name__ == '__main__':
	main()
