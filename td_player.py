from td_common import get_image
import pygame

class Player:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x - 4
        self.pos_y = pos_y - 4
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        self.image = get_image('player/player_still')
        self.direction = 0
        
    def draw(self, win):
        win.blit(self.image, (self.pos_x, self.pos_y))
        
    def move(self):
        self.vel_x = 0
        self.vel_y = 0
        keys = pygame.key.get_pressed()
        left, right, up, down = False, False, False, False
        if keys[pygame.K_LEFT] or keys[ord('a')]:
            left = True
            self.direction = -90
            self.pos_x -= self.speed
            self.vel_x = -1
        if keys[pygame.K_RIGHT] or keys[ord('d')]:
            right = True
            self.direction = 90
            self.pos_x += self.speed
            self.vel_x = 1
        if keys[pygame.K_UP] or keys[ord('w')]:
            up = True
            self.direction = 180
            self.pos_y -= self.speed
            self.vel_y = -1
        if keys[pygame.K_DOWN] or keys[ord('s')]:
            down = True
            self.direction = 0
            self.pos_y += self.speed
            self.vel_y = 1

        if left or right or up or down:
            self.image = get_image('player/player_moving', self.direction)
        else:
            self.image = get_image('player/player_still', self.direction)
            
            
            
    def get_mask(self):
        return pygame.mask.from_surface(self.image)