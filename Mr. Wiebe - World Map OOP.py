class Room(object):
    def __init__(self, name, north, south):
        self.name = name
        self.north = north
        self.south = south

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
west_house = Room("West of House", 'north_house', None)

current_node = west_house
directions = ['north', 'south', 'east', 'west']
short_directions = ['n', 's', 'e', 'w']

while True:
    print(current_node*********)
    print(current_node*********)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Look for which command we typed in
        pos = short_directions.index(command)
        # Change the command to be the long form
        command = directions[pos]
    if command in directions:
        try:
            ***********
        except KeyError:
            print("You cannot go this way.")
    else:
        print('Command not Recognized')
    print()