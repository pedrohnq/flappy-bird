import pygame as pg
from constants import *

class GameObject:
    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))

class Bird(GameObject):
    def __init__(self):
        pass

class Background(GameObject):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = BACKGROUND
    
    def draw(self, screen):
        self.x -= 1
        screen_width = screen.get_size()[0]
        if self.x < -1 * screen_width:
            self.x = 0
        second_bg_x = screen_width + self.x
        super().draw(screen, self.x, self.y)
        super().draw(screen, second_bg_x, self.y)

class Pipe(GameObject):
    pass

class Floor(GameObject):
    pass

class FlappyBird:
    def __init__(self):
        self.running = True
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    def update_screen(self, background):
        background.draw(self.screen)