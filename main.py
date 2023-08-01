import pygame
from sys import exit
from character import Character


# initilise pygame
pygame.init()

# display surface
screen = pygame.display.set_mode((800,400))
screen.fill("white")
pygame.display.set_caption("Pixel-Stride")
background = pygame.image.load("Sky.png").convert()

# ground
ground = pygame.image.load("ground.png").convert()
ground_rect = ground.get_rect(midtop = (400,300))

# player character
player = Character(screen)

score = 0
# game_font = pygame.font.Font("pygame zero-to-hero-assets/Pixeltype.ttf",50)
# score_text = game_font.render(f"Score:{score}", False, (64,64,64))
# score_text_rect = score_text.get_rect(center = (400,100))

# clock object
clock = pygame.time.Clock()



while True:
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(ground,ground_rect)
    screen.blit(player.player_image, player.player_image_rect)
    player.move_character() 
    pygame.display.update()
    clock.tick(60)

