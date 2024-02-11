import pygame

class Animation:
    def __init__(self, image, pokemon, tree, enumDirection, x):
        # Chargement de l'image principale
        self.image = image
        self.image.fill((255, 255, 255), None, pygame.BLEND_RGBA_MULT)
        self.pokemon=pokemon
        # Chargement de l'image de l'ombre
        self.shadow_image = pygame.image.load("assets/"+self.pokemon+"/Walk-Shadow.png")

        # Analyse du fichier XML
        root = tree.getroot()
        self.x = x
        
        # Accès aux données d'animation
        self.shadow_size = int(root.find('ShadowSize').text)
        anim_data = root.find('Anims/Anim')
        self.anim_name = anim_data.find('Name').text
        self.frame_width = int(anim_data.find('FrameWidth').text)
        self.frame_height = int(anim_data.find('FrameHeight').text)
        self.durations = [int(duration.text) for duration in anim_data.findall('Durations/Duration')]
        self.direction = enumDirection
        
        # Création d'une surface pour l'animation
        self.animation_surface = pygame.Surface((self.frame_width * self.direction, self.frame_height))
        
        # Variables pour gérer l'animation
        self.current_frame = 0
        self.frame_counter = 0
        self.total_frames = len(self.durations)

    def update(self):
        # Incrémentation du compteur de frames
        self.frame_counter += 1

        # Changement de frame si le temps écoulé dépasse la durée de la frame actuelle
        if self.frame_counter >= self.durations[self.current_frame]:
            self.frame_counter = 0
            self.current_frame = (self.current_frame + 1) % self.total_frames

    def draw(self, surface, position):
        # Calcul de la position de l'ombre
        #shadow_image = self.shadow_image.subsurface((self.current_frame * self.frame_width, self.frame_height * self.direction, self.frame_width, self.frame_height))
        # Affichage de l'ombre
        #surface.blit(shadow_image, position)
        
        # Affichage de la surface d'animation sur la surface spécifiée
        cropped_image = self.image.subsurface((self.current_frame * self.frame_width , self.frame_height * self.direction, self.frame_width , self.frame_height))
        surface.blit(cropped_image, position)
