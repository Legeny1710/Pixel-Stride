import pygame
from random import randint


class Snail(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("snail_1.png").convert_alpha() # alpha bit removes the alpha values
        self.rect = self.image.get_rect(midbottom = (randint(900,1400),300))
        self.speed = 4

    def move(self):
        # enemy mechanic
        self.rect.x -= self.speed

    def destroy(self):
        if self.rect.x <= -75:
            self.kill()
            print("destroy")

    def update(self):
        self.move()
        self.destroy()






class Fly(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("fly_1.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (randint(1000,1600), randint(150,200)))
        self.speed = 6

    def move(self):
        # enemy mechanic
        self.rect.x -= self.speed

    def destroy(self):
        if self.rect.x <= -25:
            self.kill()
            print("destroy")

    def update(self):
        self.move()

