import pygame as pg
from constants import *


class FlappyBird:
    def __init__(self):
        self.running = True
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def fly_bird(self, bird):
        bird.fly()
        
    def update_screen(self, *objects):
        for obj in objects:
            obj.draw(self.screen)
    
    def handle_exit(self):
        self.running = False