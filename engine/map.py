import json
import pygame

class GameMap:
    def __init__(self, map_file):
        with open(map_file, "r") as f:
            self.map_data = json.load(f)
        self.width = len(self.map_data[0])
        self.height = len(self.map_data)

    def is_blocked(self, x, y):
        if 0 <= y < self.height and 0 <= x < self.width:
            return self.map_data[y][x] != 0  # 0 = walkable
        return True  # Outside map = blocked

    def render(self, screen, tile_size):
        colors = {
            0: (0, 200, 0),    # Grass
            1: (100, 100, 100),# Wall
            2: (0, 0, 200)     # Water
        }
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                rect = pygame.Rect(x*tile_size, y*tile_size, tile_size, tile_size)
                pygame.draw.rect(screen, colors[tile], rect)