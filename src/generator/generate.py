import random
import json

def generate_dungeon_with_corridors(width, height, num_rooms=10, min_room_size=8, max_room_size=20):
    dungeon = [[5] * width for _ in range(height)]
    rooms = []

    def is_room_valid(room):
        for other_room in rooms:
            if room.intersects(other_room):
                return False
        return True

    def add_room(room):
        for y in range(room.y, room.y + room.height):
            for x in range(room.x, room.x + room.width):
                if x == room.x and y == room.y:
                    dungeon[y][x] = 2  # Coin nord-ouest
                elif x == room.x + room.width - 1 and y == room.y:
                    dungeon[y][x] = 3  # Coin nord-est
                elif x == room.x and y == room.y + room.height - 1:
                    dungeon[y][x] = 8  # Coin sud-ouest
                elif x == room.x + room.width - 1 and y == room.y + room.height - 1:
                    dungeon[y][x] = 4  # Coin sud-est
                elif x == room.x:
                    dungeon[y][x] = 9  # Côté gauche
                elif x == room.x + room.width - 1:
                    dungeon[y][x] = 10  # Côté droit
                elif y == room.y:
                    dungeon[y][x] = 11  # Côté haut
                elif y == room.y + room.height - 1:
                    dungeon[y][x] = 12  # Côté bas
                else:
                    dungeon[y][x] = 0  # Zone traversable à l'in
       

    def add_corridor(start, end):
        x, y = start
        end_x, end_y = end

        while x != end_x:
            dungeon[y][x] = 0  # Zone traversable
            if x < end_x:
                x += 1
            elif x > end_x:
                x -= 1

        while y != end_y:
            dungeon[y][x] = 0  # Zone traversable
            if y < end_y:
                y += 1
            elif y > end_y:
                y -= 1

    for _ in range(num_rooms):
        room_width = random.randint(min_room_size, max_room_size)
        room_height = random.randint(min_room_size, max_room_size)
        room_x = random.randint(0, width - room_width - 1)
        room_y = random.randint(0, height - room_height - 1)
        new_room = Rect(room_x, room_y, room_width, room_height)

        if is_room_valid(new_room):
            add_room(new_room)
            rooms.append(new_room)

    # Choix aléatoire d'une salle pour le spawn
    spawn_room = random.choice(rooms)
    spawn_x = random.randint(spawn_room.x, spawn_room.x + spawn_room.width - 1)
    spawn_y = random.randint(spawn_room.y, spawn_room.y + spawn_room.height - 1)

    # Position de spawn
    spawn_position = (spawn_x, spawn_y)

    # Création des couloirs pour relier les salles
    for i in range(len(rooms) - 1):
        start = rooms[i].center()
        end = rooms[i + 1].center()
        add_corridor(start, end)

    dungeon_json = {
        "map": {
            "nom": "Donjon Mystère",
            "largeur": width,
            "hauteur": height,
            "tiles": dungeon,
            "spawn": spawn_position
        }
    }

    with open("assets/map.json", "w") as json_file:
        json.dump(dungeon_json, json_file, indent=2)

class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def center(self):
        center_x = self.x + self.width // 2
        center_y = self.y + self.height // 2
        return (center_x, center_y)

    def intersects(self, other):
        return (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        )

# Exemple d'utilisation
width = 100
height = 100
generate_dungeon_with_corridors(width, height)
