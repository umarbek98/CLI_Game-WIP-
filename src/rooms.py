from enum import Enum

class Rooms:
    rooms = {
        "Grotto of the Mad Forest",
        "Maze of the Spirit's Cult",
        "Crypt of the Cruel Paladin",
        "Tombs of the Vanishing Horsemen",
        "The Swamp Point",
        "The Perfumed Tunnels",
        "The Wondering Haunt",
        "The Ethereal Pits",
        "The Mesmerizing Haunt",
        "The Nether Delves",
    }

class Room:
    def __init__(self,room_id,contents=[]):
        self.room_id = room_id
        self.contents = contents


class Direction(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    NORTHEAST = "NE"
    SOUTHEAST = "SE"
    NORTHWEST = "NW"
    SOUTHWEST = "SW"