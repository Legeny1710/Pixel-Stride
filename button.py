import pygame

class Button:
    def __init__(self):
        self.button_image_1 = pygame.transform.rotozoom(pygame.image.load("wood_btn1.png").convert_alpha(), 0, 3)
        self.button_image_2 = pygame.transform.rotozoom(pygame.image.load("wood_btn2.png").convert_alpha(), 0, 3)
        self.button_image_3 = pygame.transform.rotozoom(pygame.image.load("wood_btn3.png").convert_alpha(), 0, 3)
        self.button_movement_list = [self.button_image_1, self.button_image_2, self.button_image_3]


        self.movement_list = [self.button_image_1, self.button_image_2, self.button_image_3]
        self.move_index = 0
        self.image = self.movement_list[self.move_index]
        self.rect = self.image.get_rect(center=(400, 350))

    def animate(self):
        self.move_index += 0.05
        if self.move_index >= len(self.movement_list): self.move_index = 0
        self.image = self.movement_list[int(self.move_index)]
