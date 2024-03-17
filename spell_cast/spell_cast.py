import pygame
import sys
from random import randint

# classes

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


# functions 
def game_over_screen():
    # file imports
    mage_1_title_surf = pygame.transform.scale2x(mage_1_surf)
    mage_1_title_rect = mage_1_title_surf.get_rect()

    # rendering text and creating rectangles for it 
    title_surf_1 = main_font.render("Spellcast 2D", False, BLACK).convert_alpha()
    title_surf_2 = main_font.render("Press \"ENTER\" to play", False, BLACK).convert_alpha()
    title_rect_1 = title_surf_1.get_rect()
    title_rect_2 = title_surf_2.get_rect()

    # drawing screen and positioning images
    screen.fill(PURPLE)
    title_rect_1.center = (400, 50)
    title_rect_2.center = (400, 340)
    mage_1_title_rect.center = (400, 210)
    screen.blit(title_surf_1, title_rect_1)
    screen.blit(title_surf_2, title_rect_2)
    screen.blit(mage_1_title_surf, mage_1_title_rect)

def draw_game():
    # file imports
    cave_background_surf = pygame.image.load("images/cave_background/cave_background.png").convert_alpha()
    stone_ground_surf = pygame.image.load("images/stone_ground/stone_ground.png").convert_alpha()

    # drawing screen and positioning images
    mage_1_rect.center = (400, 350)
    goblin_1_rect.center = (150, 330)
    bat_1_rect.center = (650, 300)
    screen.blit(cave_background_surf, (0, 0))
    screen.blit(stone_ground_surf, (0, 300))
    screen.blit(mage_1_surf, mage_1_rect)
    screen.blit(goblin_1_surf, goblin_1_rect)
    screen.blit(bat_1_surf, bat_1_rect)

# colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
PURPLE = "#5B115B"

# initialization                    
pygame.init()
screen_width = 800
screen_height = 400
game_active = False 
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Spellcast 2D") 

# global file imports
# player
main_font = pygame.font.Font("fonts/VisitorRus.ttf", 60)
mage_1_surf = pygame.image.load("images/mage/mage1.png").convert_alpha()

# enemies
goblin_1_surf = pygame.image.load("images/goblin/goblin.png").convert_alpha()
bat_1_surf = pygame.image.load("images/bat/bat.png").convert_alpha()

#rectangles creation
mage_1_rect = mage_1_surf.get_rect()
goblin_1_rect = goblin_1_surf.get_rect()
bat_1_rect = bat_1_surf.get_rect()

# running game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit() 
             
        if game_active == False:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_active = True
                
    if game_active:
        draw_game()
    else:
        game_over_screen()
    



    pygame.display.update()
    clock.tick(60)
        











