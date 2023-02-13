import pygame
from td_common import get_image, WIN_WIDTH, WIN_HEIGHT
from td_world import WorldMap


def draw_window(win):
    world_map = WorldMap()
    world_map.draw(win)
    
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