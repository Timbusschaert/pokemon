from src.player.joueur import Joueur,DirectionEnum
from src.screen.tileset import canPass
import random
class Bot(Joueur):
    def __init__(self,group,x,y,pokemon,map,joueur):
        super().__init__(group,x,y,pokemon,map)
        self.joueur = joueur
        self.input = None
     
    def calcul_next_pos(self):
        self.input = random.choice([0,1,2,3])
        if (self.joueur.x - 10 <= self.x or self.joueur.x + 10 >= self.x )and (self.joueur.y-10 >= self.y or self.joueur.y + 10 >= self.y  and self.input == None):
            self.input = random.choice([0,1,2,3])
        else :
            print('else')
        if self.input == 0  and self.distanceParcourue == 0 :
            self.direction.x = 0
            if  self.direction.x == 0 and self.distanceParcourue == 0 :                
                self.direction.y =  -self.speed
            self.distanceParcourue += self.speed 
        elif self.input == 1 and self.distanceParcourue == 0:
            self.direction.x = 0
            if self.direction.y == 0 and self.direction.x == 0  and self.distanceParcourue == 0 :
                self.direction.y = self.speed
            self.distanceParcourue += self.speed 
        if self.distanceParcourue == 0:
            self.direction.y = 0       

        if self.input == 2 and self.distanceParcourue == 0 :
            if self.direction.y == 0  :
                self.direction.x = self.speed    
            self.distanceParcourue += self.speed 
        elif self.input == 3 and self.distanceParcourue == 0 :
            if self.direction.y == 0 :
                self.direction.x = - self.speed           
            self.distanceParcourue += self.speed    
        if self.distanceParcourue == 0:
            self.direction.x = 0 
        
        if input == None :
            self.distanceParcourue += self.speed
    def update(self):
        if(self.joueur.hasPlayed == True and self.input == None):
            self.calcul_next_pos()
        print(self.x,self.y)
        if self.distanceParcourue >= (24 * 2 ) - self.speed:
            self.distanceParcourue = 0
            self.direction.x = 0   
            self.direction.y = 0   
            self.joueur.hasPlayed = False
            self.input = None
        elif (self.canMove and self.distanceParcourue != 0 ):
            self.distanceParcourue += self.speed
            self.rect.centerx += self.direction.x     
            self.rect.centery += self.direction.y      
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
        
        if self.direction.x == 0 and self.direction.y == 0:
            if self.isAttacking:
                self.isAttacking = not self.image.getIsFinished()
            elif self.isAttacked:
                self.image = self.animationList.getHurtAnimation(self.directionAnim)
                self.isAttacked = not self.image.getIsFinished()
            else :
                self.image = self.animationList.getIdleAnimation(self.directionAnim)    
        else:
            self.image = self.animationList.getWalkCurrentAnimation(self.directionAnim) 
        
        
