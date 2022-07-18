from random import choice
import pygame as pg
import constants
from components import *

class FlappyBird:
    def __init__(self):
        self.running = True
        self.screen = pg.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        self.started = False
        self.can_create_pipe = False
        self.can_create_fruit = False
        self.lost = False
        self.pipes = []
        self.fruits = []
        self.bird = None
        self.background = None
        self.floor = None
        self.restart_text = None
        self.score = None
        self.best_score = 0
        self.speed = 2

    def fly_bird(self):
        if not self.started:
            self.started = True
            self.can_create_pipe = True
        self.bird.fly()
        
    def update_screen(self):
        if self.lost:
            objects = [self.background, self.floor, self.restart_text]
        else:
            objects = [self.background, self.bird, *self.pipes, self.floor, self.score, *self.fruits]
        for obj in objects:
            obj.draw(self.screen)
        pg.display.update()
    
    def handle_exit(self):
        self.running = False
    
    def generate_pipe(self):
        self.pipes.append(Pipe())
        self.can_create_pipe = False

    def generate_fruit(self):
        self.fruits.append(Fruit())
        self.can_create_fruit = False
    
    def remove_old_pipes(self):
        for pipe in self.pipes:
            if pipe.x + pipe.width < 0:
                self.pipes.pop(self.pipes.index(pipe))
    
    def update_score(self):
        for pipe in self.pipes:
            if not pipe.passed and self.bird.x > pipe.x + pipe.width:
                pipe.passed = True
                self.score.value += 1
                self.can_create_pipe = True
                self.can_create_fruit = choice([not bool(i) for i in range(10)])
                self.speed += 2
    
    def check_collisions(self):
        has_collision = False
        if self.bird.y + self.bird.image.get_width() >= self.floor.y:
            has_collision = True
        bird_mask = self.bird.get_mask()
        for pipe in self.pipes:
            top_collision = bird_mask.overlap(pipe.get_top_mask(), (pipe.x - self.bird.x, pipe.pipe_top_y - self.bird.y))
            base_collision = bird_mask.overlap(pipe.get_base_mask(), (pipe.x - self.bird.x, pipe.pipe_base_y - self.bird.y))
            if top_collision or base_collision:
                has_collision = True
        for fruit in self.fruits:
            eat_fruit = bird_mask.overlap(fruit.get_mask(), (fruit.x - self.bird.x, fruit.y - self.bird.y))
            if eat_fruit:
                self.score.value += 2
                fruit_index = self.fruits.index(fruit)
                self.fruits.pop(fruit_index)
        if has_collision:
            if self.best_score < self.score.value:
                self.best_score = self.score.value
            self.lost = True
            self.restart_text.best_score = self.best_score
            self.restart_text.current_score = self.score.value
    
    def init_objects(self):
        self.background = Background()
        self.bird = Bird()
        self.floor = Floor()
        self.score = Score()
        self.restart_text = RestartText()

    def init_states(self):
        self.started = False
        self.lost = False
        self.pipes = []
        self.fruits = []

    def restart(self):
        self.init_states()
        self.init_objects()