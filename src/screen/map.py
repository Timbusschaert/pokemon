from src.screen.tileset import TilesetEnum 
class Map:
    def __init__(self, width, height,jsonFile):
        self.width = width
        self.height = height
        self.tiles = jsonFile['tiles']

    def set_tile(self, x, y, tile_enum):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.tiles[y][x] = tile_enum

    def get_tile(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]
        return None