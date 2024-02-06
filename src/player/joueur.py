import pygame
import gif_pygame
class DirectionEnum:
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3
    
class Joueur(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        super().__init__()
        self.image = gif_pygame.load("assets/bulbizarre.gif")
        gif_pygame.transform.scale(self.image,[54,48])
        self.rect = self.image.get_rect()
        self.rect.topleft = (205, 199)  # Position initiale du joueur
        self.dx = 0  # Déplacement horizontal
        self.dy = 0  # Déplacement vertical
        self.direction = DirectionEnum.DOWN
        self.x = x
        self.y = y
        
        
    def deplacer(self,map):
            
            if(self.dx > 0):
                self.x -= 1
                if self.direction != DirectionEnum.RIGHT:
                    self.direction = DirectionEnum.RIGHT
            if(self.dx < 0):
                self.x += 1
                if self.direction != DirectionEnum.LEFT:
                    self.direction = DirectionEnum.LEFT
            if(self.dy > 0):
                self.y -= 1
                if self.direction != DirectionEnum.RIGHT:
                    self.direction = DirectionEnum.RIGHT
            if(self.dy < 0):
                self.y += 1
                if self.direction != DirectionEnum.RIGHT:
                    self.direction = DirectionEnum.RIGHT