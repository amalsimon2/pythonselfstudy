import random
def main():
    print('Welcome to Number Guessing Game with a Twist!')
    target = random.randint(1, 100)
    user_guess = None
    while user_guess != target:
        try:
            user_guess = int(input('Guess the number between 1 and 100: '))
            if user_guess < target:
                print('Higher!')
            elif user_guess > target:
                print('Lower!')
        except ValueError:
            print('Please enter a valid integer.')
    print(f'Congratulations! You guessed the number {target}.')
if __name__ == '__main__':
    main()
