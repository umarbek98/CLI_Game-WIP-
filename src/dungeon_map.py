from __future__ import annotations
from rooms import Room
import random
import click
from rooms import Direction

class DungeonMap:
    def __init__(self):
        self.rooms = {}
        self.player_location = None

    def add_room(self, room:Room):
        if room not in self.rooms:
            self.rooms[room] = {}

    def add_connection(self, room1:Room, room2:Room, direction:Direction.value):
        if room1 not in self.rooms:
            self.add_room(room1)
        if room2 not in self.rooms:
            self.add_room(room2)
        self.rooms[room1][direction] = room2
        self.rooms[room2][opposite_direction(direction)] = room1

    def set_player_location(self, room:Room):
        self.player_location = room

    def move_player(self, direction:Direction.value):
        if direction not in self.rooms[self.player_location]:
            click.echo("You can't go that way!")
            return False
        self.player_location = self.rooms[self.player_location][direction]
        return True


def opposite_direction(direction:Direction.value):
    if direction == Direction.NORTH.value:
        return Direction.SOUTH.value
    elif direction == Direction.NORTHEAST.value:
        return Direction.SOUTHWEST.value
    elif direction == Direction.EAST.value:
        return Direction.WEST.value
    elif direction == Direction.SOUTHEAST.value:
        return Direction.NORTHWEST.value
    elif direction == Direction.SOUTH.value:
        return Direction.NORTH.value
    elif direction == Direction.SOUTHWEST.value:
        return Direction.NORTHEAST.value
    elif direction == Direction.WEST.value:
        return Direction.EAST.value
    elif direction == Direction.NORTHWEST.value:
        return Direction.SOUTHEAST.value
    else:
        raise ValueError("Invalid direction: {}".format(direction))
    
def generate_dungeon(num_rooms):
    # First room is always room 1
    dungeon = DungeonMap()
    first_room = Room(1)
    dungeon.add_room(first_room)
    dungeon.set_player_location(first_room)
    num_created = 1
    while num_created < num_rooms:
        random_room = random.choice(list(dungeon.rooms.keys()))
        direction = random.choice(list(Direction))
        if direction.value not in dungeon.rooms[random_room]:
            if random.random() < 0.8:
                num_created += 1
                new_room_id = num_created
                new_room = Room(new_room_id)
                dungeon.add_room(new_room)
                dungeon.add_connection(random_room,new_room,direction.value)
    return dungeon