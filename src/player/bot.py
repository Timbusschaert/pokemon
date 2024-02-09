from src.player.joueur import Joueur,DirectionEnum
from src.screen.tileset import canPass
import random
class Bot(Joueur):
    def __init__(self, x, y):
        super().__init__(x, y)
     
    def calcul_next_pos(self, joueur,map):
        if (joueur.x - 10 <= self.x or joueur.x + 10 >= self.x )and (joueur.y-10 >= self.y or joueur.y + 10 >= self.y ):
            print("trop loin")
            next_x, next_y = self.generate_next_pos(map)
            self.dx = next_x 
            self.dy = next_y
            print("Prochaine position:", next_x, next_y)
        else :
            print('else')

    def generate_next_pos(self,map):
        x_directions = [-1, 0, 1]
        y_directions = [-1, 0, 1]
        
        print("current pos : " + str(self.x) + str(self.y))
        for x in x_directions:
            for y in y_directions:
                tile = map.get_tile(x+self.x, self.y + y)
                if canPass(tile) and (self.x + x != self.x or self.y + y != self.y):
                    return x, y
        