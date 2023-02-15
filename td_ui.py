from td_common import get_image, WIN_WIDTH, WIN_HEIGHT, TILE_SIZE
import pygame


class Slot:
    def __init__(self, pos):
        self.image = get_image('ui/slot')
        self.pos = pos
        self.rect = self.image.get_rect()
        
    def draw(self, box, event, window_pos):
        box.blit(self.image, self.pos)
        self.rect.x = self.pos[0] + window_pos[0]
        self.rect.y = self.pos[1] + window_pos[1]
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                box.blit(get_image('ui/slot_select'), self.pos)
    
    def get_mask(self):
        return pygame.mask.from_surface(self.image)
        

class Menu:
    def __init__(self):
        self.BACKGROUND = get_image('ui/menu')
        self.width = self.BACKGROUND.get_width()
        self.height = self.BACKGROUND.get_height()
        self.slots = []
        slot_number = 1
        pos_x = 15
        for slot_number in range(10):
            self.slots.append(Slot((pos_x, 6)))
            pos_x += 31
            slot_number += 1
        
    def draw(self, win, event):
        self.box = pygame.Surface((self.width, self.height))
        self.box.blit(self.BACKGROUND, (0,0))
        pos = ((WIN_WIDTH - self.width) / 2, WIN_HEIGHT - self.height)
        for slot in self.slots:
            slot.draw(self.box, event, pos)
        win.blit(self.box, pos)


class Inventory:
    def __init__(self):
        self.BACKGROUND = get_image('ui/inventory')
        self.width = self.BACKGROUND.get_width()
        self.height = self.BACKGROUND.get_height()
        self.inv_toggle = False
        self.slots = [
            self.slot_row(10, [15, 30]),
            self.slot_row(10, [15, 61]),
            self.slot_row(10, [15, 92]),
            self.slot_row(10, [15, 123]),
            self.slot_row(10, [15, 154])
        ]
        
    def draw(self, win, pos, event):
        self.box = pygame.Surface((self.width, self.height))
        self.box.blit(self.BACKGROUND, (0,0))
        for row in self.slots:
            for slot in row:
                slot.draw(self.box, event, pos)
        win.blit(self.box, pos)
        
    def slot_row(self, slots, pos):
        pos_x, pos_y = pos
        slot_row = []
        slot_number = 1
        for slot_number in range(slots):
            slot_row.append(Slot((pos_x, pos_y)))
            pos_x += 31
            slot_number += 1
        return slot_row
    
    def check_input(self, event):
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[ord('i')]:
                if self.inv_toggle == False:
                    self.inv_toggle = True        
                else:
                    self.inv_toggle = False
