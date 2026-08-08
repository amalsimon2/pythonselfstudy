import random

def roll_dice():
	return random.randint(1, 6)

print("Welcome to the Dice Roller!")
while True:
	input("Press Enter to roll the dice...")
	result = roll_dice()
	print(f"You rolled a {result}!")
	if input("Roll again? (y/n) ").lower() != 'y':
		break
