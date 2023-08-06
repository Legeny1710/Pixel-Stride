import pygame
from random import randint

import score



class Monsters(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == "fly":
            fly1 = pygame.image.load("fly_1.png")
            fly2 = pygame.image.load("fly_2.png")
            self.movement_list = [fly1,fly2]
            self.move_index = 0
            self.image = self.movement_list[self.move_index]

            self.rect = self.image.get_rect(midbottom=(randint(2100, 2300), randint(230, 300)))
            self.speed = 10

        elif type == "snail":
            snail1 = pygame.image.load("snail_1.png")
            snail2 = pygame.image.load("snail_2.png")
            self.movement_list = [snail1, snail2]
            self.move_index = 0
            self.image = self.movement_list[self.move_index]
            self.image = pygame.image.load("snail_1.png").convert_alpha()  # alpha bit removes the alpha values
            self.rect = self.image.get_rect(midbottom=(850, 300))
            self.speed = 8

    def monster_animate(self):
        self.move_index += 0.1
        if self.move_index >= len(self.movement_list): self.move_index = 0
        self.image = self.movement_list[int(self.move_index)]

    def move(self):
        # enemy mechanic
        self.rect.x -= self.speed

    def destroy(self):
        if self.rect.x <= -75:
            self.kill()


    def update(self):
        self.move()
        self.destroy()
        self.monster_animate()




