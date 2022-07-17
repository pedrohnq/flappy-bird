from .game_object import GameObject
import constants
import pygame as pg

class Bird(GameObject):
    def __init__(self):
        self.x = constants.BIRD_INITIAL_X
        self.y = constants.BIRD_INITIAL_Y
        self.images = [constants.BIRD_1, constants.BIRD_2, constants.BIRD_3, constants.BIRD_2]
        self.image = self.images[0]
        self.is_falling = False
        self.remaining_frames = constants.FRAMES_PER_IMAGE_TO_BIRD
        self.angle = 0

    def get_next_image(self):
        if self.remaining_frames == 1:
            current_image = self.images.pop(0)
            self.images.append(current_image)
            self.image = self.images[0]

        self.remaining_frames -= 1
        if self.remaining_frames < 0:
            self.remaining_frames = constants.FRAMES_PER_IMAGE_TO_BIRD

    def draw(self, screen):
        if self.is_falling:
            self.y += 5
        super().draw(screen, self.x, self.y)
        self.get_next_image()
    
    def fly(self):
        self.is_falling = False
        self.y -= 50
        self.is_falling = True
    
    def get_mask(self):
        return pg.mask.from_surface(self.image)