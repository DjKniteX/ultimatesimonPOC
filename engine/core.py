import pygame

class Game:
    def __init__(self, width, height, fps=60):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Ultimate Simon POC")
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True
        self.scene = None

    def set_scene(self, scene):
        self.scene = scene

    def run(self):
        while self.running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            if self.scene:
                self.scene.handle_input(keys)
                self.scene.update()
                self.scene.render(self.screen)

            pygame.display.flip()

        pygame.quit()