import os

rooms = {
    'Start': {'description': 'You are in a dark room. There is a door to the north.', 'north': 'Hall'},
    'Hall': {'description': 'You are in a long hall. There are doors to the south and east.', 'south': 'Start', 'east': 'Kitchen'},
    'Kitchen': {'description': 'You are in a dimly lit kitchen. There is a door to the west.', 'west': 'Hall'}
}

def get_room(room_name):
    return rooms.get(room_name, {'description': 'Unknown room.'})

def main():
    current_room = 'Start'
    while True:
        room = get_room(current_room)
        print(room['description'])
        action = input('What do you do? (north, south, east, west, quit): ').lower()
        if action == 'quit':
            print('Thanks for playing! Goodbye.')
            break
        elif action in ['north', 'south', 'east', 'west'] and action in room:
            current_room = room[action]
        else:
            print('Invalid action. Try again.')

if __name__ == '__main__':
    main()
