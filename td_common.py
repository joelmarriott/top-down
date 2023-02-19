import pygame
import os


WIN_WIDTH = 640
WIN_HEIGHT = 360
TILE_SIZE = 32


def get_image(image_name, degrees=0):
    image_path = os.path.join(os.path.realpath(os.path.dirname(__file__)),
                              'assets',
                              image_name+'.png')
    loaded_image = pygame.image.load(image_path)
    if degrees:
        loaded_image = pygame.transform.rotate(loaded_image, degrees)
    return loaded_image


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