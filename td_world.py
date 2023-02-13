from td_common import get_image, WIN_WIDTH, WIN_HEIGHT, TILE_SIZE

class WorldMap:
    def __init__(self):
        pass
        
    def draw(self, win):
        world_map = [
            [ 0, 1, 1, 1, 0 ],
            [ 1, 1, 1, 1, 1 ],
            [ 1, 1, 1, 1, 1 ],
            [ 1, 1, 1, 1, 1 ],
            [ 0, 1, 1, 1, 0 ]
        ]
        tile_x = (WIN_WIDTH - (len(world_map[0]) * TILE_SIZE)) / 2
        start_tile_x = tile_x
        tile_y = (WIN_HEIGHT - (len(world_map)* TILE_SIZE)) / 2
        for row in world_map:
            for tile in row:
                if row[tile]:
                    win.blit(get_image('tile'), (tile_x, tile_y))
                tile_x += TILE_SIZE - 1
            tile_x = start_tile_x
            tile_y += TILE_SIZE - 1