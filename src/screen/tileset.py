import pygame
import random
class TilesetEnum:
    COORDINATES = {
        0 : (7,1, True),
        1 : (7,2,True),
        2 : (13,3,False),
        3 : (15,3,False),
        5 : (14,5,False),
        11 : (6,0,False),
        12 : (6,0,False),
        8 : (14,3,False),
        4 : (4,3,False),   
        10 : (2,1,False),     
        9 : (2,1,False),
        20 : (3,8,True),                                   
        None : (14,5,False) 
    }
    
    
image_width = 384  # La largeur totale de l'image PNG (en supposant une largeur de 8 tuiles pour l'exemple)
tile_size = 24 # La taille de chaque tuile en pixels
tile_size_= 24


def get_tile_surface(tileset_image, tileset_items,tile_enum):
    value = tile_enum
    if tile_enum == 0 :
        value = random.choice([0,1])
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