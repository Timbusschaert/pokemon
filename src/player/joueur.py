import pygame
from src.screen.tileset import canPass
from src.screen.animation import Animation
from src.player.stats import Stats
from src.player.animationsList import AnimationsList
from src.player.directionEnum import DirectionEnum
from src.player.current_action import CurrentAction
class Joueur(pygame.sprite.Sprite):
    
    def __init__(self,group,x,y,pokemon,map):
        super().__init__(group)     
        self.directionAnim = DirectionEnum.DOWN
        self.x = x
        self.y = y
        self.animationList = AnimationsList(pokemon)        
        self.image = self.animationList.getIdleAnimation(self.directionAnim)
        self.rect = self.image.image.get_rect(center = (x*24,y*24))
        self.hitbox = pygame.Rect(self.rect.center, (24, 24))
        self.direction = pygame.math.Vector2()
        self.speed = 4
        self.stats = Stats()
        self.map = map
        self.isAttacking = False
        self.isOnStair= False
        self.distanceParcourue = 0
        self.canMove = True
        self.isAttacked = False
        self.hasPlayed = False

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.distanceParcourue == 0 :
            self.direction.x = 0
            if  self.direction.x == 0 and self.distanceParcourue == 0 :                
                self.direction.y =  -self.speed
            self.distanceParcourue += self.speed 
        elif keys[pygame.K_DOWN] and self.distanceParcourue == 0:
            self.direction.x = 0
            if self.direction.y == 0 and self.direction.x == 0  and self.distanceParcourue == 0 :
                self.direction.y = self.speed
            self.distanceParcourue += self.speed 
        elif self.distanceParcourue == 0:
            self.direction.y = 0       
        else :
            self.distanceParcourue += self.speed 
        if keys[pygame.K_RIGHT] and self.distanceParcourue == 0 :
            if self.direction.y == 0  :
                self.direction.x = self.speed
                
            self.distanceParcourue += self.speed 
        elif keys[pygame.K_LEFT] and self.distanceParcourue == 0 :
            if self.direction.y == 0 :
                self.direction.x = - self.speed           
            self.distanceParcourue += self.speed
        elif self.distanceParcourue == 0:
            self.direction.x = 0   
        elif self.distanceParcourue < (23 * self.speed) - self.speed  :
            self.distanceParcourue += self.speed


        if keys[pygame.K_a]:
            self.attack()

    def update(self):
        self.input()       
        if self.distanceParcourue >= (24 * 2 ) - self.speed:
            self.distanceParcourue = 0
        if(self.direction.x < 0 and self.direction.y == 0):
                tile = self.map.get_tile(self.x -1 , self.y)
                self.canMove = canPass(tile)   
                if self.canMove and self.distanceParcourue == 0:
                    self.x -= 1
                if self.directionAnim != DirectionEnum.LEFT:
                    self.directionAnim = DirectionEnum.LEFT 
        if(self.direction.x > 0 and self.direction.y == 0):
                tile = self.map.get_tile(self.x+1 , self.y)
                self.canMove = canPass(tile)
                if self.canMove and self.distanceParcourue == 0:
                    self.x += 1
                if self.directionAnim != DirectionEnum.RIGHT:
                    self.directionAnim = DirectionEnum.RIGHT
        if(self.direction.y < 0 and self.direction.x == 0):
                tile = self.map.get_tile(self.x , self.y-1)
                self.canMove = canPass(tile)
                if self.canMove and self.distanceParcourue == 0:
                    self.y -= 1
                if self.directionAnim != DirectionEnum.UP:
                    self.directionAnim = DirectionEnum.UP               
        if(self.direction.y > 0 and self.direction.x == 0):
                tile = self.map.get_tile(self.x , self.y + 1 )
                self.canMove = canPass(tile)
                if self.canMove and self.distanceParcourue == 0:
                    self.y += 1
                if self.directionAnim != DirectionEnum.DOWN:
                    self.directionAnim = DirectionEnum.DOWN
        if(self.direction.y > 0 and self.direction.x > 0 ):
                if self.directionAnim != DirectionEnum.DOWN_RIGHT:
                    self.directionAnim = DirectionEnum.DOWN_RIGHT
        if(self.direction.y > 0 and self.direction.x < 0 ):
                if self.directionAnim != DirectionEnum.DOWN_LEFT:
                    self.directionAnim = DirectionEnum.DOWN_LEFT                    
        if(self.direction.y < 0 and self.direction.x > 0 ):                
                if self.directionAnim != DirectionEnum.TOP_RIGHT:
                    self.directionAnim = DirectionEnum.TOP_RIGHT
        if(self.direction.y < 0 and self.direction.x < 0 ):               
                if self.directionAnim != DirectionEnum.TOP_LEFT:
                    self.directionAnim = DirectionEnum.TOP_LEFT           
        if 20 == self.map.get_tile(self.x , self.y):
                self.isOnStair = True
        if self.direction.x == 0 and self.direction.y == 0:
            if self.isAttacking:
                self.isAttacking = not self.image.getIsFinished()
                if self.isAttacking == False : 
                    self.hasPlayed = True 

            elif self.isAttacked:
                self.image = self.animationList.getHurtAnimation(self.directionAnim)
                self.isAttacked = not self.image.getIsFinished()
            else :
                self.image = self.animationList.getIdleAnimation(self.directionAnim)    
        else:
            self.image = self.animationList.getWalkCurrentAnimation(self.directionAnim)  
        if( self.canMove and not self.isOnStair ):
            self.rect.centerx += self.direction.x     
            self.rect.centery += self.direction.y      
        self.hitbox = pygame.Rect(self.rect.center, (24, 24))

    def attack(self):
        self.isAttacking = True
        self.image = self.animationList.getAttackAnimation(self.directionAnim)

        
    def takeDamage(self,damage):
        self.isAttacked = True
        self.image = self.animationList.getHurtAnimation(self.directionAnim)        
    
    def isInAnimation(self):
        self.isAnimated = self.image.current_frame != 0
        if(self.isAnimated):
            self.image = self.animationList.getWalkCurrentAnimation(self.directionAnim)

    def nextDirection(self):
        toReturn = 0
        match self.directionAnim:
            case DirectionEnum.DOWN_RIGHT:
                toReturn = (self.x + 1,self.y + 1 )
            case DirectionEnum.RIGHT:
               toReturn = (self.x + 1,self.y + 1 )
            case DirectionEnum.TOP_RIGHT:
                toReturn = (self.x + 1,self.y + 1 )
            case DirectionEnum.UP:
                toReturn = (self.x + 1,self.y - 1 )
            case DirectionEnum.DOWN:
                toReturn = (self.x ,self.y + 1 )
            case DirectionEnum.DOWN_RIGHT:
                toReturn = (self.x + 1,self.y + 1 )
            case DirectionEnum.LEFT:
               toReturn = (self.x - 1,self.y  )
            case DirectionEnum.TOP_LEFT:
                toReturn = (self.x - 1,self.y - 1 )
            
        return toReturn
