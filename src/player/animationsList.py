from src.screen.animation import Animation
import xml.etree.ElementTree as ET
from src.player.directionEnum import DirectionEnum
import pygame
class AnimationsList():
    def __init__(self,pokemon):
        self.pokemon = pokemon
        self.idle = dict()
        self.initIdle()
        self.walk=dict()
        self.initWalk()
        self.attack = dict()
        self.initAttack()
        self.hurt = dict()
        self.initHurt()
        self.faint = dict()
        self.initFaint()
       

    def initWalk(self):
        image = pygame.image.load("assets/"+str(self.pokemon)+"/Walk-Anim.png")
        tree = ET.parse("assets/"+str(self.pokemon)+"/AnimData.xml")
        shadow = pygame.image.load("assets/"+str(self.pokemon)+"/Walk-Shadow.png")

        self.walk[0] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.DOWN,7,True)
        self.walk[1] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.DOWN_RIGHT,7,True)
        self.walk[2] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.RIGHT,7,True)
        self.walk[3] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.TOP_RIGHT,7,True)
        self.walk[4] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.UP,7,True)
        self.walk[5] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.TOP_LEFT,3,True)
        self.walk[6] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.LEFT,5,True)
        self.walk[7] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.DOWN_LEFT,3,True)

    def initAttack(self):
        image = pygame.image.load("assets/"+str(self.pokemon)+"/Attack-Anim.png")
        tree = ET.parse("assets/"+str(self.pokemon)+"/AnimData-Attack.xml")
        shadow = pygame.image.load("assets/"+str(self.pokemon)+"/Attack-Shadow.png")

        self.attack[0] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.DOWN,10,False)
        self.attack[1] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.DOWN_RIGHT,10,False)
        self.attack[2] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.RIGHT,10,False)
        self.attack[3] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.TOP_RIGHT,10,False)
        self.attack[4] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.UP,10,False)
        self.attack[5] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.TOP_LEFT,10,False)
        self.attack[6] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.LEFT,10,False)
        self.attack[7] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.DOWN_LEFT,10,False)

    def initIdle(self):
        image = pygame.image.load("assets/"+str(self.pokemon)+"/Idle-Anim.png")
        tree = ET.parse("assets/"+str(self.pokemon)+"/AnimData-Idle.xml")
        shadow = pygame.image.load("assets/"+str(self.pokemon)+"/Idle-Shadow.png")

        self.idle[0] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.DOWN,10,True)
        self.idle[1] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.DOWN_RIGHT,10,True)
        self.idle[2] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.RIGHT,10,True)
        self.idle[3] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.TOP_RIGHT,10,True)
        self.idle[4] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.UP,10,True)
        self.idle[5] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.TOP_LEFT,10,True)
        self.idle[6] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.LEFT,10,True)
        self.idle[7] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.DOWN_LEFT,10,True)

    def initHurt(self):
        image = pygame.image.load("assets/"+str(self.pokemon)+"/Hurt-Anim.png")
        tree = ET.parse("assets/"+str(self.pokemon)+"/AnimData-Hurt.xml")
        shadow = pygame.image.load("assets/"+str(self.pokemon)+"/Hurt-Shadow.png")

        self.hurt[0] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.DOWN,10,False)
        self.hurt[1] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.DOWN_RIGHT,10,False)
        self.hurt[2] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.RIGHT,10,False)
        self.hurt[3] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.TOP_RIGHT,10,False)
        self.hurt[4] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.UP,10,False)
        self.hurt[5] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.TOP_LEFT,10,False)
        self.hurt[6] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.LEFT,10,False)
        self.hurt[7] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.DOWN_LEFT,10,False)
    
    def initFaint(self):
        image = pygame.image.load("assets/"+str(self.pokemon)+"/Fainted-Anim.png")
        tree = ET.parse("assets/"+str(self.pokemon)+"/AnimData-Faint.xml")
        shadow = pygame.image.load("assets/"+str(self.pokemon)+"/Fainted-Shadow.png")

        self.faint[0] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.DOWN,10,False)
        self.faint[1] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.DOWN_RIGHT,10,False)
        self.faint[2] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.RIGHT,10,False)
        self.faint[3] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.TOP_RIGHT,10,False)
        self.faint[4] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.UP,10,False)
        self.faint[5] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.TOP_LEFT,10,False)
        self.faint[6] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.LEFT,10,False)
        self.faint[7] = Animation(image,shadow,self.pokemon,tree,DirectionEnum.DOWN_LEFT,10,False)

        
    def getWalkCurrentAnimation(self,enumDirection):
        return self.walk.get(enumDirection)
    
    def getAttackAnimation(self,enumDirection):
        self.attack.get(enumDirection).startAnimation()
        return self.attack.get(enumDirection)
    
    def getIdleAnimation(self,enumDirection):
        return self.idle.get(enumDirection)
    
    def getHurtAnimation(self,enumDirection):
        self.hurt.get(enumDirection).startAnimation()
        return self.hurt.get(enumDirection)

    def getFaintAnimation(self,enumDirection):
        self.faint.get(enumDirection).startAnimation()
        return self.faint.get(enumDirection)
