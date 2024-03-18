import pygame
import sys
from random import randint

# classes
class Mage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # file imports
        mage_walk_1 = pygame.image.load("images/mage/mage1.png").convert_alpha()
        mage_walk_2 = pygame.image.load("images/mage/mage2.png").convert_alpha()
        mage_walk_3 = pygame.image.load("images/mage/mage3.png").convert_alpha()
        mage_walk_4 = pygame.image.load("images/mage/mage4.png").convert_alpha()

        # mage variables
        # variables for mage animation
        self.current_frame = 0
        self.animation_speed = 100
        self.mage_walk = [mage_walk_1, mage_walk_2, mage_walk_3, mage_walk_4]
        self.image = self.mage_walk[self.current_frame]
        self.last_update = pygame.time.get_ticks()
        self.player_speed = 3
        self.direction = True

        # mage rectangle
        self.rect = self.image.get_rect(midbottom = (400, 400))
        self.x_position_old = self.rect.x
        self.x_position_new = self.rect.x
    
        # mage methods
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.direction = True
            self.rect.x -= self.player_speed
        elif keys[pygame.K_d]:
            self.direction = False
            self.rect.x += self.player_speed

    # def move_left(self):
    #     self.rect.x -= self.player_speed
    # def move_right(self):
    #     self.rect.x += self.player_speed

    def animation_state(self):
        now = pygame.time.get_ticks()
        if (now - self.last_update > self.animation_speed):
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % (len(self.mage_walk))
            self.image = self.mage_walk[self.current_frame]       
            
    def draw(self, screen):
        if self.direction == True:
            screen.blit(self.image, self.rect)     
        elif self.direction == False:
            self.image = pygame.transform.flip(self.mage_walk[self.current_frame], True, False)
            screen.blit(self.image, self.rect)   

    def update(self):
        self.player_input()
        self.animation_state()
        # self.move_left()
        # self.move_right()
        self.draw(screen)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == "goblin":
            goblin_1_surf = pygame.image.load("images/goblin/goblin1.png").convert_alpha()
            goblin_2_surf = pygame.image.load("images/goblin/goblin2.png").convert_alpha()
            goblin_3_surf = pygame.image.load("images/goblin/goblin3.png").convert_alpha()
            goblin_4_surf = pygame.image.load("images/goblin/goblin4.png").convert_alpha()
            self.frames = [goblin_1_surf, goblin_2_surf, goblin_3_surf, goblin_4_surf]
            y_pos = 380
        else:
            bat_1_surf = pygame.image.load("images/goblin/bat1.png").convert_alpha()
            bat_2_surf = pygame.image.load("images/goblin/bat2.png").convert_alpha()
            bat_3_surf = pygame.image.load("images/goblin/bat3.png").convert_alpha()
            bat_4_surf = pygame.image.load("images/goblin/bat4.png").convert_alpha()
            self.frames = [bat_1_surf, bat_2_surf, bat_3_surf, bat_4_surf]
            y_pos = 340
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.image >= len(self.frames): self.image = 0
        self.image = self.frames[int(self.animation_index)]
    
    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destrok(self):
        if self.rect <= -100:
            self.kill()         

# functions  
def game_over_screen():
    # mage model transformation and creating a rectangle for it 
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
    
    # mage_1_rect.center = (400, 350)
    goblin_1_rect.center = (150, 330)
    bat_1_rect.center = (650, 300)

    # drawing every image
    screen.blit(cave_background_surf, (0, 0))
    screen.blit(stone_ground_surf, (0, 300))
    mage.draw(screen)
    mage.update()
    # screen.blit(mage_1_surf, mage_1_rect)
    # screen.blit(goblin_1_surf, goblin_1_rect)
    # screen.blit(bat_1_surf, bat_1_rect)

def enemies_spawn():
    spawn_delay = 3000
    last_spawn_time = pygame.time.get_ticks()

    now = pygame.time.get_ticks()
    if now - last_spawn_time > spawn_delay:
        enemy = Enemy()



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

# sprites group
mage = Mage()
enemy = Enemy()
all_sprites = pygame.sprite.Group()
all_sprites.add(mage, enemy)

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

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_a:
        #         mage.move_left()
        #     elif event.key == pygame.K_d:
        #         mage.move_right()
            
    if game_active:
        draw_game()
    else:
        game_over_screen()
    

    pygame.display.update()
    clock.tick(60)
        











