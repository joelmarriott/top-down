import pygame
from td_common import get_image

WIN_WIDTH = 1280
WIN_HEIGHT = 720

def draw_window(win):
    tile_size = 32
    world_map = [
        [ 0, 1, 1, 1, 0 ],
        [ 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1 ],
        [ 0, 1, 1, 1, 0 ]
    ]
    start_tile_x = (WIN_WIDTH - (len(world_map[0]) * 32)) / 2
    tile_x = start_tile_x
    tile_y = (WIN_HEIGHT - (len(world_map)*32)) / 2
    for row in world_map:
        for tile in row:
            if row[tile]:
                win.blit(get_image('tile'), (tile_x, tile_y))
            tile_x += 31
        tile_x = start_tile_x
        tile_y += 31
    
    pygame.display.update()
    

def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption('Unnamed Top Down Game')
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        
        draw_window(win)


if __name__ == '__main__':
    main()