def get_user_choice():
    while True:
        choice = input("Choose Rock, Paper, or Scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please try again.")
def determine_winner(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"
def main():
    print("Welcome to Rock Paper Scissors!")
    player1 = get_user_choice()
    player2 = get_user_choice()
    result = determine_winner(player1, player2)
    print(result)
if __name__ == '__main__':
    main()
