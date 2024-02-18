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
        if(self.can_play):
            #self.calcul_next_pos()
            if  self.current_action != CurrentAction.ATTACK: 
                self.attack()
            
        self.change_animation()
    
            
       
