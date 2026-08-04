def get_user_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")
def determine_winner(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == 'rock' and player2 == 'scissors') or (player1 == 'paper' and player2 == 'rock') or (player1 == 'scissors' and player2 == 'paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"
def main():
    print("Welcome to Rock Paper Scissors Game!")
    player1_choice = get_user_choice()
    player2_choice = get_user_choice()
    result = determine_winner(player1_choice, player2_choice)
    print(f"Player 1 chose {player1_choice}")
    print(f"Player 2 chose {player2_choice}")
    print(result)
if __name__ == '__main__':
    main()
