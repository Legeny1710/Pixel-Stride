import pygame
import random
from score import Score
from sys import exit
from character import RunnerCharacter
from enemies import Monsters


the_story_text1 = " Welcome to PIXEL STRIDE!"
the_story_text2 = " This is the first story of Pixel Stride series!"
the_story_text3 =  "Story: There was once a hunter, minding his own business, hunting, eating, surviving... But one time his son, (his rifle given by his dad) stolen"
the_story_text4 =  " He doesn't know who but he knows whoever stole it escaped into the woods..."
the_story_text5 =  " Now it is your time to help him survive through this dangerous forest and get back his almighty weapon!"


story_list = [the_story_text1, the_story_text2, the_story_text3, the_story_text4, the_story_text5]


# initilise pygame
pygame.init()





# display surface
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pixel-Stride")
background = pygame.image.load("fores_background.png").convert()
background = pygame.transform.scale(background, (800, 300))

# ground
ground = pygame.image.load("fores_background.png").convert()
ground = pygame.transform.scale(ground, (800, 400))
ground_rect = ground.get_rect(midtop=(400, 300))


game_speed = 8

x_pos_bg = ground_rect.x
y_pos_bg = ground_rect.y


def Background():
    global x_pos_bg, y_pos_bg, game_speed
    image_width = ground.get_width()
    screen.blit(ground, (x_pos_bg, y_pos_bg))
    screen.blit(ground, (image_width + x_pos_bg, y_pos_bg))
    if x_pos_bg <= -image_width:
        screen.blit(ground, (image_width + x_pos_bg, y_pos_bg))
        x_pos_bg = 0
    x_pos_bg -= game_speed


# game_states
in_story = True
in_game = False
is_transitioning = False
start_menu_active = False






player = pygame.sprite.GroupSingle()
player.add(RunnerCharacter())


enemies_sprite_group = pygame.sprite.Group()


score = Score()

# game variables
game_font = pygame.font.Font("Pixeltype.ttf", 50)
story_font = pygame.font.Font("Pixeltype.ttf",21)

score_text = game_font.render(f"Score:{score}", False, (255, 255, 255))
score_text_rect = score_text.get_rect(center=(400, 100))

game_title = game_font.render("PIXEL STRIDE", False, (255, 255, 255))
game_title_rect = game_title.get_rect(center = (400,150))

game_over = game_font.render("GAME OVER",  False, (255, 255, 255))
game_over_rect = game_over.get_rect(center = (400, 200))


button = pygame.image.load("button_image.png").convert_alpha()
pygame.transform.rotozoom(button, 0, 0.5)
button_rect = button.get_rect(center = (400,200))

# game_variables
start_time = 0


bg_music = pygame.mixer.Sound("music.wav")

keys = pygame.key.get_pressed()



# clock object
clock = pygame.time.Clock()


def game_over_text():
    screen.blit(game_over, game_over_rect)


# Timer
enemy_spawn_time = 1000
enemy_spawn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_spawn_timer, enemy_spawn_time)
enemy_spawn_count = 1

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, enemies_sprite_group , False):
        score.save_score()
        enemies_sprite_group.empty()
        return False
    return True

bg_music.play(loops= -1)

while True:

    screen.blit(background, (0, 0))
    screen.blit(ground, ground_rect)

    Background()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            score.save_score()
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if in_story:
                in_story = False
                start_menu_active = True
            if is_transitioning:
                start_menu_active = True
                is_transitioning = False
        if event.type == pygame.MOUSEBUTTONDOWN and start_menu_active == True:
            if button_rect.collidepoint(event.pos):
                start_menu_active = False
                in_game = True



        if event.type == enemy_spawn_timer:
            # for i in range(enemy_spawn_count):
            if random.choice(["fly","wolf","wolf"]) == "fly":
                enemies_sprite_group.add(Monsters("fly"))
            else:
                enemies_sprite_group.add(Monsters("wolf"))

            # enemy_spawn_count += 1
            #
            # if enemy_spawn_count == 2:
            #     enemy_spawn_count = 1

    if in_story:
        the_story_text_image1 = story_font.render(story_list[0], 0, (255, 255, 255))
        the_story_text_rect1 = the_story_text_image1.get_rect(center=(400, 80))
        the_story_text_image2 = story_font.render(story_list[1], 0, (255, 255, 255))
        the_story_text_rect2 = the_story_text_image2.get_rect(center=(400, 130))
        the_story_text_image3 = story_font.render(story_list[2], 0, (255, 255, 255))
        the_story_text_rect3 = the_story_text_image3.get_rect(center=(400, 180))
        the_story_text_image4 = story_font.render(story_list[3], 0, (255, 255, 255))
        the_story_text_rect4 = the_story_text_image4.get_rect(center=(400, 230))
        the_story_text_image5 = story_font.render(story_list[4], 0, (255, 255, 255))
        the_story_text_rect5 = the_story_text_image5.get_rect(center=(400, 280))
        screen.blit(the_story_text_image1, the_story_text_rect1)
        screen.blit(the_story_text_image2, the_story_text_rect2)
        screen.blit(the_story_text_image3, the_story_text_rect3)
        screen.blit(the_story_text_image4, the_story_text_rect4)
        screen.blit(the_story_text_image5, the_story_text_rect5)




    if in_game and not start_menu_active:


        score.update_score(start_time)
        screen.blit(score.score_text, score.score_text_rect)



        # # Player
        player.draw(screen)
        player.update()

        # Enemy
        enemies_sprite_group.draw(screen)
        enemies_sprite_group.update()


        # collision
        in_game = collision_sprite()
        if in_game == False:
            is_transitioning = True


    elif is_transitioning:
        screen.blit(game_over, game_over_rect)


    elif start_menu_active and not in_game:

        start_menu_active = True
        enemy_spawn_count = 0
        score.current_score = 0
        start_time = pygame.time.get_ticks()
        screen.blit(button, button_rect)
        screen.blit(game_title, game_title_rect)

        score.best_score_text = score.game_font.render(f"Best Score: {score.show_best_score()}", False, (255, 255, 255))
        score.best_score_text_rect = score.best_score_text.get_rect(center=(400, 350))
        screen.blit(score.best_score_text,score.best_score_text_rect)


    pygame.display.update()
    clock.tick(60)




