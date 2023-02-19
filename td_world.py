from td_common import get_image, TILE_SIZE
import random
import pygame
import csv
import os

class WorldMap:
    def __init__(self, map_name):
        self.world_map = self.construct_map(map_name)
        self.pos_x = 0
        self.pos_y = 0
        
    def construct_map(self, map_name):
        map_matrix = self.read_in_csv(map_name)
        world_map = []
        images = [
                     0,
                     get_image('world/floor/grass'),         # 1
                     get_image('world/barrier/fence_horizontal'),             # 2
                     get_image('world/barrier/fence_left'),             # 3
                     get_image('world/barrier/fence_right'),        # 4
                     get_image('world/barrier/fence_topleft'),      # 5  (top_left)
                     get_image('world/barrier/fence_bottomleft'),  # 6  (bottom_left)
                     get_image('world/barrier/fence_bottomright'), # 7  (bottom_right)
                     get_image('world/barrier/fence_topright'), # 8  (top_right)
        ]
        for i, row in enumerate(map_matrix):
            world_map.append([])
            for tile in row:
                solid = False
                if tile <= 0:
                    image = 0
                if tile > 1:
                    image = images[tile]
                    solid = True
                if tile >= 1 and tile <= 8:
                    grass_type = random.randint(0,100)
                    if grass_type < 60:
                        subimage = get_image('world/floor/grass')
                    elif grass_type >= 80:
                        subimage = get_image('world/floor/grass_1')
                    else:
                        subimage = get_image('world/floor/grass_2')
                if tile == 1:
                    image = subimage
                    subimage = None
                world_map[i].append(Tile(image, solid, subimage))
        return world_map
    
    def read_in_csv(self, map_name):
        map_matrix = []
        directory = os.path.join(os.path.realpath(os.path.dirname(__file__)),
                              'assets',
                              'world')
        with open(os.path.join(directory, map_name+'.map')) as map_file:
            csv_reader = csv.reader(map_file, delimiter=',')
            for row in csv_reader:
                map_row = [ int(value) for value in row]
                map_matrix.append(map_row)
        return map_matrix
                
        
    def draw(self, win):
        tile_x = self.pos_x - ((len(self.world_map[0]) / 2) * 12)
        start_tile_x = tile_x
        tile_y = self.pos_y - ((len(self.world_map) / 2) * 16)
        for row in self.world_map:
            for tile in row:
                if tile:
                    tile.pos_x = tile_x
                    tile.pos_y = tile_y
                    tile.draw(win)
                tile_x += TILE_SIZE
            tile_x = start_tile_x
            tile_y += TILE_SIZE
            
            
    def check_collide(self, player):
        for row in self.world_map:
            for tile in row:
                if not tile.image:
                    continue
                tile.check_collide(player, self)
            
            
class Tile:
    def __init__(self, image, solid=False, subimage=None):
        self.pos_x = 0
        self.pos_y = 0
        self.image = image
        self.solid = solid
        self.subimage = subimage
        
    def draw(self, win):
        if self.subimage:
            win.blit(self.subimage, (self.pos_x, self.pos_y))
        if self.image:
            win.blit(self.image, (self.pos_x, self.pos_y))
        
    def check_collide(self, player, map):
        player_mask = player.get_mask()
        tile_mask = pygame.mask.from_surface(self.image)
        
        tile_offset = (self.pos_x - player.pos_x, self.pos_y - player.pos_y)
        
        hit = player_mask.overlap(tile_mask, tile_offset)
        
        if hit and self.solid:
            if player.vel_x < 0:
                map.pos_x -= round(player.speed * 2.4)

            if player.vel_x > 0:
                map.pos_x += round(player.speed * 2.4)

            if player.vel_y < 0:
                map.pos_y -= round(player.speed * 2.4)

            if player.vel_y > 0:
                map.pos_y += round(player.speed * 2.4)
                
            player.move(map)

        if hit:
            return True
        
        return False