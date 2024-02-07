import pygame
import xml.etree.ElementTree as ET

class Animation:
    def __init__(self, image_path, xml_path):
        # Chargement de l'image
        self.image = pygame.image.load(image_path)
        self.image.fill((255, 255, 255), None, pygame.BLEND_RGBA_MULT)
        # Analyse du fichier XML
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # Accès aux données d'animation
        self.shadow_size = int(root.find('ShadowSize').text)
        anim_data = root.find('Anims/Anim')
        self.anim_name = anim_data.find('Name').text
        self.frame_width = int(anim_data.find('FrameWidth').text)
        self.frame_height = int(anim_data.find('FrameHeight').text)
        self.durations = [int(duration.text) for duration in anim_data.findall('Durations/Duration')]

        # Création d'une surface pour l'animation
        self.animation_surface = pygame.Surface((self.frame_width, self.frame_height))

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

        # Affichage de la surface d'animation sur la surface spécifiée
        cropped_image = self.image.subsurface((self.current_frame * self.frame_width + 5 , 0 , self.frame_width -5, self.frame_height))
        
        #resized = pygame.transform.scale(cropped_image,(24,24))
# Redimensionner l'image extraite à une taille de 24x24 pixels
        surface.blit(cropped_image,position)
