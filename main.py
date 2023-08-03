import pygame
from score import Score
from sys import exit
from character import RunnerCharacter
from enemies import Fly, Snail


# initilise pygame
pygame.init()

# display surface
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pixel-Stride")
background = pygame.image.load("Sky.png").convert()

# ground
ground = pygame.image.load("ground.png").convert()
ground_rect = ground.get_rect(midtop=(400, 300))




# player character
player_gravity = 0
player = RunnerCharacter()

score = Score()

# enemies
fly = Fly()
snail = Snail()

game_font = pygame.font.Font("Pixeltype.ttf", 50)
score_text = game_font.render(f"Score:{score}", False, (64, 64, 64))
score_text_rect = score_text.get_rect(center=(400, 100))


# game_variables
start_time = 0
# vel = 100
# jump = False

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
            if event.key == pygame.K_SPACE and player.player_image_rect.bottom >= 300:
                player_gravity = -20
                

    screen.blit(ground, ground_rect)
    score.update_score(start_time)
    screen.blit(score.score_text,score.score_text_rect)


    # Player
    player_gravity += 0.8
    player.player_image_rect.y += player_gravity

    if player.player_image_rect.bottom >= 300:
        player.player_image_rect.bottom = 300

    screen.blit(player.player_image, player.player_image_rect)

    # Enemy
    fly.move()
    snail.move()
    screen.blit(snail.snail_image, snail.snail_rect)
    screen.blit(fly.fly_image, fly.fly_rect)

    pygame.display.update()
    clock.tick(60)




