import pygame
import sys
from map import Map
import tileset
from joueur import Joueur

# Définition des couleurs
WHITE = (255, 255, 255)

# Taille de la fenêtre et des tuiles
WINDOW_SIZE = (480, 480)
TILE_SIZE = 24  # Taille de chaque tuile en pixels

# Chargement de l'image du tileset
tileset_image = pygame.image.load("assets/map.png")
# Création de la carte
map_data = Map(100, 100)

# ... Ajoutez d'autres tuiles

def draw_map(surface, map_data, tileset_image):
    for y in range(20):
        for x in range(20):
            tile_enum = map_data.get_tile(joueur.x + x  ,joueur.y + y)
            # Calcul des coordonnées dans le tileset
            
            # Découpage de la tuile à partir du tileset
            tile_surface, canPass = tileset.get_tile_surface(tileset_image,tile_enum)
            tuile_upscaled = pygame.transform.scale(tile_surface, (48, 48))
           
            # Dessin de la tuile sur la surface
            surface.blit(tuile_upscaled, ( x * TILE_SIZE  , y * TILE_SIZE  ))
                                   
joueur = Joueur()
def main():
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Affichage de la carte")

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Déplacement du joueur

                if event.key == pygame.K_UP and joueur.y > 0:
                    tile_enum = map_data.get_tile(joueur.x ,joueur.y - 1)
                    
                    tile = tileset.get_tile_surface(tileset_image,tile_enum)
                    print(tile)
                    joueur.dy = -5 
                elif event.key == pygame.K_DOWN and joueur.x < 100 - TILE_SIZE:
                    tile_enum = map_data.get_tile(joueur.x ,joueur.y + 1)
                    tile = tileset.get_tile_surface(tileset_image,tile_enum)
                    print(tile)

                    joueur.dy = 5 
                elif event.key == pygame.K_LEFT and joueur.x > 0:
                    tile_enum = map_data.get_tile(joueur.x - 1 ,joueur.y )
                    canPass = tileset.get_tile_surface(tileset_image,tile_enum)
                    print(canPass)
                   
                    joueur.dx = - 5
                elif event.key == pygame.K_RIGHT and joueur.rect.x < 400 - TILE_SIZE:
                    tile_enum = map_data.get_tile(joueur.x +1 ,joueur.y - 1)
                    canPass = tileset.get_tile_surface(tileset_image,tile_enum)
                
                    joueur.dx = 5
            elif event.type == pygame.KEYUP :
                if event.key == pygame.K_UP :
                    joueur.dy = 0
                elif event.key == pygame.K_DOWN :
                    joueur.dy = 0
                elif event.key == pygame.K_LEFT :
                    joueur.dx = 0
                elif event.key == pygame.K_RIGHT :
                    joueur.dx = 0
        joueur.deplacer()

        draw_map(screen, map_data, tileset_image)
        joueur.image.render(screen, (joueur.rect.x, joueur.rect.y))

        pygame.display.update()

        clock.tick(30)

if __name__ == "__main__":
    main()