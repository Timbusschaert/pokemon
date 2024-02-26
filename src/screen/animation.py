import pygame
from src.player.current_action import CurrentAction
class Animation:
<<<<<<< HEAD
    def __init__(self, image,shadow, pokemon, tree, enumDirection, x , isContinue):
=======
    def __init__(self, image,shadow, pokemon, tree, enumDirection, x ,isContinue,musique):
>>>>>>> 438e924ed29931003b5e9504038379eefadba40c
        # Chargement de l'image principale
        self.image = image
        self.image.fill((255, 255, 255), None, pygame.BLEND_RGBA_MULT)
        self.pokemon=pokemon
        # Chargement de l'image de l'ombre
        self.shadow_image = shadow
        self.shadow_image.fill((255, 255, 255), None, pygame.BLEND_RGBA_MULT)
       
        self.isContinue = isContinue
        # Analyse du fichier XML
        root = tree.getroot()
        self.x = x
        self.isAnimating = False
        self.musique = musique
        musique.set_volume(0.5)
        # Accès aux données d'animation
        self.shadow_size = int(root.find('ShadowSize').text)
        anim_data = root.find('Anims/Anim')
        self.anim_name = anim_data.find('Name').text
        self.frame_width = int(anim_data.find('FrameWidth').text)
        self.frame_height = int(anim_data.find('FrameHeight').text)
        self.durations = [int(duration.text) for duration in anim_data.findall('Durations/Duration')]
        self.direction = enumDirection
        self.total_duration = 0 
        self.frame_counter_total = 0 
        for i in self.durations:
            self.total_duration += i
        # Création d'une surface pour l'animation
        self.animation_surface = pygame.Surface((self.frame_width * self.direction, self.frame_height))
        
        # Variables pour gérer l'animation
        self.current_frame = 0
        self.frame_counter = 0
        self.total_frames = len(self.durations)

    def update(self):
        # Incrémentation du compteur de frames
        self.frame_counter += 1 
        self.frame_counter_total += 1
        # Changement de frame si le temps écoulé dépasse la durée de la frame actuelle
        if self.frame_counter >= self.durations[self.current_frame]:
            self.frame_counter = 0 
            if (self.current_frame + 1 ) % self.total_frames != 0  or self.isContinue:
                self.current_frame = (self.current_frame + 1) % self.total_frames 
            

    def startAnimation(self):
        self.current_frame = 0 
        self.frame_counter_total = 0 
        
    def getIsFinished(self):   
        return self.frame_counter_total >= self.total_duration + 4
     
    
    def draw(self, surface, position,pokemon):
        # Calcul de la position de l'ombre
       
        shadow_image = self.shadow_image.subsurface((self.current_frame * self.frame_width, self.frame_height * self.direction, self.frame_width, self.frame_height))
        # Affichage de l'ombre
        surface.blit(shadow_image, position)
       
        # Affichage de la surface d'animation sur la surface spécifiée
        cropped_image = self.image.subsurface((self.current_frame * self.frame_width , self.frame_height * self.direction, self.frame_width , self.frame_height))
        surface.blit(cropped_image, position)

        if pokemon.current_action ==  CurrentAction.HURT:
            font = pygame.font.Font(None, 18)
            damage_text = font.render('-10', True, (255, 255, 255))
            text_position = (position[0]+20, position[1] - 20)  # Positionnez le texte au-dessus de la tête du personnage
            surface.blit(damage_text, text_position)
