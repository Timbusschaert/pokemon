from tileset import TilesetEnum 
import json
class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        f = open("assets/map.json")
        self.tiles = json.load(f)['map']['tiles']

    def set_tile(self, x, y, tile_enum):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.tiles[y][x] = tile_enum

    def get_tile(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]
        return None