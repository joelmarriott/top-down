import pygame
import os


WIN_WIDTH = 1280
WIN_HEIGHT = 720
TILE_SIZE = 32


def get_image(image_name):
    image_path = os.path.join(os.path.realpath(os.path.dirname(__file__)),
                              'assets',
                              image_name+'.png')
    loaded_image = pygame.image.load(image_path)
    return loaded_image