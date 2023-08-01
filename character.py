import pygame

class Character():
    def __init__(self, display):
        # super().__init__()
        self.player_image = pygame.image.load("player_stand.png").convert_alpha()
        self.player_image_rect = self.player_image.get_rect(center=(400, 200))

    def move_character(self):
        self.player_image_rect.x += 1
