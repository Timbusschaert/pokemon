import pygame
import sys
from src.screen.map import Map
import src.screen.tileset as tileset
from src.player.joueur import Joueur
import json
from src.screen.infobar import InfoBar
from src.player.bot import Bot
import random
from src.screen.camera import CameraGroup
BLACK = (0, 0, 0)
BLUE = (0, 0, 255, 1)
RED = (242, 38, 19)
GREEN = (178,222,39)
ORANGE = (196,0,51,1)
pygame.init()
pygame.mixer.init()
font = pygame.font.Font(None, 50)

# Définition des couleurs
WHITE = (255, 255, 255)
# Taille de la fenêtre et des tuiles
WINDOW_SIZE = (720,720)
LARGEUR_FENETRE = 720
HAUTEUR_FENETRE = 720
TILE_SIZE = 24  # Taille de chaque tuile en pixels
TILE_SIZE_ = 24  # Taille de chaque tuile en pixels
tileset_image = pygame.image.load("assets/map.png")
tileset_items = pygame.image.load("assets/items/items.png")

BLACK = (0, 0, 0)
BLUE = (0, 0, 255, 1)
RED = (242, 38, 19)
GREEN = (178,222,39)
ORANGE = (196,0,51,1)

all_bot = []

def draw_map(surface, map_data, tileset_image,tileset_items,player):
    for y in range(0 , 100):
        for x in range(0 , 100 ):
            tile_enum = map_data.get_tile(x ,y)
            # Calcul des coordonnées dans le tileset           
            # Découpage de la tuile à partir du tileset
            tile_surface, canPass ,tile = tileset.get_tile_surface(tileset_image,tileset_items,tile_enum)
            # Dessin de la tuile sur la surface
            surface.blit(tile_surface, ((x) * TILE_SIZE, (y) * TILE_SIZE ))
                        
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def draw_menu_title(screen):
    menu_font = pygame.font.Font("assets/super_enjoy/super_font.ttf", 40)
    selected_option = 0
    InMenu = True
    pygame.mixer.music.load('assets/musique/title.mp3')
    pygame.mixer.music.play(-1)  # -1 pour jouer en boucle
    pygame.mixer.music.set_volume(0.5)
    bg = pygame.image.load("assets/bg/bg.jpg")
    while InMenu:
        screen.blit(bg,(0,0))
        draw_text("Pokemon donjon mystère", menu_font, BLACK,screen, 20, 50)
        draw_text("Version Timou", menu_font, BLACK,screen, 80, 100)

        # Affichage des options
        option_start_color = RED if selected_option == 0 else BLACK
        option_exit_color = RED if selected_option == 1 else BLACK
        draw_text("Start", menu_font, option_start_color,screen,100, 150)
        draw_text("Exit", menu_font, option_exit_color,screen, 100 , 200)

        pygame.display.update()

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % 2
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % 2
                if event.key == pygame.K_SPACE:
                    if selected_option == 0:  # Start
                        InMenu = False
                        pygame.mixer.music.stop()

                    elif selected_option == 1:  # Exit
                        pygame.quit()
                        quit()

def draw_menu(screen,option_selectionnee):
    pygame.draw.rect(screen, BLUE, (200 , 150, 400,150),30)  # Fond du menu

    font = pygame.font.Font("assets/super_enjoy/super_font.ttf", 36)
    text_info = font.render("Continuer vers l'étage suivant ?", True, BLACK)
    texte_oui = font.render("Avancer", True, BLACK)
    texte_non = font.render("Rester", True, BLACK)
    screen.blit(text_info, (200, 150 ))
    screen.blit(texte_oui, (400, 200 ))
    screen.blit(texte_non, (400, 250 ))

    # Dessiner le sélecteur autour de l'option sélectionnée
    pygame.draw.rect(screen, BLACK, (380 , 210  + 50 * option_selectionnee, 10, 10), 2)

def game_over(screen):
    pygame.mixer.music.stop()
    over = pygame.mixer.Sound("assets/musique/sounds/song205.mp3")
    over.set_volume(0.5)
    over.play()

    fadeout = pygame.Surface((780, 780))
    fadeout = fadeout.convert()
    fontTransition = pygame.font.Font(None, 80)

    for i in range(255):
        fadeout.set_alpha(i)
        dungeon_name = fontTransition.render("Game Over", True, WHITE)
        fadeout.blit(dungeon_name, (200 , 300))
        screen.blit(fadeout, (0, 0))
        pygame.time.delay(10)
        pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

def animationEtage(screen,Text,camera_group,player):
    fadeout = pygame.Surface((780, 780))
    fadeout = fadeout.convert()
    fontTransition = pygame.font.Font(None, 80)

    for i in range(255):
        fadeout.set_alpha(i)
        floor = fontTransition.render(Text, True, WHITE)
        dungeon_name = fontTransition.render("Grotte de l'ennui", True, WHITE)
        fadeout.blit(dungeon_name, (155 , 300))
        fadeout.blit(floor, (300,400))
        screen.blit(fadeout, (0, 0))
        pygame.time.delay(10)
        pygame.display.update()
    
    fadeout = pygame.Surface((780, 780))
    fadeout = fadeout.convert()
    for i in range(10):
        fadeout.set_alpha(255-i*25)     
        camera_group.custom_draw(player)
        screen.blit(fadeout, (0, 0))
        pygame.display.update()

def main():
    option_selectionnee = 0  # 0 pour "Oui", 1 pour "Non"
    etage_index = 0 
    f = open("assets/dungeon.json")
    file = json.load(f)['maps']
    pos = file[etage_index]['map']
    map_data =  Map(100, 100,pos)          
    stair_sound = pygame.mixer.Sound("assets/musique/sounds/song340.mp3")
    stair_sound.set_volume(0.5)
    
    
    # Création de la carte
    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen_map = pygame.Surface((100 * TILE_SIZE, 100 * TILE_SIZE))

    draw_menu_title(screen)

    camera_group = CameraGroup(screen_map)
    all_bot.append(Bot(camera_group,pos['spawn'][0] + 5 , pos['spawn'][1] + 5,"bulbizarre",map_data))
    player = Joueur(camera_group,pos['spawn'][0], pos['spawn'][1],"nosferapti",map_data)
    draw_map(screen_map, map_data, tileset_image,tileset_items,player)
    info_bar = InfoBar(player,screen)
    
    animationEtage(screen,file[etage_index]['map']['etage'],camera_group,player)
    pygame.mixer.music.load("assets/musique/fond.mp3")
    pygame.mixer.music.play(loops=-1)

    pygame.mixer.music.set_volume(1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if player.isOnStair:
                    if event.key == pygame.K_UP:
                        option_selectionnee = (option_selectionnee - 1) % 2
                    elif event.key == pygame.K_DOWN:
                        option_selectionnee = (option_selectionnee + 1) % 2
                    # Gérer l'événement de pression de la barre d'espace
                    elif event.key == pygame.K_SPACE:
                        if option_selectionnee == 0:
                            etage_index+=1
                            if (etage_index == len(file) ):
                                game_over(screen)
                            pygame.mixer.Sound.play(stair_sound)
                            pos = file[etage_index]['map']
                            map_data =  Map(100, 100,pos)   
                            camera_group = CameraGroup(screen_map)
                            player = Joueur(camera_group,pos['spawn'][0], pos['spawn'][1],"nosferapti",map_data)
                            draw_map(screen_map, map_data, tileset_image,tileset_items,player)
                            animationEtage(screen,file[etage_index]['map']['etage'],camera_group,player)
                            

                        else:
                            player.isOnStair = False
            
        screen.fill('#71ddee')
        camera_group.custom_draw(player)
        
        if player.isAttacking:
            for bot in all_bot:
                
                if player.nextDirection()[0] == bot.x and  player.nextDirection()[1] == bot.y:
                    bot.takeDamage(10)

        player.image.update()
        info_bar.draw_info()
        camera_group.update()   
        if(player.isOnStair):
            draw_menu(screen,option_selectionnee)
        pygame.display.update()
        
if __name__ == "__main__":
    main()