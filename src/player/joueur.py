import pygame
import gif_pygame
from src.screen.tileset import canPass
from src.screen.animation import Animation
class DirectionEnum:
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3
    
class Joueur(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        super().__init__()
        # Position initiale du joueur
        self.dx = 0  # Déplacement horizontal
        self.dy = 0  # Déplacement vertical
        self.direction = DirectionEnum.DOWN
        self.x = x
        self.y = y
        self.listAnimation = dict()
        self.listAnimation["DOWN"] = Animation("assets/bulbizarre/Walk-Anim-Down.png","assets/bulbizarre/AnimData.xml")
        self.listAnimation["UP"] = Animation("assets/bulbizarre/Walk-Anim-Up.png","assets/bulbizarre/AnimData.xml")
        self.listAnimation["RIGHT"] = Animation("assets/bulbizarre/Walk-Anim-Right.png","assets/bulbizarre/AnimData.xml")
        self.listAnimation["LEFT"] = Animation("assets/bulbizarre/Walk-Anim-Left.png","assets/bulbizarre/AnimData.xml")
        self.image = self.listAnimation.get("DOWN")
        self.rect = self.image.image.get_rect()
        self.rect.topleft = (205, 199)
        
    def deplacer(self,map):
            moveX = -1 if self.dx > 0 else 1 
            moveY = -1 if self.dy > 0 else 1
            tile = map.get_tile(self.x + moveX , self.y + moveY)
            canMove = canPass(tile)
            print(canMove)
            if(self.dx > 0):
                if canMove :
                    self.x -= 1
                if self.direction != DirectionEnum.RIGHT:
                    self.direction = DirectionEnum.RIGHT
                    self.image = self.listAnimation.get("LEFT")
            if(self.dx < 0):
                if canMove :
                    self.x += 1
                if self.direction != DirectionEnum.LEFT:
                    self.direction = DirectionEnum.LEFT
                self.image = self.listAnimation.get("RIGHT")

            if(self.dy > 0):
                if canMove :
                    self.y -= 1
                if self.direction != DirectionEnum.UP:
                    self.direction = DirectionEnum.UP
                    self.image = self.listAnimation.get("UP")

            if(self.dy < 0):
                if canPass :
                    self.y += 1

                if self.direction != DirectionEnum.DOWN:
                    self.direction = DirectionEnum.DOWN
                    self.image = self.listAnimation.get("DOWN")

