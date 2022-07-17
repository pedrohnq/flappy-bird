from random import randrange
from .game_object import GameObject
import constants

class Pipe(GameObject):
    def __init__(self):
        self.x = constants.SCREEN_WIDTH
        self.y = randrange(-275, -50)
        self.images = [constants.PIPE_1, constants.PIPE_2]
        self.image = None
        self.width = self.images[0].get_width()
        self.passed = False

    def draw(self, screen):
        self.x -= 2
        super().draw(screen, self.x, self.y, image = self.images[0])
        super().draw(screen, self.x, self.y + self.images[0].get_height() + 90, image = self.images[1])