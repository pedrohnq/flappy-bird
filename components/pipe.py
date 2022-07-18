from random import randrange
from .game_object import GameObject
import constants
import pygame as pg

class Pipe(GameObject):
    def __init__(self):
        self.x = constants.SCREEN_WIDTH
        self.pipe_top = constants.PIPE_1
        self.pipe_base = constants.PIPE_2
        self.image = None
        self.width = self.pipe_top.get_width()
        self.passed = False
        self.pipe_top_y = randrange(-275, -50)
        self.pipe_base_y = self.pipe_top_y + self.pipe_top.get_height() + 90

    def draw(self, screen):
        self.x -= constants.SPEED_PIPES
        super().draw(screen, self.x, self.pipe_top_y, image = self.pipe_top)
        super().draw(screen, self.x, self.pipe_base_y, image = self.pipe_base)
    
    def get_top_mask(self):
        return pg.mask.from_surface(self.pipe_top)
    
    def get_base_mask(self):
        return pg.mask.from_surface(self.pipe_base)