import pygame
import random
class TilesetEnum:
    COORDINATES = {
        0 : (9,0, True),
        101 : (3,4, True),
        102 : (5,4, True),
        103 : (3,4, True),
        104 : (4,4, True),
        105 : (5,4, True),
        106 : (6, 4,True),

        1 : (4,3,True),
        2 : (11,2,False),
        3 : (10,2,False),
        5 : (1,0,False),
        11 : (2,0,False),
        12 : (5,0,False),
        4 : (7,3,False),
        8 : (12,2,False),   
        9 : (3,0,False),     
        10 : (8,1,False),
        20 : (3,8,True), 
        21 : (7,1,False),
        22 : (9,1,False),
        23 : (4,0,False),
        24 : (7,0,False),
                      
        None : (14,5,False) 
    }
    
    
image_width = 384  # La largeur totale de l'image PNG (en supposant une largeur de 8 tuiles pour l'exemple)
tile_size = 24 # La taille de chaque tuile en pixels
tile_size_= 24


def get_tile_surface(tileset_image, tileset_items,tile_enum):
    value = tile_enum
    if value == 0 :
        value = random.choice([0,101,102,103,104,105,106])
    # Obtenez les coordonnées x et y à partir de l'énumération de la tuile
    tile_x, tile_y , canPass = TilesetEnum.COORDINATES.get(value, (15, 5 , False))
    # Découpage de la tuile à partir du tileset
    if tile_enum == 20 :
        tile_surface = tileset_items.subsurface(pygame.Rect(tile_x * 25.5, tile_y * 24.2, 24, 24))
    else:
        tile_surface = tileset_image.subsurface(pygame.Rect(tile_x * tile_size, tile_y * 24, 24, 24))
    
    return [tile_surface,canPass,tile_enum]

def canPass(tile_enum):
    tile_x, tile_y , canPass = TilesetEnum.COORDINATES.get(tile_enum, (15, 5 , False))
    return canPass