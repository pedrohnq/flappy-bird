from random import randrange
import pygame as pg
from constants import *

class GameObject:
    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))

class Bird(GameObject):
    def __init__(self):
        self.x = BIRD_INITIAL_X
        self.y = BIRD_INITIAL_Y
        self.images = [BIRD_1, BIRD_2, BIRD_3, BIRD_2]
        self.image = self.images[0]
        self.is_falling = False
        self.remaining_frames = FRAMES_PER_IMAGE_TO_BIRD
        self.angle = 0

    def get_next_image(self):
        if self.remaining_frames == 1:
            current_image = self.images.pop(0)
            self.images.append(current_image)
            self.image = self.images[0]

        self.remaining_frames -= 1
        if self.remaining_frames < 0:
            self.remaining_frames = FRAMES_PER_IMAGE_TO_BIRD

    def draw(self, screen):
        if self.is_falling:
            self.y += 5
        super().draw(screen, self.x, self.y)
        self.get_next_image()
    
    def fly(self):
        self.is_falling = False
        self.y -= 50
        self.is_falling = True


class Background(GameObject):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = BACKGROUND
    
    def draw(self, screen):
        screen_width = screen.get_size()[0]
        aux_bg_x = screen_width + self.x
        self.x -= 0.5
        if self.x < -1 * screen_width:
            self.x = 0
        super().draw(screen, aux_bg_x, self.y)
        super().draw(screen, self.x, self.y)


class Pipe(GameObject):
    pass


class Floor(GameObject):
    def __init__(self):
        self.x = 0
        self.y = 400
        self.image = FLOOR
    def draw(self, screen):
        screen_width = screen.get_size()[0]
        aux_floor_x = screen_width + self.x
        self.x -= 2
        if self.x < -1 * screen_width:
            self.x = 0
        super().draw(screen, aux_floor_x, self.y)
        super().draw(screen, self.x, self.y)

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