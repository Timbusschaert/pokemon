from src.player.joueur import Joueur,DirectionEnum
from src.screen.tileset import canPass
from src.player.current_action import CurrentAction
import random
class Bot(Joueur):
    def __init__(self,group,x,y,pokemon,map,joueur):
        super().__init__(group,x,y,pokemon,map)
        self.joueur = joueur
        self.can_play = False
     
    def calcul_next_pos(self):
        input = random.choice([0,1,2,3])

        if (self.joueur.x - 10 <= self.x or self.joueur.x + 10 >= self.x )and (self.joueur.y-10 >= self.y or self.joueur.y + 10 >= self.y ):
            if self.joueur.x < self.x:
                input = 3
            elif self.joueur.x > self.x:
                input = 2
        
            elif self.joueur.y < self.y:
                input = 0
            elif self.joueur.y > self.y:
                input = 1

        if self.can_attack():
            print('attack')
            if  self.current_action != CurrentAction.ATTACK:
                self.attack()
                self.joueur.takeDamage(2)
        else :
            if input == 0  :
                self.direction.x = 0
                if  self.direction.x == 0 :                
                    self.direction.y = -self.speed
                self.distanceParcourue += self.speed 
                self.directionAnim = DirectionEnum.UP
                self.current_action = CurrentAction.WALK
                tile = self.map.get_tile(self.x , self.y - 1)
                self.canMove = canPass(tile)   
            elif input == 1 :
                self.direction.x = 0
                if self.direction.y == 0 and self.direction.x == 0  :
                    self.direction.y = self.speed
                self.distanceParcourue += self.speed
                self.directionAnim = DirectionEnum.DOWN
                self.current_action = CurrentAction.WALK
                tile = self.map.get_tile(self.x, self.y+1)
                self.canMove = canPass(tile)             
            elif input == 2  :
                if self.direction.y == 0  :
                    self.direction.x = self.speed              
                self.distanceParcourue += self.speed
                self.directionAnim = DirectionEnum.RIGHT 
                self.current_action = CurrentAction.WALK
                tile = self.map.get_tile(self.x + 1 , self.y)
                self.canMove = canPass(tile)   
            elif input == 3  :
                if self.direction.y == 0 :
                    self.direction.x = - self.speed           
                self.distanceParcourue += self.speed
                self.current_action = CurrentAction.WALK
                self.directionAnim = DirectionEnum.LEFT 
                tile = self.map.get_tile(self.x - 1 , self.y)
                self.canMove = canPass(tile)          

    def update(self):
        if(self.can_play):
            self.calcul_next_pos()
        self.change_animation()

        if self.distanceParcourue > 24 * 2 :
            self.distanceParcourue = 0
            self.can_play = False
            self.go_to_next_position()
            self.direction.x = 0
            self.direction.y = 0
        elif self.distanceParcourue != 0 and self.canMove:
            self.distanceParcourue += self.speed
            self.rect.centerx += self.direction.x     
            self.rect.centery += self.direction.y
        
    
    def is_in_range(self):
        return (self.joueur.x - 10 <= self.x or self.joueur.x + 10 >= self.x )and ( self.joueur.y-10 >= self.y or self.joueur.y + 10 >= self.y)
       
    def can_attack(self):

        if abs(self.joueur.x - self.x) == 1 and self.joueur.y == self.y:
            print(self.joueur.x,self.x)
            return True
        elif abs(self.joueur.y - self.y) == 1 and self.joueur.x == self.x:
            return True
        else:
            return False
