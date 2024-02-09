class Stats :
        def __init__(self):
            self.health = 20 
            self.max_health = 20 
            self.mana = 20 
            self.max_mana = 20
            self.attack = 10
            self.defense = 10 
            self.level = 5 
            self.experience = 0 
            self.max_experience = 50 
        
        def isDead(self):
            return self.health <= 0 
         
            
        