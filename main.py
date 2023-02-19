import pygame
from td_common import get_image, WIN_WIDTH, WIN_HEIGHT
from td_world import WorldMap
from td_player import Player
from td_ui import Menu, Inventory
    

def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption('PixelMMO - I Don\'t Even Know')
    pygame.display.set_icon(get_image('player/player_base_male1'))
    clock = pygame.time.Clock()
    
    this_world = WorldMap('overworld')
    player = Player()
    menu = Menu()
    inventory = Inventory()
    
    run = True
    while run:
        clock.tick(30)
        events = pygame.event.get()
        draw_window(win, this_world, player, inventory, events, menu)
        run = input(this_world, events, inventory, menu, player)
        
        
def draw_window(win, this_world, player, inventory, event, menu):
    win.fill(pygame.Color(0,0,0))
    this_world.draw(win)
    player.draw(win)
    menu.draw(win)
    if inventory.inv_toggle:
        inventory.draw(win)
    
    pygame.display.update()
    
    
def input(this_world, events, inventory, menu, player):
    run = True
    this_world.check_collide(player)
    for event in events:
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
                
        inventory.check_input(event)
    player.move(this_world)
    
    return run


if __name__ == '__main__':
    main()