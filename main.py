import pygame
from score import Score
from sys import exit
from character import RunnerCharacter


# initilise pygame
pygame.init()

# display surface
screen = pygame.display.set_mode((800, 400))
screen.fill("white")
pygame.display.set_caption("Pixel-Stride")
background = pygame.image.load("Sky.png").convert()

# ground
ground = pygame.image.load("ground.png").convert()
ground_rect = ground.get_rect(midtop=(400, 300))

# player character
player_gravity = 0
player = RunnerCharacter()

score = Score()

game_font = pygame.font.Font("Pixeltype.ttf", 50)
score_text = game_font.render(f"Score:{score}", False, (64, 64, 64))
score_text_rect = score_text.get_rect(center=(400, 100))

vel = 5

keys = pygame.key.get_pressed()

# clock object
clock = pygame.time.Clock()

while True:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            score.save_score()
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.player_image_rect.y -= vel



    screen.blit(ground, ground_rect)
    score.update_score()
    screen.blit(score.score_text,score.score_text_rect)


    # Player
    player_gravity += 1
    player.player_image_rect.y += player_gravity
    if player.player_image_rect.y >= 215:
        player.player_image_rect.y = 215

    screen.blit(player.player_image, player.player_image_rect)
    # player.move_character()
    pygame.display.update()
    clock.tick(60)




