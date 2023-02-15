import pygame
from td_common import get_image, WIN_WIDTH, WIN_HEIGHT, TILE_SIZE
from td_world import WorldMap
from td_player import Player
from td_ui import UI, Inventory


def draw_window(win, this_world, player, ui, inventory, event):
    win.fill(pygame.Color(202,213,227))
    this_world.draw(win)
    player.draw(win)
    ui.draw(win, (30, 30))
    if inventory.inv_toggle:
        inventory.draw(win, (500, 300), event)
    
    pygame.display.update()
    

def main():
    map_matrix = [
            [ 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 2,  2,  2,  2,  2,  0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 6, 1,  1,  1,  1,  1,  9, 0, 0, 0, 0 ],
            [ 0, 0, 0, 6, 1, 1,  1,  1,  1,  1,  1, 9, 0, 0, 0 ],
            [ 0, 0, 6, 1, 1, 1,  1,  1,  1,  1,  1, 1, 9, 0, 0 ],
            [ 0, 3, 1, 1, 1, 10, 10, 1,  10, 10, 1, 1, 1, 5, 0 ],
            [ 0, 3, 1, 1, 1, 10, 1,  1,  1,  10, 1, 1, 1, 5, 0 ],
            [ 0, 3, 1, 1, 1, 1,  1,  1,  1,  1,  1, 1, 1, 5, 0 ],
            [ 0, 3, 1, 1, 1, 10, 1,  1,  1,  10, 1, 1, 1, 5, 0 ],
            [ 0, 3, 1, 1, 1, 10, 10, 1,  10, 10, 1, 1, 1, 5, 0 ],
            [ 0, 0, 7, 1, 1, 1,  1,  1,  1,  1,  1, 1, 8, 0, 0 ],
            [ 0, 0, 0, 7, 1, 1,  1,  1,  1,  1,  1, 8, 0, 0, 0 ],
            [ 0, 0, 0, 0, 7, 1,  1,  1,  1,  1,  8, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 4,  4,  4,  4,  4,  0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  0, 0, 0, 0, 0 ]
    ]
    this_world = WorldMap(map_matrix)

    player_x = (WIN_WIDTH - TILE_SIZE) / 2
    player_y = (WIN_HEIGHT - TILE_SIZE) / 2
    player = Player(player_x, player_y)
    
    ui = UI()
    inventory = Inventory()
    
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption('Unnamed Top Down Game')
    pygame.display.set_icon(get_image('player'))
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(30)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                
            inventory.check_input(event)
        
        player.move()
            
        this_world.check_collide(player)
        
        draw_window(win, this_world, player, ui, inventory, event)


if __name__ == '__main__':
    main()