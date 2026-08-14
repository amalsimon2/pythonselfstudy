import random

words = ['python', 'hangman', 'programming', 'challenge', 'beginner']
word = random.choice(words)
guessed_letters = set()
attempts = 6

print("Welcome to Hangman!")

while True:
    display_word = ''.join(letter if letter in guessed_letters else '_' for letter in word)
    print(display_word)
    if '_' not in display_word:
        print('Congratulations! You won!')
        break
    if attempts == 0:
        print(f'Game over! The word was {word}.')
        break
    guess = input('Guess a letter: ').lower()
    if len(guess) != 1 or not guess.isalpha():
        print('Please enter a single letter.')
        continue
    if guess in guessed_letters:
        print('You already guessed that letter.')
        continue
    guessed_letters.add(guess)
    if guess not in word:
        attempts -= 1
        print(f'Incorrect! You have {attempts} attempts left.')
