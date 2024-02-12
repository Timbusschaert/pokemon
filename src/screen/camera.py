
import pygame
class CameraGroup(pygame.sprite.Group):
	def __init__(self,screen):
		super().__init__()
		self.display_surface = pygame.display.get_surface()

		# camera offset 
		self.offset = pygame.math.Vector2()
		self.half_w = self.display_surface.get_size()[0] // 2
		self.half_h = self.display_surface.get_size()[1] // 2

		# box setup
		self.camera_borders = {'left': 0, 'right': 0, 'top': 0, 'bottom': 100}
		l = self.camera_borders['left']
		t = self.camera_borders['top']
		w = self.display_surface.get_size()[0]  - (self.camera_borders['left'] + self.camera_borders['right'])
		h = self.display_surface.get_size()[1]  - (self.camera_borders['top'] + self.camera_borders['bottom'])
		self.camera_rect = pygame.Rect(l,t,w,h)

		self.ground_surf = screen
		self.ground_rect = screen.get_rect(topleft = (0,0))
		# camera speed
		self.keyboard_speed = 10

		# zoom 
		self.zoom_scale = 1
		self.internal_surf_size = (2500,2500)
		self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)
		self.internal_rect = self.internal_surf.get_rect(center = (self.half_w,self.half_h))
		self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surf_size)
		self.internal_offset = pygame.math.Vector2()
		self.internal_offset.x = self.internal_surf_size[0] // 2 - self.half_w
		self.internal_offset.y = self.internal_surf_size[1] // 2 - self.half_h

	def center_target_camera(self,target):
		self.offset.x = target.rect.centerx - self.half_w 
		self.offset.y = target.rect.centery - self.half_h
		
	def box_target_camera(self,target):

		if target.rect.left < self.camera_rect.left:
			self.camera_rect.left = target.rect.left
		if target.rect.right > self.camera_rect.right:
			self.camera_rect.right = target.rect.right
		if target.rect.top < self.camera_rect.top:
			self.camera_rect.top = target.rect.top
		if target.rect.bottom > self.camera_rect.bottom:
			self.camera_rect.bottom = target.rect.bottom

		self.offset.x = self.camera_rect.left - self.camera_borders['left']
		self.offset.y = self.camera_rect.top - self.camera_borders['top']

	def keyboard_control(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]: self.camera_rect.x -= self.keyboard_speed
		if keys[pygame.K_d]: self.camera_rect.x += self.keyboard_speed
		if keys[pygame.K_w]: self.camera_rect.y -= self.keyboard_speed
		if keys[pygame.K_s]: self.camera_rect.y += self.keyboard_speed

		self.offset.x = self.camera_rect.left - self.camera_borders['left']
		self.offset.y = self.camera_rect.top - self.camera_borders['top']
    
   
	def custom_draw(self,player):
		
		self.center_target_camera(player)
		# self.box_target_camera(player)
		# self.keyboard_control()

		# ground 
		ground_offset = self.ground_rect.topleft - self.offset + self.internal_offset
		self.internal_surf.blit(self.ground_surf,ground_offset)
		# active elements
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = (sprite.rect.centerx + ( 24 - sprite.image.frame_width) // 2 ,sprite.rect.centery + ( 24 - sprite.image.frame_height)//2) - self.offset + self.internal_offset
			sprite.image.draw(self.internal_surf,offset_pos)
		scaled_surf = pygame.transform.scale(self.internal_surf ,self.internal_surface_size_vector * self.zoom_scale)
		scaled_rect = scaled_surf.get_rect(center = (self.half_w -200,self.half_h))

		self.display_surface.blit(scaled_surf,scaled_rect)