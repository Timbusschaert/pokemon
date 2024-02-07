import pygame
import sys
from src.screen.map import Map
import src.screen.tileset as tileset
from src.player.joueur import Joueur
import json

# Définition des couleurs
WHITE = (255, 255, 255)
# Taille de la fenêtre et des tuiles
WINDOW_SIZE = (480, 480)
TILE_SIZE = 24  # Taille de chaque tuile en pixels
TILE_SIZE_ = 24  # Taille de chaque tuile en pixels
tileset_image = pygame.image.load("assets/map.png")
map_data = Map(100, 100)

def draw_map(surface, map_data, tileset_image ,joueur):
    for y in range(-10 , 10):
        for x in range(-10 , 10 ):
            tile_enum = map_data.get_tile(joueur.x + x  ,joueur.y + y)
            # Calcul des coordonnées dans le tileset
            
            # Découpage de la tuile à partir du tileset
            tile_surface, canPass ,tile = tileset.get_tile_surface(tileset_image,tile_enum)
            # Dessin de la tuile sur la surface
            surface.blit(tile_surface, ( (x + 10 ) * TILE_SIZE   , (y + 10)  * TILE_SIZE ))

def main():
    pygame.init()
    pygame.mixer.init()
    
    f = open("assets/map.json")
    pos = json.load(f)['map']['spawn']                   
    joueur = Joueur(pos[0],pos[1])
    music = pygame.mixer.music.load("assets/musique/fond.mp3")
    pygame.mixer.music.set_volume(1)
    #pygame.mixer.music.play(loops=-1)
    # Création de la carte
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Affichage de la carte")

    clock = pygame.time.Clock()

    while True:
        tile = ("",True,"")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Déplacement du joueur
                if event.key == pygame.K_UP :               
                    joueur.dy = 1 
                elif event.key == pygame.K_DOWN:                  
                    joueur.dy = -1                 
                elif event.key == pygame.K_LEFT:  
                    joueur.dx = 1 
                elif event.key == pygame.K_RIGHT :
                    joueur.dx = -1
            elif event.type == pygame.KEYUP :
                if event.key == pygame.K_UP :
                    joueur.dy = 0
                elif event.key == pygame.K_DOWN :
                    joueur.dy = 0
                elif event.key == pygame.K_LEFT :
                    joueur.dx = 0
                elif event.key == pygame.K_RIGHT :
                    joueur.dx = 0
        
        joueur.deplacer(map_data)
        joueur.image.update()
        draw_map(screen, map_data, tileset_image,joueur)
        joueur.image.draw(screen, (joueur.rect.x+10, joueur.rect.y+10))

        pygame.display.flip()

        clock.tick(10)

if __name__ == "__main__":
    main()