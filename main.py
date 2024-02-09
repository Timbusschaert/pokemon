import pygame
import sys
from src.screen.map import Map
import src.screen.tileset as tileset
from src.player.joueur import Joueur
import json
from src.screen.infobar import InfoBar
from src.player.bot import Bot
import random
pygame.init()
pygame.mixer.init()
font = pygame.font.Font(None, 50)

# Définition des couleurs
WHITE = (255, 255, 255)
# Taille de la fenêtre et des tuiles
WINDOW_SIZE = (480, 480)
TILE_SIZE = 24  # Taille de chaque tuile en pixels
TILE_SIZE_ = 24  # Taille de chaque tuile en pixels
tileset_image = pygame.image.load("assets/map.png")
map_data = Map(100, 100)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255, 128)
RED = (242, 38, 19)
GREEN = (178,222,39)
ORANGE = (196,0,51,1)

def draw_map(surface, map_data, tileset_image ,joueur,bot):
    botPos = (0,0)
    for y in range(-10 , 10):
        for x in range(-10 , 10 ):
            tile_enum = map_data.get_tile(joueur.x + x  ,joueur.y + y)
            # Calcul des coordonnées dans le tileset           
            # Découpage de la tuile à partir du tileset
           

            tile_surface, canPass ,tile = tileset.get_tile_surface(tileset_image,tile_enum)
            # Dessin de la tuile sur la surface
            surface.blit(tile_surface, ( (x + 10 ) * TILE_SIZE   , (y + 10)  * TILE_SIZE ))
            if bot.x == joueur.x + x  and bot.y ==  joueur.y + y:
                botPos =( (x + 10 ) * TILE_SIZE   , (y + 10)  * TILE_SIZE )
                
    bot.image.draw(surface, botPos)
    
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    
def draw_menu(screen):
    font_menu = pygame.font.Font(None, 30)

    pygame.draw.rect(screen, BLUE, (300, 50, 1600, 250))  # Rectangle bleu transparent
    draw_text("Statut", font_menu, BLACK, screen, 360 , 70)
    draw_text("Capacité", font_menu, BLACK, screen, 360, 120)
    draw_text("Inventaire", font_menu, BLACK, screen, 360 ,280)

def game_over(screen):
    pygame.draw.rect(screen, BLACK, (0,0 , 480, 480))  # Rectangle bleu transparent
    draw_text("GAME OVER", font, WHITE, screen, 240 , 200)

def main():
    
    f = open("assets/map.json")
    pos = json.load(f)['map']['spawn']                   
    joueur = Joueur(pos[0],pos[1])
    bot = Bot(pos[0] +2, pos[1])
    music = pygame.mixer.music.load("assets/musique/fond.mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(loops=-1)
    # Création de la carte
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Affichage de la carte")
    info_bar = InfoBar(joueur,screen)
    clock = pygame.time.Clock()
    menu_open = False
    while True:
        tile = ("",True,"")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Déplacement du joueur
                bot.calcul_next_pos(joueur,map_data)
                
                if event.key == pygame.K_UP :               
                    joueur.dy = 1
                elif event.key == pygame.K_DOWN:                  
                    joueur.dy = -1
                elif event.key == pygame.K_LEFT:  
                    joueur.dx = 1
                elif event.key == pygame.K_RIGHT :
                    joueur.dx = -1
                elif event.key == pygame.K_a :
                    menu_open = not menu_open
                elif event.key == pygame.K_SPACE:
                    joueur.stats.health -= 1
            elif event.type == pygame.KEYUP :
                if event.key == pygame.K_UP :
                    joueur.dy = 0
                    bot.dy = 0
                    bot.dx = 0  
                elif event.key == pygame.K_DOWN :
                    joueur.dy = 0
                    bot.dy = 0
                    bot.dx = 0  
                elif event.key == pygame.K_LEFT :
                    joueur.dx = 0
                    bot.dx = 0
                    bot.dy = 0  
                elif event.key == pygame.K_RIGHT :
                    joueur.dx = 0
                    bot.dx = 0
                    bot.dy = 0  
        joueur.deplacer(map_data)
              
        bot.deplacer(map_data)

        joueur.image.update()
        bot.image.update()
        
        draw_map(screen, map_data, tileset_image,joueur,bot)
        
        info_bar.draw_info()
        
        joueur.image.draw(screen, (joueur.rect.x+10, joueur.rect.y+10))
        
        if menu_open:
            draw_menu(screen)
            
        if joueur.stats.isDead() :
            game_over(screen)
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()