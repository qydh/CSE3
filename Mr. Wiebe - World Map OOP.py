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

