import pygame


class RunnerCharacter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player_stand.png").convert_alpha()
        self.rect = self.image.get_rect(center=(50, 260))
        self.gravity = 0

    def apply_gravity(self):
        self.gravity += 0.85
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            # self.jump_sound.play()

    def update(self):
        self.apply_gravity()
        self.jump()

