import pygame as pg
from constants import *


class FlappyBird:
    def __init__(self):
        self.running = True
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.started = False
        self.score = 0
        self.can_create_pipe = False

    def fly_bird(self, bird):
        if not self.started:
            self.started = True
            self.can_create_pipe = True
        bird.fly()
        
    def update_screen(self, *objects):
        for obj in objects:
            obj.draw(self.screen)
    
    def handle_exit(self):
        self.running = False
    
    def generate_pipe(self, PipeClass):
        self.can_create_pipe = False
        return PipeClass()
    
    def remove_old_pipes(self, pipes):
        for pipe in pipes:
            if pipe.x + pipe.width < 0:
                pipes.pop(pipes.index(pipe))
    
    def update_score(self, pipes, bird):
        for pipe in pipes:
            if not pipe.passed and bird.x > pipe.x + pipe.width:
                pipe.passed = True
                self.score += 1
                self.can_create_pipe = True