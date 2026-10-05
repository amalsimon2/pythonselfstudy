import random
def main():
    print("Welcome to the Adventure Game!")
    name = input("What is your name? ")
    print(f"Hello, {name}! You find yourself at the crossroads.")
    direction = input("Which direction do you choose? (left/right) ")
    if direction.lower() == "left":
        left_path()
    elif direction.lower() == "right":
        right_path()
    else:
        print("Invalid choice. Game over.")

def left_path():
    print("You chose the left path. A wild monster appears!")
    action = input("Do you fight or run? (fight/run) ")
    if action.lower() == "fight":
        print("You bravely fought the monster and won!")
    elif action.lower() == "run":
        print("You ran away safely!")
    else:
        print("Invalid choice. Game over.")

def right_path():
    print("You chose the right path. You find a treasure chest!")
    treasure = input("Do you open the chest or leave it? (open/leave) ")
    if treasure.lower() == "open":
        print("You opened the chest and found a gold coin! You win!")
    elif treasure.lower() == "leave":
        print("You left the chest alone. Game over.")
    else:
        print("Invalid choice. Game over.")

if __name__ == '__main__':
    main()
