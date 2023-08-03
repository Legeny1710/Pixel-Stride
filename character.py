import pygame


class RunnerCharacter:
    def __init__(self):
        # super().__init__()
        self.player_image = pygame.image.load("player_stand.png").convert_alpha()
        self.player_image_rect = self.player_image.get_rect(center=(50, 260))


