from td_common import get_image, WIN_WIDTH, WIN_HEIGHT, TILE_SIZE
import pygame


class Slot:
    def __init__(self, pos, slot_type=None):
        self.image = get_image('ui/slot')
        self.pos = pos
        self.rect = self.image.get_rect()
        self.slot_type = slot_type
        self.toggle = False
        self.selected = False
        
    def draw(self, box, event, window_pos):
        self.selected = False
        box.blit(self.image, self.pos)
        self.rect.x = self.pos[0] + window_pos[0]
        self.rect.y = self.pos[1] + window_pos[1]
        self.check_slot(box, event)

    def check_slot(self, box, event):
        if self.slot_type == 'inventory':
            box.blit(get_image('ui/bag'), self.pos)
                    
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                box.blit(get_image('ui/slot_select'), self.pos)
                self.selected = True
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.toggle = True
 
    def get_mask(self):
        return pygame.mask.from_surface(self.image)
        

class Menu:
    def __init__(self):
        self.BACKGROUND = get_image('ui/menu')
        self.width = self.BACKGROUND.get_width()
        self.height = self.BACKGROUND.get_height()
        self.slots = []
        pos_x = 15
        menu_items = [ 'inventory', None, None, None, None, None, None, None, None, None]
        for menu_item in menu_items:            
            self.slots.append(Slot((pos_x, 6), menu_item))
            pos_x += 31
        
    def draw(self, win, event, inventory):
        self.box = pygame.Surface((self.width, self.height))
        self.box.blit(self.BACKGROUND, (0,0))
        pos = ((WIN_WIDTH - self.width) / 2, WIN_HEIGHT - self.height)
        for slot in self.slots:
            slot.draw(self.box, event, pos)
            if slot.selected and slot.toggle:
                slot.toggle = False
                if slot.slot_type == 'inventory':
                    if inventory.inv_toggle == False:
                        inventory.inv_toggle = True
                    elif inventory.inv_toggle == True:
                        inventory.inv_toggle = False
                    break
        win.blit(self.box, pos)


class Inventory:
    def __init__(self):
        self.BACKGROUND = get_image('ui/inventory')
        self.width = self.BACKGROUND.get_width()
        self.height = self.BACKGROUND.get_height()
        self.rect = self.BACKGROUND.get_rect()
        self.pos = (500, 300)
        self.inv_toggle = False
        self.rectangle_draging = False
        self.slots = [
            self.slot_row(10, [15, 30]),
            self.slot_row(10, [15, 61]),
            self.slot_row(10, [15, 92]),
            self.slot_row(10, [15, 123]),
            self.slot_row(10, [15, 154])
        ]
        
    def draw(self, win, event):
        x, y = self.pos
        self.box = pygame.Surface((self.width, self.height))
        self.box.blit(self.BACKGROUND, (0,0))
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.slot_active = False
        
        for row in self.slots:
            for slot in row:
                slot.draw(self.box, event, self.pos)
                if slot.selected:
                    self.slot_active = True

        if event.type == pygame.MOUSEBUTTONDOWN and not self.slot_active:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    self.offset_x = x - mouse_x
                    self.offset_y = y - mouse_y

        elif event.type == pygame.MOUSEMOTION and not self.slot_active:
            if self.rectangle_draging:
                mouse_x, mouse_y = event.pos
                x = mouse_x + self.offset_x
                y = mouse_y + self.offset_y
        self.pos = (x, y)

        win.blit(self.box, self.pos)
        
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
                    
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                self.rectangle_draging = False
