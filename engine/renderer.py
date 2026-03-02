import pygame

class Renderer:
    def __init__(self, tile_size=32):
        self.tile_size = tile_size

    def draw_entity(self, screen, entity, color=(255, 255, 0)):
        rect = pygame.Rect(entity.x*self.tile_size, entity.y*self.tile_size,
                           self.tile_size, self.tile_size)
        pygame.draw.rect(screen, color, rect)