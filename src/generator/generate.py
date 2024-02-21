import random
import json

def generate_dungeon_with_corridors(width, height, num_rooms=10, min_room_size=8, max_room_size=15,index=1):
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
        startX = x 
        startY = y       
        while x != end_x:
            dungeon[y][x] = 0 # Zone traversable               
            if x < end_x:
                x += 1
            elif x > end_x:
                x -= 1
        while y != end_y:
            dungeon[y][x] = 0            
            if y < end_y:
                y += 1
            elif y > end_y:
                y -= 1           
                
        
        x, y = start
        end_x, end_y = end
        startX = x 
        startY = y
        
        while x != end_x:
            if x < end_x:               
                x += 1
            elif x > end_x:                
                x -= 1
            if(dungeon[y+1][x] != 0 and x != startX and (y + 1 != end_y and y + 1!= startY)):
                dungeon[y+1][x] = 12 if dungeon[y+1][x] != 0 else 0 # Zone traversable
            if(dungeon[y-1][x] != 0 and x != startX and (y - 1 != end_y and y - 1!= startY)):
                dungeon[y-1][x] = 11 if dungeon[y-1][x] != 0 else 0 # Zone traversable
           
            #horizontal droit
            if(dungeon[y][x] == 0 and (dungeon[y+2][x] == 10 or dungeon[y+2][x] == 3 )  and (dungeon[y+1][x] == 12 or dungeon[y+1][x] == 3 ) ):
                    dungeon[y+1][x] = 21  if dungeon[y+1][x] != 22 else 50 if dungeon[y+1][x] != 0 else 0
            if(dungeon[y][x] == 0 and ( dungeon[y-2][x] == 10 or dungeon[y-2][x] == 4) and (dungeon[y-1][x] == 11 or dungeon[y-1][x] == 4 ) ):
                    dungeon[y-1][x] = 22  if dungeon[y-1][x] != 21 else 50 if dungeon[y-1][x] != 0 else 0  
            #horitontal gauche
            if(dungeon[y][x] == 0 and (dungeon[y+2][x] == 9 or dungeon[y+2][x] == 2 ) and (dungeon[y+1][x] == 12 or dungeon[y+1][x] == 2 )):
                    dungeon[y+1][x] = 24 if dungeon[y+1][x] != 23 else 50 if dungeon[y+1][x] != 0 else 0
            if(dungeon[y][x] == 0 and (dungeon[y-2][x] == 9 or dungeon[y-2][x] == 8 )and (dungeon[y-1][x] == 11 or dungeon[y-1][x] == 8 )):
                    dungeon[y-1][x] = 23 if dungeon[y-1][x] != 24 else 50 if dungeon[y-1][x] != 0 else 0               
        
        while y != end_y:
            if y < end_y:

                y += 1
            elif y > end_y:              
                y -= 1
                
            if(dungeon[y][x+1] != 0 and y != startY  ):
                dungeon[y][x+1] = 10 if dungeon[y][x+1] != 0 else 0 # Zone traversable
            if(dungeon[y][x-1] != 0 and y != startY ):
                dungeon[y][x-1] = 9 if dungeon[y][x-1] != 0 else 0  # Zone traversable              
           
            if(dungeon[y][x] == 0 and (dungeon[y][x-2] == 11 or dungeon[y][x-2] == 2 ) and (dungeon[y][x-1] == 9 or  dungeon[y][x-1] == 2)):
                dungeon[y][x-1] = 23  if dungeon[y][x-1] != 0 else 0
            if(dungeon[y][x] == 0 and (dungeon[y][x+2] == 11 or dungeon[y][x+2] == 3) and (dungeon[y][x+1] == 10 or  dungeon[y][x+1] == 3 )):
                dungeon[y][x+1] = 22  if dungeon[y][x+1] != 0 else 0              
            if(dungeon[y][x] == 0 and (dungeon[y][x-2] == 12 or dungeon[y][x-2] == 8 )and ( dungeon[y][x-1] == 9 or  dungeon[y][x-1] == 8 )):
                dungeon[y][x-1] = 24  if dungeon[y][x-1] != 0 else 0
            if(dungeon[y][x] == 0 and (dungeon[y][x+2] == 12 or dungeon[y][x+2] == 4) and ( dungeon[y][x+1] == 10 or  dungeon[y][x+1] == 10 )):
                dungeon[y][x+1] = 21  if dungeon[y][x+1] != 0 else 0  
            
        if (startY < end_y) :
            if(startX < end_x):
                dungeon[y][end_x+1] = 3  if  dungeon[y][end_x+1] == 5 else  dungeon[y][end_x+1]
                dungeon[y+1][end_x+1] = 10 if dungeon[y+1][end_x+1] == 5 else dungeon[y+1][end_x+1] 
                dungeon[startY][end_x+1] = 10  if  dungeon[startY][end_x+1] == 5 else  dungeon[startY][end_x+1]
                dungeon[startY-1][end_x+1] = 3 if dungeon[startY][end_x+1] == 5 else dungeon[startY][end_x+1]
            else:
                dungeon[y][end_x-1] = 3  if  dungeon[y][end_x-1] == 5 else  dungeon[y][end_x+1]
                dungeon[y+1][end_x-1] = 10 if dungeon[y+1][end_x-1] == 5 else dungeon[y+1][end_x+1] 
                dungeon[startY][end_x-1] = 10  if  dungeon[startY][end_x-1] == 5 else  dungeon[startY][end_x-1]
                dungeon[startY-1][end_x-1] = 3 if dungeon[startY][end_x-1] == 5 else dungeon[startY][end_x-1]
                
       
        
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
   

    # Création des couloirs pour relier les salles
    for i in range(len(rooms) - 1):
        start = rooms[i].center()
        end = rooms[i + 1].center()
        add_corridor(start, end)
        
    spawn_room = random.choice(rooms)
    spawn_x = random.randint(spawn_room.x+1, spawn_room.x + spawn_room.width - 2)
    spawn_y = random.randint(spawn_room.y+1, spawn_room.y + spawn_room.height - 2)

    spawn_room = random.choice(rooms)
    out_x = random.randint(spawn_room.x+1, spawn_room.x + spawn_room.width - 2)
    out_y = random.randint(spawn_room.y+1, spawn_room.y + spawn_room.height - 2)
    dungeon[out_y][out_x] = 20
    # Position de spawn
    spawn_position = (spawn_x, spawn_y)
    dungeon_json = {
        "map": {
            "nom": "Grotte sombre",
            "largeur": width,
            "etage": index,
            "hauteur": height,
            "tiles": dungeon,
            "spawn": spawn_position
        }
    }
    return dungeon_json

   

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
width = 50
height = 50
maps = []

for i in range(1,2): 
    maps.append(generate_dungeon_with_corridors(width, height,index="E. " + str(i)))

maps.append(generate_dungeon_with_corridors(100, 100,1,10,10,index="Sommet"))
data = {"maps" : maps}
with open("assets/dungeon.json", "w") as json_file:
        json.dump(data, json_file, indent=2)