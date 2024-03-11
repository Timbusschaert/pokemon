from src.bot.bot_queue import BotQueue
class BotList:
    def __init__(self):
        self.bots = []  # A list to store bots in queue
        self.bot_queue = BotQueue()

    def add_bot(self, bot,):
        self.bots.append(bot)  # Add a bot to the queue
    
    def check_health_bot(self):
        for bot in self.bots :
            if bot.stats.health <= 0 :
                print('dead')
        
    
    def has_bot(self,x,y):
        toReturn = None
        for bot in self.bots :
            if bot.x == x and bot.y == y :
                toReturn =  bot
        
        return toReturn
    def update_bot(self):
        for bot in self.bots :
            bot.image.update()
            
    def play_turn_bot(self,player):
        if not player.can_play and self.bot_queue.is_empty() and self.bot_queue.current_bot == None:
            for bot in self.bots :
                if bot.is_in_range():
                    self.bot_queue.add_bot(bot)
            if (not self.bot_queue.is_empty()):
                self.bot_queue.next_bot().can_play = True

        if(not player.can_play):
            if self.bot_queue.current_bot != None :
                can_play = self.bot_queue.current_bot.can_play
                if can_play == False :
                        newbot = self.bot_queue.next_bot()
                        if newbot == None :
                            self.bot_queue.current_bot = None
                            player.can_play = True
                        else : 
                            newbot.can_play = True
            else :
                player.can_play = True