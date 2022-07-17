from .game_object import GameObject
import constants
import pygame as pg


class Score(GameObject):
    def __init__(self):
        self.x = 30
        self.y = 20
        self.color = (255, 255, 255)
        self.image = None
        self.value = 0
    
    def draw(self, screen):
        text = f'Score: {self.value}'
        text_surface = constants.FONT.render(text, False, self.color)
        super().draw(screen, self.x, self.y, image = text_surface)