import random
def deal_card():
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11])
def calculate_score(cards):
    return sum(cards)
def show_hand(cards):
    return ', '.join(map(str, cards))
def main():
    print("Welcome to Blackjack!")
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    print(f"Your hand: {show_hand(player_hand)}")
    print(f"Dealer's hand: {show_hand(dealer_hand)}")
    while True:
        action = input("Do you want to hit or stand? ").lower()
        if action == 'hit':
            player_hand.append(deal_card())
            print(f"Your hand: {show_hand(player_hand)}")
            if calculate_score(player_hand) > 21:
                print("Bust! You lose.")
                return
        elif action == 'stand':
            break
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card())
    print(f"Dealer's hand: {show_hand(dealer_hand)}")
    if calculate_score(dealer_hand) > 21:
        print("Dealer busts! You win.")
    elif calculate_score(dealer_hand) > calculate_score(player_hand):
        print("Dealer wins.")
    elif calculate_score(dealer_hand) < calculate_score(player_hand):
        print("You win.")
    else:
        print("It's a tie.")
if __name__ == '__main__':
    main()
