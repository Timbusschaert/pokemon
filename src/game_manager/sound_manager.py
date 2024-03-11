import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sound_effects = {}
        self.music = None

    def load_sound_effect(self, name, file_path):
        sound = pygame.mixer.Sound(file_path)
        self.sound_effects[name] = sound

    def play_sound_effect(self, name):
        if name in self.sound_effects:
            self.sound_effects[name].play()
        else:
            print(f"Sound effect '{name}' not found.")

    def load_music(self, file_path):
        pygame.mixer.music.load(file_path)

    def play_music(self, loops=-1):
        pygame.mixer.music.play(loops)

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)

# Exemple d'utilisation :
if __name__ == "__main__":
    pygame.init()
    manager = SoundManager()

    # Charger les sons et la musique
    manager.load_sound_effect("explosion", "explosion.wav")
    manager.load_music("background_music.mp3")

    # Jouer les sons et la musique
    manager.play_sound_effect("explosion")
    manager.play_music()

    # Arrêter la musique
    pygame.time.wait(5000)  # Attendre 5 secondes
    manager.stop_music()

    pygame.quit()
