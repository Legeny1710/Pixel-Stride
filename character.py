import pygame
import os


RUNNING = [
    pygame.image.load(os.path.join("player_walk_1.png")),
    pygame.image.load(os.path.join("player_walk_2.png")),
]


class RunnerCharacter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load("player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("player_walk_2.png").convert_alpha()
        self.walk_list = [player_walk_1, player_walk_2]
        self.jump = pygame.image.load("jump.png").convert_alpha()
        self.frame_index = 0
        self.image = self.walk_list[self.frame_index]
        self.rect = self.image.get_rect(center=(50, 260))
        self.gravity = 0

    def player_animate(self):
        if self.rect.bottom < 300:
            self.image = self.jump
        else:
            self.frame_index += 0.1
            if self.frame_index >= len(self.walk_list): self.frame_index = 0
            self.image = self.walk_list[int(self.frame_index)]

    def apply_gravity(self):
        self.gravity += 0.85
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def Jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            # self.jump_sound.play()

    def update(self):
        self.apply_gravity()
        self.Jump()
        self.player_animate()

