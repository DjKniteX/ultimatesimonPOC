import pygame
from engine.core import Game
from engine.scene import Scene
from engine.map import GameMap
from engine.entity import Player
from engine.renderer import Renderer

class OverworldScene(Scene):
    def __init__(self):
        self.map = GameMap("data/map1.json")
        self.player = Player(2, 2)
        self.renderer = Renderer(tile_size=64)  # bigger tiles for visibility

    def handle_input(self, keys):
        if keys[pygame.K_UP]:
            self.player.move(0, -1, self.map)
        elif keys[pygame.K_DOWN]:
            self.player.move(0, 1, self.map)
        elif keys[pygame.K_LEFT]:
            self.player.move(-1, 0, self.map)
        elif keys[pygame.K_RIGHT]:
            self.player.move(1, 0, self.map)

    def update(self):
        pass

    def render(self, screen):
        self.map.render(screen, self.renderer.tile_size)
        self.renderer.draw_entity(screen, self.player)

if __name__ == "__main__":
    game = Game(512, 320, fps=60)
    game.set_scene(OverworldScene())
    game.run()