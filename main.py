import pygame
from td_common import WIN_WIDTH, WIN_HEIGHT, TILE_SIZE
from td_world import WorldMap
from td_player import Player


def draw_window(win, world_map, player):
    win.fill(pygame.Color(202,213,227))
    world_map.draw(win)
    player.draw(win)
    
    pygame.display.update()
    

def main():
    world_map = WorldMap()

    player_x = (WIN_WIDTH - TILE_SIZE) / 2
    player_y = (WIN_HEIGHT - TILE_SIZE) / 2
    player = Player(player_x, player_y)
    
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption('Unnamed Top Down Game')
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
        
        player.move()
        
        draw_window(win, world_map, player)


if __name__ == '__main__':
    main()