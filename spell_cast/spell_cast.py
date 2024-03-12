import pygame
import sys
from random import randint

# classes

# functions 

def game_over_screen():
    screen.fill((0,0,255))

# main variables

game_active = False

# initialization                    

pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Spellcast 2D") 
main_font = pygame.font.Font("fonts/VisitorRus.ttf")

# running game

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_active = False
            elif event.key == pygame.K_KP_ENTER:
                game_active = True
    if game_active:
        screen.blit()
    if game_active == False:
        game_over_screen()
        











