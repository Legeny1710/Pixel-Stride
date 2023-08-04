import pygame



class Snail:
    def __init__(self):
        self.snail_image = pygame.image.load("snail_1.png").convert_alpha() # alpha bit removes the alpha values
        self.snail_rect = self.snail_image.get_rect(midbottom = (750,300))

    def move(self):
        # enemy mechanic
        self.snail_rect.x -= 4
        if self.snail_rect.right <= 0:
            self.snail_rect.x = 800




class Fly:
    def __init__(self):
        self.fly_image = pygame.image.load("fly_1.png").convert_alpha()
        self.fly_rect = self.fly_image.get_rect(midbottom = (750, 200))

    def move(self):
        # enemy mechanic
        self.fly_rect.x -= 6
        if self.fly_rect.right <= 0:
            self.fly_rect.x = 800
