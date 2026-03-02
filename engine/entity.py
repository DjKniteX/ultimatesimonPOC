class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy, game_map):
        if not game_map.is_blocked(self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)