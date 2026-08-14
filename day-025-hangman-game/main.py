import random

def get_word(words):
    return random.choice(words)

def display_hangman(tries):
    stages = ["", "O", "O-", "O--", "O---", "-----"]
    return stages[tries]

def play_game():
    words = ['python', 'hangman', 'programming', 'developer', 'computer']
    word = get_word(words)
    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")

    while True:
        display_word = [letter if letter in guessed_letters else '_' for letter in word]
        print(display_hangman(tries))
        print(' '.join(display_word))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            tries -= 1
            print("Incorrect. You have", tries, "tries left")

        if '_' not in display_word:
            print(' '.join(display_word))
            print("Congratulations! You guessed the word.")
            break

        if tries == 0:
            print(display_hangman(tries))
            print("Game over. The word was", word)
            break

if __name__ == '__main__':
    play_game()
