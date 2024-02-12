import pygame

BLACK = (0, 0, 0)
BLUE = (0, 0, 255, 128)
RED = (242, 38, 19)
GREEN = (178,222,39)
ORANGE = (196,0,51,1)

class InfoBar :
    def __init__(self, joueur, screen):
        self.screen = screen
        self.joueur = joueur
        self.health_bar_length = joueur.stats.health / joueur.stats.max_health * 50
        self.mana_bar_length = joueur.stats.mana / joueur.stats.max_mana * 50
        self.health_bar_rect_max = 50
        self.health_bar_rect = pygame.Rect(190, 12, self.health_bar_length, 15)
        self.health_bar_rect_max = pygame.Rect(190, 12, self.health_bar_rect_max, 15)
        self.fond_health = pygame.Rect(190, 11, 50, 17)
       
    def draw_info(self):
        
        self.health_bar_length = self.joueur.stats.health / self.joueur.stats.max_health * 50
        self.mana_bar_length = self.joueur.stats.mana / self.joueur.stats.max_mana * 50
        self.health_bar_rect_max = 50
        self.health_bar_rect = pygame.Rect(250, 12, self.health_bar_length, 15)
        self.health_bar_rect_max = pygame.Rect(250, 12, self.health_bar_rect_max, 15)
        self.fond_health = pygame.Rect(250, 11, 50, 17)
        
        pygame.draw.rect(self.screen, BLACK, self.fond_health)
        pygame.draw.rect(self.screen, RED, self.health_bar_rect_max)
        pygame.draw.rect(self.screen, GREEN, self.health_bar_rect)
        # Barre de mana
       


        # Texte
        font = pygame.font.Font("assets/super_enjoy/super_font.ttf", 24)
        text = f"  Lv. {self.joueur.stats.level}     Pv :  {self.joueur.stats.health}/{self.joueur.stats.max_health}     " + \
            f"           Mp :   {self.joueur.stats.mana}/{self.joueur.stats.max_mana}"
        text_surface = font.render(text, True, ORANGE)
        self.screen.blit(text_surface, (10, 10))
