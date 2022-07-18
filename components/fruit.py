from random import randrange
from .game_object import GameObject
import constants
import pygame as pg

class Fruit(GameObject):
    def __init__(self):
        self.x = constants.SCREEN_WIDTH + randrange(100, 150)
        self.y = randrange(10, 350)
        self.image = constants.FRUIT
        self.eat = False

    def draw(self, screen):
        self.x -= constants.SPEED_PIPES
        super().draw(screen, self.x, self.y)
    
    def get_mask(self):
        return pg.mask.from_surface(self.image)