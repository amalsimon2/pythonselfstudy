import sys

print('Welcome to the Interactive Storytelling Game!')
print('You find yourself at a crossroads. Do you go left or right? Type left/right:')
choice = input().strip().lower()

if choice == 'left':
    print('You encounter a dragon! Do you fight or run? Type fight/run:')
    dragon_choice = input().strip().lower()
    if dragon_choice == 'fight':
        print('You bravely fought the dragon and defeated it! You win!')
    else:
        print('You ran away, but the dragon caught up with you and you lost. Game over.')
elif choice == 'right':
    print('You find a hidden treasure chest! What do you do? Type open/close:')
    treasure_choice = input().strip().lower()
    if treasure_choice == 'open':
        print('You opened the chest and found a lot of gold! You win!')
    else:
        print('You closed the chest and left it there. You win by avoiding danger!')
else:
    print('Invalid choice. Game over.')

print('Thanks for playing!')
sys.exit()
