class BotQueue:
    def __init__(self):
        self.queue = []  # A list to store bots in queue
        self.current_bot = None
    def add_bot(self, bot):
        self.queue.append(bot)  # Add a bot to the queue

    def next_bot(self):
        if self.queue:
            self.current_bot = self.queue.pop(0)
            return self.current_bot  # Return and remove the next bot from the queue
        else:
            return None  # Return None if there are no bots in the queue
    
    def current_bot(self):
        return self.current_bot
    
    def is_empty(self):
        return len(self.queue) == 0  # Check if the queue is empty
