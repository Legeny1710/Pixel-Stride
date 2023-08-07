import pygame



class RunnerCharacter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.transform.rotozoom(pygame.image.load("hunter_1.png").convert_alpha(), 0 , 2)
        player_walk_2 = pygame.transform.rotozoom(pygame.image.load("hunter_2.png").convert_alpha(), 0 , 2)
        player_walk_3 = pygame.transform.rotozoom(pygame.image.load("hunter_3.png").convert_alpha(), 0 , 2)
        player_walk_4 = pygame.transform.rotozoom(pygame.image.load("hunter_4.png").convert_alpha(), 0 , 2)
        player_walk_5 = pygame.transform.rotozoom(pygame.image.load("hunter_5.png").convert_alpha(), 0 , 2)
        player_walk_6 = pygame.transform.rotozoom(pygame.image.load("hunter_6.png").convert_alpha(), 0, 2)
        self.walk_list = [player_walk_1, player_walk_2, player_walk_3, player_walk_4, player_walk_5, player_walk_6]
        self.jump = pygame.transform.rotozoom(pygame.image.load("hunter-jump1.png").convert_alpha(), 0 , 2)
        self.frame_index = 0

        self.image = self.walk_list[self.frame_index]
        self.rect = self.image.get_rect(center=(50, 280))
        self.gravity = 0

    def player_animate(self):
        if self.rect.bottom < 300:
            self.image = self.jump
        else:
            self.frame_index += 0.3
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

