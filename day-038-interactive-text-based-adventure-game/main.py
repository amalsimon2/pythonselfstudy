import time

class Room:
    def __init__(self, description, exits, item=None):
        self.description = description
        self.exits = exits
        self.item = item

    def move(self, direction):
        return self.exits.get(direction, None)

    def has_item(self):
        return self.item is not None

    def take_item(self):
        item = self.item
        self.item = None
        return item

    def __str__(self):
        return self.description

class Game:
    def __init__(self):
        self.rooms = {}
        self.current_room = None

    def add_room(self, name, description, exits, item=None):
        room = Room(description, exits, item)
        self.rooms[name] = room

    def start(self, start_room):
        self.current_room = start_room
        print(self.current_room)

    def move(self, direction):
        next_room = self.current_room.move(direction)
        if next_room:
            self.current_room = next_room
            print(self.current_room)
        else:
            print('You cannot go that way.')

    def take(self, item_name):
        if self.current_room.has_item() and self.current_room.take_item() == item_name:
            print(f'You take the {item_name}.')
        else:
            print(f'There is no {item_name} in this room.')

if __name__ == '__main__':
    game = Game()
    game.add_room('Start', 'You are in a dark room. There is a door to the north.', {'north': 'Hall'}, 'key')
    game.add_room('Hall', 'You are in a long hall. There are doors to the south and east.', {'south': 'Start', 'east': 'Chest Room'})
    game.add_room('Chest Room', 'You are in a room with a chest. There is a door to the west.', {'west': 'Hall'}, 'treasure')

    game.start('Start')

    while True:
        command = input('> ').lower()
        if command in ['north', 'south', 'east', 'west']:
            game.move(command)
        elif command.startswith('take '):
            item_name = command[5:].strip()
            game.take(item_name)
        elif command == 'quit':
            print('Thanks for playing!')
            break
        else:
            print('Invalid command.')
