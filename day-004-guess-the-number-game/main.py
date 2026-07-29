import random
def main():
	print("Welcome to Guess the Number!")
	secret_number = random.randint(1, 10)
	attempts = 0
	while True:
		try:
			guess = int(input("Guess a number between 1 and 10: "))
			attempts += 1
			if guess < secret_number:
				print("Too low! Try again.")
			elif guess > secret_number:
				print("Too high! Try again.")
			else:
				print(f"Congratulations! You guessed the number in {attempts} attempts!")
				break
		except ValueError:
			print("Invalid input. Please enter a valid number.")
if __name__ == "__main__":
	main()
