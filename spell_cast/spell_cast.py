import pygame
import sys
from random import randint

# classes

# functions 
def game_over_screen():
    screen.fill(PURPLE)
    title_rect.center = (400, 50)
    mage_1_rect.center = (400, 150)
    screen.blit(title_surf, title_rect)
    screen.blit(mage_1_surf, mage_1_rect)

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

# file imports
main_font = pygame.font.Font("fonts/VisitorRus.ttf", 60)
mage_1_surf = pygame.image.load("images/mage/mage1.png")


# text render
title_surf = main_font.render("Spellcast 2D", False, BLACK)

#rectangles creation and text render
title_rect = title_surf.get_rect()
mage_1_rect = mage_1_surf.get_rect()


# running game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_KP_ENTER:
                game_active = True
    if game_active:
        screen.blit()
    if game_active == False:
        game_over_screen()

    pygame.display.update()
    clock.tick(60)
        











