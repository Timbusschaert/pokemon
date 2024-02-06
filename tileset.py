import pygame
class TilesetEnum:
    COORDINATES = {
        3: (0, 0 , False),
        5: (3, 0 , False),
        0: (0,4,True),
        1: (2,6,True),
        None : (0,0,False)
    }
    
    
image_width = 384  # La largeur totale de l'image PNG (en supposant une largeur de 8 tuiles pour l'exemple)
tile_size = 34 # La taille de chaque tuile en pixels



def get_tile_surface(tileset_image, tile_enum):
    # Obtenez les coordonnées x et y à partir de l'énumération de la tuile
    tile_x, tile_y , canPass = TilesetEnum.COORDINATES.get(tile_enum, (0, 0 , False))
    # Découpage de la tuile à partir du tileset
    tile_surface = tileset_image.subsurface(pygame.Rect(tile_x * tile_size, tile_y * tile_size, tile_size, tile_size))

    return tile_surface,canPass
