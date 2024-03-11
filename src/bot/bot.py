from src.player.joueur import Joueur,DirectionEnum
from src.screen.tileset import canPass
from src.player.current_action import CurrentAction
import random
class Bot(Joueur):
    def __init__(self,group,x,y,pokemon,map,joueur,bots):
        super().__init__(group,x,y,pokemon,map,bots)
        self.joueur = joueur
        self.can_play = False
     
    def calcul_next_pos(self,choices):
        input = str(random.choice(choices))
        
        if (self.joueur.x - 10 <= self.x or self.joueur.x + 10 >= self.x )and (self.joueur.y-10 >= self.y or self.joueur.y + 10 >= self.y ):
            if self.joueur.x < self.x and '3' in choices:
                input = '3'
            elif self.joueur.x > self.x and '2' in choices:
                input = '2'        
            elif self.joueur.y < self.y and '0' in choices:
                input = '0'
            elif self.joueur.y > self.y and '1' in choices:
                input = '1'
            print(input)
            
        if self.can_attack() != None:
            self.directionAnim = self.can_attack()
            if  self.current_action != CurrentAction.ATTACK:
                self.attack()
        else :
            if input == '0'  :
                self.direction.x = 0
                if  self.direction.x == 0 :                
                    self.direction.y = -self.speed
                self.distanceParcourue += self.speed 
                self.directionAnim = DirectionEnum.UP
                self.current_action = CurrentAction.WALK
                tile = self.map.get_tile(self.x , self.y - 1)
                self.canMove = canPass(tile) and self.bots.has_bot(self.x , self.y - 1) == None 
            elif input == '1' :
                self.direction.x = 0
                if self.direction.y == 0 and self.direction.x == 0 and self.distanceParcourue == 0  :
                    self.direction.y = self.speed
                self.distanceParcourue += self.speed
                self.directionAnim = DirectionEnum.DOWN
                self.current_action = CurrentAction.WALK
                tile = self.map.get_tile(self.x, self.y+1)
                self.canMove = canPass(tile) and self.bots.has_bot(self.x , self.y + 1) == None            
            elif input == '2'  :
                if self.direction.y == 0 and self.distanceParcourue ==0  :
                    self.direction.x = self.speed              
                self.distanceParcourue += self.speed
                self.directionAnim = DirectionEnum.RIGHT 
                self.current_action = CurrentAction.WALK
                tile = self.map.get_tile(self.x + 1 , self.y)
                self.canMove = canPass(tile) and self.bots.has_bot(self.x + 1, self.y ) == None  
            elif input == '3'  :
                if self.direction.y == 0 and self.distanceParcourue ==0 :
                    self.direction.x = - self.speed           
                self.distanceParcourue += self.speed
                self.current_action = CurrentAction.WALK
                self.directionAnim = DirectionEnum.LEFT 
                tile = self.map.get_tile(self.x - 1 , self.y)
                self.canMove = canPass(tile) and self.bots.has_bot(self.x -1, self.y ) == None   
            if self.canMove == False :
               
                if str(input) in choices:
                    choices.remove(input)
            
                self.calcul_next_pos(choices)      

    def update(self):
        if(self.can_play and self.current_action != CurrentAction.HURT):
            choices = ['0','1','2','3']
            self.calcul_next_pos(choices)
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
        
    def change_animation(self):
            if self.current_action == CurrentAction.ATTACK:
                isAttacking = self.image.getIsFinished()
                if isAttacking :
                    self.joueur.takeDamage(10)
                    self.current_action = CurrentAction.IDLE
                    self.can_play = False
            if self.current_action == CurrentAction.HURT:
                isAttacking = self.image.getIsFinished()
                if isAttacking :
                     self.current_action = CurrentAction.IDLE
            elif self.current_action == CurrentAction.FAINTED :
                self.image = self.animationList.getHurtAnimation(self.directionAnim)  
                if self.image.getIsFinished() :
                    self.kill()
                    self.can_play = False
            if self.current_action == CurrentAction.IDLE :
                self.image = self.animationList.getIdleAnimation(self.directionAnim)                              
            if self.current_action == CurrentAction.WALK:
                self.image = self.animationList.getWalkCurrentAnimation(self.directionAnim)
    
    def kill(self):
        self.image.image.fill((0,0,0,0))
        self.image.shadow_image.fill((0,0,0,0))


    def is_in_range(self):
        return (self.joueur.x - 10 <= self.x or self.joueur.x + 10 >= self.x )and ( self.joueur.y-10 >= self.y or self.joueur.y + 10 >= self.y)
       
    def can_attack(self):
        to_return = None
        if self.joueur.y == self.y:
            if(self.joueur.x - self.x == 1):
                to_return = DirectionEnum.RIGHT
            elif self.joueur.x - self.x == - 1:
                to_return = DirectionEnum.LEFT
        elif self.joueur.x == self.x:
            if (self.joueur.y - self.y == 1) :
                to_return = DirectionEnum.DOWN
            elif self.joueur.y - self.y == -1 :
                to_return = DirectionEnum.UP
        return to_return
