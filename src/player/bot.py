from src.player.joueur import Joueur,DirectionEnum
from src.screen.tileset import canPass
import random
class Bot(Joueur):
    def __init__(self,group,x,y,map):
        super().__init__(group,x,y,map)
     
    def calcul_next_pos(self, joueur,map):
        if (joueur.x - 10 <= self.x or joueur.x + 10 >= self.x )and (joueur.y-10 >= self.y or joueur.y + 10 >= self.y ):
            next_x, next_y = self.generate_next_pos(self.map)
            self.direction.x = next_x * - 6
            self.direction.y = next_y * - 6
        else :
            print('else')

    def generate_next_pos(self,map):
        x_directions = [-1, 0, 1]
        y_directions = [-1, 0, 1]
        random.shuffle(x_directions)
        random.shuffle(y_directions)
        for x in x_directions:
            for y in y_directions:
                tile = map.get_tile(self.x + x, self.y + y)              
                 
                if canPass(tile) and (self.x + x != self.x and self.y + y != self.y):             
                    return x, y
        return 0,0
        