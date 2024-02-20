import pygame
from src.screen.tileset import canPass
from src.screen.animation import Animation
from src.player.stats import Stats
from src.player.animationsList import AnimationsList
from src.player.directionEnum import DirectionEnum
from src.player.current_action import CurrentAction
class Joueur(pygame.sprite.Sprite):
    
    def __init__(self,group,x,y,pokemon,map,bots):
        super().__init__(group)     
        self.x = x
        self.y = y
        self.bots = bots
        self.animationList = AnimationsList(pokemon)
        self.directionAnim = DirectionEnum.DOWN
      
        self.image = self.animationList.getIdleAnimation(self.directionAnim)
        self.rect = self.image.image.get_rect(center = (x*24,y*24))
        self.current_action = CurrentAction.IDLE
        self.direction = pygame.math.Vector2()
        self.speed = 2
        
        self.stats = Stats()
        self.map = map
        self.canMove = False
        self.isOnStair= False
        self.can_play = True
        self.distanceParcourue = 0
          
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] :
            tile = self.map.get_tile(self.x , self.y - 1)
            self.canMove = canPass(tile) and self.bots.has_bot(self.x , self.y - 1) == None
            if  self.direction.x == 0 and self.canMove and self.distanceParcourue == 0:                
                self.direction.y = -self.speed
                self.distanceParcourue += self.speed
                self.current_action = CurrentAction.WALK
                self.directionAnim = DirectionEnum.UP 

            elif not self.canMove :
                self.directionAnim = DirectionEnum.UP
                    
        elif keys[pygame.K_DOWN] :
            tile = self.map.get_tile(self.x , self.y + 1)
            self.canMove = canPass(tile) and  self.bots.has_bot(self.x , self.y + 1) == None
            self.direction.x = 0
            if self.direction.x == 0 and self.canMove and self.direction.y == 0 and self.distanceParcourue == 0 :
                self.direction.y = self.speed
                self.distanceParcourue += self.speed
                self.current_action = CurrentAction.WALK
                self.directionAnim = DirectionEnum.DOWN

            elif not self.canMove :
                self.directionAnim = DirectionEnum.DOWN
                         
        elif keys[pygame.K_RIGHT]  :
            tile = self.map.get_tile(self.x + 1 , self.y)
            self.canMove = canPass(tile) and self.bots.has_bot(self.x +1 , self.y) == None
            if self.direction.y == 0  and self.canMove  and self.distanceParcourue == 0:
                self.direction.x = self.speed              
                self.distanceParcourue += self.speed
                self.current_action = CurrentAction.WALK
                self.directionAnim = DirectionEnum.RIGHT 

            elif not self.canMove :
                self.directionAnim = DirectionEnum.RIGHT 
           
        elif keys[pygame.K_LEFT]  :
            tile = self.map.get_tile(self.x - 1 , self.y)
            self.canMove = canPass(tile) and self.bots.has_bot(self.x -1 , self.y ) == None
            if self.direction.y == 0 and self.canMove  and self.distanceParcourue == 0:
                self.direction.x = - self.speed           
                self.distanceParcourue += self.speed
                self.current_action = CurrentAction.WALK
                self.directionAnim = DirectionEnum.LEFT 

            elif not self.canMove :
                self.directionAnim = DirectionEnum.LEFT 
            
        if keys[pygame.K_a]:
            self.attack()
            

    def update(self):
        if(self.can_play and self.distanceParcourue == 0):
            
                self.input()
        if self.distanceParcourue > (24) and (self.can_play ):
            self.distanceParcourue = 0
            self.can_play = False 
            self.go_to_next_position()
            self.direction.x = 0
            self.direction.y = 0

        elif self.distanceParcourue != 0 and self.canMove:
            self.distanceParcourue += self.speed
            self.rect.centerx += self.direction.x     
            self.rect.centery += self.direction.y

        self.is_on_stair()  
        self.change_animation()
        
    def change_animation(self):
            if self.current_action == CurrentAction.ATTACK:
                isAttacking = self.image.getIsFinished()
                if isAttacking :
                    direction = self.nextDirection()
                    bot_to_attack = self.bots.has_bot(direction[0],direction[1])
                    if bot_to_attack != None:
                        bot_to_attack.takeDamage(20)
                    
                    self.current_action = CurrentAction.IDLE
                    self.can_play = False
            elif self.current_action == CurrentAction.HURT:
                isAttacking = self.image.getIsFinished()
                if isAttacking :
                     self.current_action = CurrentAction.IDLE
            elif self.current_action == CurrentAction.IDLE :
                self.image = self.animationList.getIdleAnimation(self.directionAnim)                              
            elif self.current_action == CurrentAction.WALK:
                self.image = self.animationList.getWalkCurrentAnimation(self.directionAnim)
                if self.image.getIsFinished() :
                  self.image = self.animationList.getIdleAnimation(self.directionAnim)  

          
    def is_on_stair(self):
        if 20 == self.map.get_tile(self.x , self.y):
            self.isOnStair = True

    def go_to_next_position(self):
        if(self.direction.x < 0 and self.direction.y == 0):
               
                if self.canMove and self.distanceParcourue == 0:
                    self.x -= 1
               
        if(self.direction.x > 0 and self.direction.y == 0):
                tile = self.map.get_tile(self.x+1 , self.y)
                self.canMove = canPass(tile)
                if self.canMove and self.distanceParcourue == 0:
                    self.x += 1
               
        if(self.direction.y < 0 and self.direction.x == 0):
                tile = self.map.get_tile(self.x , self.y-1)
                self.canMove = canPass(tile)
                if self.canMove and self.distanceParcourue == 0:
                    self.y -= 1
                             
        if(self.direction.y > 0 and self.direction.x == 0):
                tile = self.map.get_tile(self.x , self.y + 1 )
                self.canMove = canPass(tile) 
                if self.canMove and self.distanceParcourue == 0:
                    self.y += 1
        self.can_play = False       
    
        
       
          
            
    def attack(self):
        self.current_action = CurrentAction.ATTACK
        self.image = self.animationList.getAttackAnimation(self.directionAnim)
        
    def takeDamage(self,damage):
        self.isAttacked = True
        self.stats.health -= damage
        font = pygame.font.Font(None, 36)
        self.current_action = CurrentAction.HURT
        self.image = self.animationList.getHurtAnimation(self.directionAnim)

        text = font.render("-2", True, (255, 255, 255))
    

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
                toReturn = (self.x,self.y - 1 )
            case DirectionEnum.DOWN:
                toReturn = (self.x ,self.y + 1 )
            case DirectionEnum.DOWN_RIGHT:
                toReturn = (self.x + 1,self.y + 1 )
            case DirectionEnum.LEFT:
               toReturn = (self.x - 1 ,self.y  )
            case DirectionEnum.TOP_LEFT:
                toReturn = (self.x - 1 , self.y - 1)           
        return toReturn
    