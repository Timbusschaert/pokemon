import pygame

class MenuBox:
    def __init__(self, screen, font, items):
        self.screen = screen
        self.font = font
        self.items = items
        self.selected_item = 0
        self.visible = False
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive

        # Dimensions du menu
        self.menu_width = 200
        self.menu_height = len(items) * 40
        self.menu_rect = pygame.Rect(screen.get_width() - self.menu_width - 10,
                                      screen.get_height() - self.menu_height - 10,
                                      self.menu_width, self.menu_height)

    def toggle_visibility(self):
        self.visible = not self.visible

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.visible:
                if event.key == pygame.K_UP:
                    self.selected_item = (self.selected_item - 1) % len(self.items)
                elif event.key == pygame.K_DOWN:
                    self.selected_item = (self.selected_item + 1) % len(self.items)
                elif event.key == pygame.K_a:
                    print("Selected:", self.items[self.selected_item])
                elif event.key ==pygame.K_b:
                    self.toggle_visibility

    def draw(self):
        if self.visible:
            pygame.draw.rect(self.screen, pygame.Color('gray'), self.menu_rect)
            for i, item in enumerate(self.items):
                item_surface = self.font.render(item, True, self.color_active if i == self.selected_item else self.color_inactive)
                item_rect = item_surface.get_rect(center=(self.menu_rect.centerx, self.menu_rect.top + 20 + i * 40))
                self.screen.blit(item_surface, item_rect)
