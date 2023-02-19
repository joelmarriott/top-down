import pygame
from td_common import get_image, WIN_WIDTH, WIN_HEIGHT, TILE_SIZE

class Player:
    def __init__(self):
        self.pos_x = (WIN_WIDTH - (TILE_SIZE / 2)) / 2
        self.pos_y = (WIN_HEIGHT - (TILE_SIZE / 2)) / 2
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 8
        self.image = get_image('player/design/player_animate1')
        self.direction = 0
        
    def draw(self, win):
        win.blit(self.image, (self.pos_x, self.pos_y))
        
    def move(self, map):
        self.vel_x = 0
        self.vel_y = 0
        keys = pygame.key.get_pressed()
        left, right, up, down = False, False, False, False
        if keys[pygame.K_LEFT] or keys[ord('a')]:
            left = True
            self.direction = -90
            map.pos_x += self.speed
            self.vel_x = -1
        if keys[pygame.K_RIGHT] or keys[ord('d')]:
            right = True
            self.direction = 90
            map.pos_x -= self.speed
            self.vel_x = 1
        if keys[pygame.K_UP] or keys[ord('w')]:
            up = True
            self.direction = 180
            map.pos_y += self.speed
            self.vel_y = -1
        if keys[pygame.K_DOWN] or keys[ord('s')]:
            down = True
            self.direction = 0
            map.pos_y -= self.speed
            self.vel_y = 1

        if left or right or up or down:
            if self.moving == 0:
                self.moving = 1
        else:
            self.moving = 0
        self.get_player_image()
            
            
    def get_mask(self):
        return pygame.mask.from_surface(self.image)
    
    
    def get_player_image(self):
        if self.moving == 0:
            if self.direction == 0:
                self.image = get_image('player/player_base_male1')
            elif self.direction == 180:
                self.image = get_image('player/player_base_male_back1')
            elif self.direction == 90:
                self.image = get_image('player/player_base_male_right1')
            else:
                self.image = get_image('player/player_base_male_left1')
                
        if self.moving > 0:
            frame = round(self.moving/4)
            if frame == 0:
                frame = 1
            if self.direction == 0:
                self.image = get_image('player/player_base_male'+str(frame))
            elif self.direction == 180:
                self.image = get_image('player/player_base_male_back'+str(frame))
            elif self.direction == 90:
                self.image = get_image('player/player_base_male_right'+str(frame))
            else:
                self.image = get_image('player/player_base_male_left'+str(frame))
            if self.moving == 16:
                self.moving = 1
                
            self.moving += 1

