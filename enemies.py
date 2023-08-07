import pygame
from random import randint

import score



class Monsters(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == "fly":
            fly1 = pygame.transform.rotozoom(pygame.image.load("fly_ultimate.png"),0 , 0.5)
            fly2 = pygame.transform.rotozoom(pygame.image.load("fly_ultimate2.png"), 0, 0.5)
            fly3 = pygame.transform.rotozoom(pygame.image.load("fly_ultimate3.png"), 0, 0.5)
            fly4 = pygame.transform.rotozoom(pygame.image.load("fly_ultimate4.png"), 0, 0.5)

            self.movement_list = [fly1, fly2, fly3, fly4]
            self.move_index = 0
            self.image = self.movement_list[self.move_index]

            self.rect = self.image.get_rect(midbottom=(randint(2100, 2300), randint(210, 280)))
            self.speed = 10

        elif type == "wolf":
            wolf1 = pygame.transform.rotozoom(pygame.image.load("wolf_brown1.png"), 0, 3)
            wolf2 = pygame.transform.rotozoom(pygame.image.load("wolf_brown2.png"), 0, 3)
            wolf3 = pygame.transform.rotozoom(pygame.image.load("wolf_brown3.png"), 0, 3)
            wolf4 = pygame.transform.rotozoom(pygame.image.load("wolf_brown4.png"), 0, 3)
            wolf5 = pygame.transform.rotozoom(pygame.image.load("wolf_brown5.png"), 0, 3)
            wolf6 = pygame.transform.rotozoom(pygame.image.load("wolf_brown6.png"), 0, 3)
            self.movement_list = [wolf1, wolf2, wolf3, wolf4, wolf5, wolf6]
            self.move_index = 0
            self.image = self.movement_list[self.move_index]

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




