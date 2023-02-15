from td_common import get_image
import pygame

class Player:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x + 1
        self.pos_y = pos_y + 1
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        self.image = get_image('player')
        
    def draw(self, win):
        win.blit(self.image, (self.pos_x, self.pos_y))
        
    def move(self):
        self.vel_x = 0
        self.vel_y = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[ord('a')]:
            self.pos_x -= self.speed
            self.vel_x = -1
        if keys[pygame.K_RIGHT] or keys[ord('d')]:
            self.pos_x += self.speed
            self.vel_x = 1
        if keys[pygame.K_UP] or keys[ord('w')]:
            self.pos_y -= self.speed
            self.vel_y = -1
        if keys[pygame.K_DOWN] or keys[ord('s')]:
            self.pos_y += self.speed
            self.vel_y = 1
            
            
    def get_mask(self):
        return pygame.mask.from_surface(self.image)