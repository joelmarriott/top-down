from td_common import get_image, WIN_WIDTH, WIN_HEIGHT, TILE_SIZE
import pygame

class WorldMap:
    def __init__(self, map_matrix):
        self.world_map = []
        self.construct_map(map_matrix)
        
    def construct_map(self, map_matrix):
        images = [
                     0,
                     get_image('tile_path'),          # 1
                     get_image('tile_x'),             # 2
                     get_image('tile_y'),             # 3
                     get_image('tile_x', 180),        # 4
                     get_image('tile_y', 180),        # 5
                     get_image('tile_corner_2'),      # 6  (top_left)
                     get_image('tile_corner_2', 90),  # 7  (bottom_left)
                     get_image('tile_corner_2', 180), # 8  (bottom_right)
                     get_image('tile_corner_2', -90), # 9  (top_right)
                     get_image('tile_fill')           # 10
        ]
        for i, row in enumerate(map_matrix):
            self.world_map.append([])
            for tile in row:
                if tile > 1:
                    solid = True
                else:
                    solid = False
                self.world_map[i].append(Tile(images[tile], solid))
        
    def draw(self, win):
        tile_x = (WIN_WIDTH - (len(self.world_map[0]) * TILE_SIZE)) / 2
        start_tile_x = tile_x
        tile_y = (WIN_HEIGHT - (len(self.world_map)* TILE_SIZE)) / 2
        for row in self.world_map:
            for tile in row:
                if tile:
                    tile.pos_x = tile_x
                    tile.pos_y = tile_y
                    tile.draw(win)
                tile_x += TILE_SIZE - 1
            tile_x = start_tile_x
            tile_y += TILE_SIZE - 1
            
            
    def check_collide(self, player):
        for row in self.world_map:
            for tile in row:
                if not tile.image:
                    continue
                tile.check_collide(player)
            
            
class Tile:
    def __init__(self, image, solid=False):
        self.pos_x = 0
        self.pos_y = 0
        self.image = image
        self.solid = solid
        
    def draw(self, win):
        if self.image:
            win.blit(self.image, (self.pos_x, self.pos_y))
        
    def check_collide(self, player):
        player_mask = player.get_mask()
        tile_mask = pygame.mask.from_surface(self.image)
        
        tile_offset = (self.pos_x - player.pos_x, self.pos_y - player.pos_y)
        
        hit = player_mask.overlap(tile_mask, tile_offset)
        
        if hit and self.solid:
            if player.vel_x < 0:
                player.pos_x += round(player.speed * 1.9)

            if player.vel_x > 0:
                player.pos_x -= round(player.speed * 1.9)

            if player.vel_y < 0:
                player.pos_y += round(player.speed * 1.9)

            if player.vel_y > 0:
                player.pos_y -= round(player.speed * 1.9)
                
            player.move()

        if hit:
            return True
        
        return False