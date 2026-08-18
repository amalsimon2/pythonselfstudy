import time

def main():
    print('Welcome to the Interactive Storytelling Game!')
    time.sleep(1)
    print('You find yourself in a dark forest.')
    time.sleep(1)
    print('Do you want to go left or right?')
    choice = input('> ').lower()
    if choice == 'left':
        print('You encounter a friendly wizard who gives you a map.')
    elif choice == 'right':
        print('You find a treasure chest filled with gold and jewels.')
    else:
        print('Invalid choice. The forest starts to grow dark and ominous.')

if __name__ == '__main__':
    main()
