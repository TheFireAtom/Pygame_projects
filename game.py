import pygame
from sys import exit
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load("graphics/player/jump.png").convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (200, 300))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == "fly":
            fly_1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
            fly_2 = pygame.image.load("graphics/fly/fly2.png").convert.alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
            snail_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(900, 1100), y_pos))

    def animation_state(self):
        # do by my own


def display_score():
    current_time = (pygame.time.get_ticks() // 1000) - start_time
    score_surf = test_font.render(f"Score: {current_time}", False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300: screen.blit(snail_surf, obstacle_rect)  
            else: screen.blit(fly_surf, obstacle_rect)
                
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else : return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]
    # play walking animation if the player is on floor
    # display the jump surface when player is not on floor

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = False
start_time = 0
score = 0

player = pygame.sprite.GroupSingle()
player.add(Player())

sky_surf = pygame.image.load("graphics/Sky.png").convert()
ground_surf = pygame.image.load("graphics/ground.png").convert()

# score_surf = test_font.render("My game", False, (64, 64, 64))
# score_rect = score_surf.get_rect(center = (400, 50))

# Obstacles

# Snail
snail_frame_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

# Fly
fly_frame_1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
fly_frame_2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]


obstacle_rect_list = []

player_walk_1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load("graphics/player/jump.png").convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

# Intro screen
player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

title_surf = test_font.render("Manrunner 2D", False, (111, 196, 169))
title_rect = title_surf.get_rect(center = (400, 80))

game_message = test_font.render("Press space to run", False, (111, 196, 169))
game_message_rect = game_message.get_rect(center= (400, 330))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print("collision")
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300: 
                    player_gravity = -20

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
                    player_gravity = -20
        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks() // 1000

        if game_active:
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900, 1100), 210)))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]

    if game_active:           
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        # pygame.draw.rect(screen, "#c0e8ec", score_rect)
        # pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
        # pygame.draw.ellipse(screen, "Brown", pygame.Rect(50, 200, 100, 100))
        # screen.blit(score_surf, score_rect)
        score = display_score()

        # snail_rect.x -= 4
        # if snail_rect.right <= 0: snail_rect.left = 800
        # screen.blit(snail_surf, snail_rect)
        # player_rect.left += 1

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf, player_rect)
        player.draw(screen)
        player.update()

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collisions 
        game_active = collisions(player_rect, obstacle_rect_list)
        
    else:
        screen.fill((94,129,162)) 
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message = test_font.render(f"Your score: {score}", False, (111,196,169))
        score_message_rect = score_message.get_rect(center = (400, 330))
        screen.blit(title_surf, title_rect)
        if score == 0: screen.blit(game_message, game_message_rect)
        else: screen.blit(score_message, score_message_rect)
    
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("jump")

    # if player_rect.colliderect(snail_rect):
    #     print("collision")

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())
   
    pygame.display.update()
    clock.tick(60)